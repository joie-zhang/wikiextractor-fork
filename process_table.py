import json
import glob
import pandas as pd
from tqdm import tqdm
from urllib.parse import unquote
import io

import sys
sys.path.append("/scratch/gpfs/hyen/ALCE")
from utils import normalize_answer # use this to check the answers

threshold = 25

def normalize_title(title):
    if title is None:
        return None
    title = unquote(title)
    return title.strip()

def keep_table(table, corpus):
    """
    For each table, we apply the following heuristics:
    1. extract all the links and map them to natural texts in wikipedia articles
    2. keep the rows where there is at least one valid link
    3. for each value in the row, we check if it is answerable (e.g., it's not null and exists as a substring in the linked text)
    4. we remove any column or row that are all not answerable
    5. keep if there are at least threshold number of answerable values
    6. leave the rest for manual inspection
    """

    table = pd.read_json(io.StringIO(table), orient="records")

    # extract the links
    links = table.map(lambda x: x[1] if isinstance(x, list) else None)
    # only keep the ones that are in our corpus
    linked_text = links.map(lambda x: corpus.get(normalize_title(x), None))
    linked_text['all'] = linked_text.agg(lambda x: '\n\n'.join([y.strip() for y in x if y is not None]), axis=1)

    #values = table.map(lambda x: x if x is None else x[0] if x[0] else None)
    values = table.map(lambda x: x[0] if isinstance(x, list) and x[0] else None)

    # only keep the rows where there is at least one valid link
    values = values[linked_text['all'] != ""]
    filtered_links = linked_text[linked_text['all'] != ""]

    kept = []
    answerable = []
    index = []
    for i, row in values.iterrows():
        text = normalize_answer(linked_text['all'][i])
        # might want to change how numbers are checked
        answerable.append({k: v is not None and normalize_answer(v) in text for k, v in row.items()})
        index.append(row.name)

    answerable = pd.DataFrame(answerable, index=index)

    # remove any column or row that are all not answerable
    if answerable.sum().sum() == 0:
        return None
    values = values[answerable.any(axis=1)]
    values = values.loc[:, answerable.any(axis=0)]
    filtered_link = filtered_links[answerable.any(axis=1)]

    count = values.size - values.isna().sum().sum()

    if count < threshold:
        return None

    answerable = answerable[answerable.any(axis=1)]
    answerable = answerable.loc[:, answerable.any(axis=0)]
    values = json.loads(values.to_json(orient="records"))
    provenance = filtered_links['all'].tolist()
    answerable = json.loads(answerable.to_json(orient="records"))
    return {'data': values, 'provenance': provenance, 'answerable': answerable}
    #return values, filtered_links['all']


def load_corpus():
    corpus = {}
    with open("output.jsonl") as f:
        for line in f:
            d = json.loads(line)
            corpus[d['title'].strip()] = d['text']
    return corpus


if __name__ == "__main__":
    output = []
    print('loading corpus')
    corpus = load_corpus()

    print('processing tables')
    files = glob.glob("linked_text/*/*")
    total_tables = 0
    for file in tqdm(files):
        with open(file) as f:
            for line in f:
                data = json.loads(line)

                if data['tables'] is None:
                    continue

                for table in data['tables']:
                    total_tables += 1
                    t = keep_table(table, corpus)
                    if t is not None:
                        t['id'] = data['id']
                        t['revid'] = data['revid']
                        t['text'] = corpus[data['title']]
                        t['title'] = data['title']
                        t['url'] = data['url']
                        output.append(t)

    print(f"total tables: {total_tables}, kept tables: {len(output)}")

    with open("wikitable_test.jsonl", 'w') as f:
        for o in output:
            f.write(json.dumps(o) + "\n")

