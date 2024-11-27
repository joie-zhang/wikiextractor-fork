import pytablereader as ptr

confederation = '''
{|
|+ Results by confederation
!scope="col"| Confederation
!scope="col"| Appearances
!scope="col"| Winners
!scope="col"| Runners-up
|-
! scope="row"| [[UEFA]]
| 29
| 12
| 17
|-
!scope="row"| [[CONMEBOL]]
| 15
| 10
| 5
|}
'''

tallest_buildings = '''
{|
! rowspan=2 |Number
! rowspan=2 |Name
! colspan=2 |Height
! rowspan=2 |Floors
! rowspan=2 class="unsortable" |Image
! rowspan=2 |City
! rowspan=2 |Country
! rowspan=2 |Year
! rowspan=2 class="unsortable" |Comments
! rowspan=2 class="unsortable" |Refs
|-
! m
! ft
|- style="background:#dfd;"
|1
| \'\'\'[[Burj Khalifa]]\'\'\'
| {{cvt|828.0|m|ft|disp=table|0}}
| 163 (+ 2 below ground)
| [[File:Burj Khalifa.jpg|frameless|100px]]
| [[Dubai]]
| {{Flag|United Arab Emirates}}
| 2010
| Tallest building in the world since 2009, tallest building in the [[Eastern Hemisphere|Eastern]] and [[Northern Hemisphere]], [[Asia]], the [[Arab world]], the [[Middle East]], the [[Arabian Peninsula]] and the [[List of tallest buildings in the United Arab Emirates|UAE]]
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/burj-khalifa/3|title = Burj Khalifa - the Skyscraper Center}}</ref>
|-
|2
| [[Merdeka 118]]
| {{cvt|678.9|m|ft|disp=table|0}}
| 118 (+ 5 below ground)
| [[File:Merdeka 118 20230317.jpg|frameless|100px]]
| [[Kuala Lumpur]]
| {{Flag|Malaysia}}
| 2024
|Tallest building in [[List of tallest buildings in Southeast Asia|Southeast Asia]], [[ASEAN]] and [[List of tallest buildings in Malaysia|Malaysia]]
| <ref>{{Cite web|title=Merdeka PNB118 – The Skyscraper Center|url=http://www.skyscrapercenter.com/building/merdeka-pnb118/10115|access-date=|website=}}</ref>
|-
|3
| [[Shanghai Tower]]
| {{cvt|632.0|m|ft|disp=table|0}}
| 128 (+ 5 below ground)
| [[File:Shanghai Tower in 2015 (2).jpg|frameless|100px]]
| [[Shanghai]]
| {{Flag|China}}
| 2015
|Tallest building in [[East Asia]] and [[List of tallest buildings in China|China]] and contains the highest luxury hotel in the world; [[List of twisted buildings|Tallest twisted building]]
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/shanghai-tower/56|title = Shanghai Tower - the Skyscraper Center}}</ref>
|-
|4
| [[The Clock Towers|Abraj Al-Bait Clock Tower]]
| {{cvt|601.0|m|ft|disp=table|0}}
| 120 (+ 3 below ground)
| [[File:Abraj-al-Bait-Towers.JPG|frameless|133x133px]]
| [[Mecca]]
| {{Flag|Saudi Arabia}}
| 2012
| Tallest building in [[Saudi Arabia]], tallest [[Clock tower|clock tower]] and contains the [[Clock Tower Museum|highest museum in the world]]
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/makkah-royal-clock-tower/84|title=Makkah Royal Clock Tower - The Skyscraper Center|website=www.skyscrapercenter.com}}</ref>
|-
|5
| [[Ping An International Finance Centre]]
| {{cvt|599.1|m|ft|disp=table|0}}
| 115 (+ 5 below ground)
| [[File:Pingan International Finance Center2020.jpg|frameless|100px]]
| [[Shenzhen]]
| {{Flag|China}}
| 2017
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/ping-an-finance-center/54|title = Ping an Finance Center - the Skyscraper Center}}</ref>
|-
|6
| [[Lotte World Tower]]
| {{cvt|554.5|m|ft|disp=table|0}}
| 123 (+ 6 below ground)
| [[File:Lotte World Tower 2019.jpg|frameless|100px]]
| [[Seoul]]
| {{Flag|South Korea}}
| 2017
| Tallest building in [[List of tallest buildings in South Korea|South Korea]] and the [[OECD]]
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/lotte-world-tower/88|title = Lotte World Tower - the Skyscraper Center}}</ref>
|-
|7
| [[One World Trade Center]]
| {{cvt|541.3|m|ft|disp=table|0}}
| 94 (+ 5 below ground)
| [[File:New York and Jersey City Skyline Panorama Crop Edit - One World Trade Center.jpg|frameless|100px]]
| [[New York City]]
| {{Flag|United States}}
| 2014
| Tallest building outside of Asia; tallest building in the [[Western Hemisphere]], the [[Americas]], [[List of tallest buildings in North America|North America]] and the [[List of tallest buildings in the United States|USA]]; tallest building on an island
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/one-world-trade-center/98|title = One World Trade Center - the Skyscraper Center}}</ref>
|-
| rowspan=2 |8
| [[Guangzhou CTF Finance Centre]]
| rowspan=2 | 530.0 || rowspan=2 | {{cvt|530|m|ft|disp=number}}
| 111 (+ 5 below ground)
| [[File:Guangzhou CTF Finance Center.jpg|frameless|100px]]
| [[Guangzhou]]
| rowspan=3 |{{Flag|China}}
| 2016
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/guangzhou-ctf-finance-centre/176|title = Guangzhou CTF Finance Centre - the Skyscraper Center}}</ref>
|-
| {{left}} [[Tianjin CTF Finance Centre]]
| 97 (+ 4 below ground)
| [[File:Tianjin CTF Finance Centre in 2019.jpg|frameless|100px]]
| [[Tianjin]]
| 2019
| Τallest building in the world with fewer than 100 floors
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/tianjin-ctf-finance-centre/310|title=Tianjin CTF Finance Centre - The Skyscraper Center|website=www.skyscrapercenter.com}}</ref>
|-
|10
| [[China Zun|CITIC Tower]]
| {{cvt|527.7|m|ft|disp=table|0}}
| 109 (+ 8 below ground)
| [[File:CITIC Tower 2021.jpg|frameless|100px]]
| [[Beijing]]
| 2018
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/citic-tower/11116|title = CITIC Tower - the Skyscraper Center}}</ref>
|- style="background:#dfd;"
|11
| \'\'\'[[Taipei 101]]\'\'\'
| {{cvt|508.0|m|ft|disp=table|0}}
| 101 (+ 5 below ground)
| [[File:Taipei 101 in 2019.jpg|frameless|100px]]
| [[Taipei]]
| {{Flag|Taiwan}}
| 2004
| Tallest building in the world from 2004 till 2010; tallest building in [[List of tallest buildings in Taiwan|Taiwan]]
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/taipei-101/117|title = TAIPEI 101 - the Skyscraper Center}}</ref>
|-
|12
| [[Shanghai World Financial Center]]
| {{cvt|492.0|m|ft|disp=table|0}}
| 101 (+ 3 below ground)
| [[File:上海国际金融中心.jpg|frameless|100px]]
| Shanghai
| {{Flag|China}}
| 2008
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/shanghai-world-financial-center/131|title = Shanghai World Financial Center - the Skyscraper Center}}</ref>
|-
|13
| [[International Commerce Centre]]
| {{cvt|484.0|m|ft|disp=table|0}}
| 108 (+ 4 below ground)
| [[File:International Commerce Centre in 201008.jpg|frameless|100px]]
| [[Hong Kong]]
| {{Flag|China}}
| 2010
| Tallest building in [[List of tallest buildings in Hong Kong|Hong Kong]]
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/international-commerce-centre/137|title=International Commerce Centre - The Skyscraper Center|website=www.skyscrapercenter.com}}</ref>
|-
|14
| [[Wuhan Greenland Center]]
| {{cvt|475.6|m|ft|disp=table|0}}
| 101 (+ 6 below ground)
| [[File:Wuhan Greenland Center.jpg|frameless|100px]]
| [[Wuhan]] 
| {{Flag|China}}
| 2023
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/wuhan-greenland-center/33983|title = Wuhan Greenland Center - the Skyscraper Center}}</ref>
|-
|15
| [[Central Park Tower]]
| {{cvt|472.4|m|ft|disp=table|0}}
| 98 (+ 4 below ground)
| [[File:Central Park Tower April 2021.jpg|frameless|100px]]
| New York City
| {{Flag|United States}}
| 2021
| [[List of tallest residential buildings|Tallest residential building]]
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/central-park-tower/14269|title=Central Park Tower - The Skyscraper Center|website=www.skyscrapercenter.com}}</ref>
|-
|16
| [[Lakhta Center]]
| {{cvt|462.0|m|ft|disp=table|0}}
| 87 (+ 3 below ground)
| [[File:Lakhta Center in 2018.jpg|frameless|100px]]
| [[Saint Petersburg]]
| {{Flag|Russia}}
| 2019
| Tallest building in [[List of tallest buildings in Europe|Europe]] and [[List of tallest buildings in Russia|Russia]]; Northernmost skyscraper in the world
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/lakhta-center/12575|title = Lakhta Center - the Skyscraper Center}}</ref>
|-
|17
| [[Landmark 81]]
| {{cvt|461.2|m|ft|disp=table|0}}
| 81 (+ 3 below ground)
| [[File:The Landmark 81 at night.jpg|frameless|100px]]
| [[Ho Chi Minh City]]
| {{Flag|Vietnam}}
| 2018
| Tallest building in [[List of tallest buildings in Vietnam|Vietnam]]
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/vincom-landmark-81/18192|title=Vincom Landmark 81 - The Skyscraper Center|website=www.skyscrapercenter.com}}</ref>
|-
| 18
| [[Chongqing International Trade and Commerce Center|Chongqing International Land-Sea Center]]
| {{cvt|458.0|m|ft|disp=table|0}}
| 98 (+ 4 below ground)
| [[File:陆海国际中心2024.5.jpg|frameless|100px]]
| [[Chongqing]]
| {{Flag|China}}
| 2024
| 
|
|-
|19
| [[The Exchange 106]]
| {{cvt|453.6|m|ft|disp=table|0}}
| 95 (+ 6 below ground)
| [[File:The Exchange 106 20230317.jpg|frameless|100px]]
| Kuala Lumpur
| {{Flag|Malaysia}}
| 2019
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/the-exchange-106/24971|title = The Exchange 106 - the Skyscraper Center}}</ref>
|-
|20
| [[Changsha IFS Tower T1]]
| {{cvt|452.1|m|ft|disp=table|0}}
| 94 (+ 5 below ground)
| [[File:Changsha IFS 2021.jpg|frameless|100px]]
| [[Changsha]]
| {{Flag|China}}
| 2018
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/changsha-ifs-tower-t1/13144|title=Changsha IFS Tower T1 - The Skyscraper Center|website=www.skyscrapercenter.com}}</ref>
|- style="background:#dfd;"
| rowspan=2 |21
| [[Petronas Towers|\'\'\'Petronas Tower&amp;nbsp;1\'\'\']]
| rowspan=2 | 451.9 || rowspan=2 | {{cvt|451.9|m|ft|disp=number}}
| rowspan=2 |88 (+ 5 below ground)
| rowspan=2 |[[File:The Twins SE Asia 2019 (49171985716) (cropped) 2.jpg|100px]]
| rowspan=2 | Kuala Lumpur
| rowspan=2 |{{Flag|Malaysia}}
| rowspan=2 |1998
| rowspan=2 |Tallest building in the world from 1998 till 2004; tallest building built in the 20th century; [[List of tallest twin buildings and structures|Tallest twin buildings]]
| rowspan=2 | <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/petronas-twin-tower-1/149|title = Petronas Twin Tower 1 - the Skyscraper Center}}</ref><ref>{{Cite web|url=https://www.skyscrapercenter.com/building/petronas-twin-tower-2/150|title = Petronas Twin Tower 2 - the Skyscraper Center}}</ref>
|- style="background:#dfd;"
| {{left}} [[Petronas Towers|\'\'\'Petronas Tower&amp;nbsp;2\'\'\']]
|-
| rowspan=2 | 23
| [[Zifeng Tower]]
| rowspan=2 | 450.0 || rowspan=2 | {{cvt|450|m|ft|disp=number}}
| 89 (+ 5 below ground)
| [[File:Zifeng Tower in 2017.jpg|frameless|100px]]
| [[Nanjing]]
| rowspan=3 |{{Flag|China}}
| 2010
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/zifeng-tower/165|title = Zifeng Tower - the Skyscraper Center}}</ref>
|-
| {{left}} [[Suzhou IFS]]
| 95 (+ 5 below ground)
| [[File:Suzhou IFS 2018.jpg|frameless|100px]]
| [[Suzhou]]
| 2019
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/suzhou-ifs/196|title = Suzhou IFS - the Skyscraper Center}}</ref>
|-
|25
| [[Wuhan Center]]
| {{cvt|443.1|m|ft|disp=table|0}}
| 88 (+ 4 below ground)
| [[File:Wuhan Center 201704.jpg|frameless|100px]]
| Wuhan
| 2019
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/wuhan-center-tower/8823|title = Wuhan Center Tower - the Skyscraper Center}}</ref>
|- style="background:#dfd;"
|26
| \'\'\'[[Willis Tower]]\'\'\'
| {{cvt|442.1|m|ft|disp=table|0}}
| 108 (+ 3 below ground)
| [[File:Willis_Tower_From_Lake.jpg|frameless|100px]]
| [[Chicago]]
| {{Flag|United States}}
| 1974
| Tallest building in the world from 1974 till 1998
|  <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/willis-tower/169|title = Willis Tower - the Skyscraper Center}}</ref>
|-
|27
| [[KK100]]
| {{cvt|441.8|m|ft|disp=table|0}}
| 98 (+ 4 below ground)
| [[File:KK100 exterior southeast.jpg|frameless|100px]]
| Shenzhen
| rowspan=2 |{{Flag|China}}
| 2011
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/kk100/173|title=KK100 - The Skyscraper Center|website=www.skyscrapercenter.com}}</ref>
|-
|28
| [[Guangzhou International Finance Center]]
| {{cvt|438.6|m|ft|disp=table|0}}
| 101 (+ 4 below ground)
| [[File:Guangzhou International Finance Center.jpg|frameless|100px]]
| Guangzhou
| 2010
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/guangzhou-international-finance-center/174|title=Guangzhou International Finance Center - The Skyscraper Center|website=www.skyscrapercenter.com}}</ref>
|-
|29
| [[111 West 57th Street]]
| {{cvt|435.3|m|ft|disp=table|0}}
| 84 (+ 2 below ground)
| [[File:111 West 57th Street.png|frameless|100px]]
| New York City
| {{Flag|United States}}
| 2021
| Slenderest skyscraper in the world
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/111-west-57th-street/14320|title = 111 West 57th Street - the Skyscraper Center}}</ref><ref>{{Cite web|url=https://edition.cnn.com/style/article/steinway-tower-intl-scli/index.html|title = The world's skinniest skyscraper is ready for its first residents - CNN| date=6 April 2022 }}</ref>
|-
|30
| [[Shandong IFC|Shandong International Financial Center]]
| {{cvt|428|m|ft|disp=table|0}}
| 88 (+ 4 below ground)
|
| [[Jinan]]
| {{Flag|China}}
| 2023
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/greenland-shandong-international-financial-center/30121|title=Shandong International Financial Center - The Skyscraper Center|website=www.skyscrapercenter.com}}</ref> 
|-
|31
| [[One Vanderbilt]]
| {{cvt|427.0|m|ft|disp=table|0}}
| 62 (+ 4 below ground)
| [[File:One Vanderbilt in April 2021 (2).jpg|frameless|100px]]
|New York City
|{{Flag|United States}}
| 2020
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/one-vanderbilt-avenue/15833|title=One Vanderbilt Avenue - The Skyscraper Center|website=www.skyscrapercenter.com}}</ref>
|-
|32
|Nanjing Financial City Phase II Plot C Tower 1
|426
|1,398
|88
|
|Nanjing
|China
|2025
|
|<ref>{{Cite web |title=Nanjing Financial City Phase II Plot C Tower 1 - The Skyscraper Center |url=https://www.skyscrapercenter.com/building/nanjing-financial-city-phase-ii-plot-c-tower-1/24137 |access-date=2024-07-13 |website=www.skyscrapercenter.com}}</ref>
|-
|33
| [[432 Park Avenue]]
| {{cvt|425.7|m|ft|disp=table|0}}
| 85 (+ 3 below ground)
| [[File:432 Park Avenue, NY (cropped)2.jpg|frameless|100px]]
|New York City
|{{Flag|United States}}
| 2015
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/432-park-avenue/13227|title=432 Park Avenue - The Skyscraper Center|website=www.skyscrapercenter.com}}</ref>
|-
|34
| [[Marina 101]]
| {{cvt|425.0|m|ft|disp=table|0}}
| 101 (+ 6 below ground)
| [[File:Marina 101.jpg|frameless|100px]]
| Dubai
| {{Flag|United Arab Emirates}}
| 2017
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/marina-101/207|title = Marina 101 - the Skyscraper Center}}</ref>
|-
|35
| [[Trump International Hotel and Tower (Chicago)|Trump International Hotel and Tower]]
| {{cvt|423.2|m|ft|disp=table|0}}
| 98 (+ 2 below ground)
| [[File:Trump International Hotel and Tower 2022.jpg|frameless|100px]]
| Chicago
| {{Flag|United States}}
| 2009
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/trump-international-hotel-tower/203|title = Trump International Hotel &amp; Tower - the Skyscraper Center}}</ref>
|-
|36
|[[270 Park Avenue (2021–present)|JPMorgan Chase World Headquarters]]
|423
|1,388
|60
|
|New York City
|{{Flag|United States}}
|2025
|
|<ref>{{Cite web |title=JPMorgan Chase World Headquarters - The Skyscraper Center |url=https://www.skyscrapercenter.com/building/jpmorgan-chase-world-headquarters/34450 |access-date=2024-07-13 |website=www.skyscrapercenter.com}}</ref>
|-
|37
| [[Dongguan International Trade Center&amp;nbsp;1|Minying International Trade Center 1]]
| {{cvt|422.6|m|ft|disp=table|0}}
| 85 (+ 3 below ground)
| [[File:Minying International Trade Center T2 in 2021.jpg|frameless|100px]]
| [[Dongguan]]
| rowspan="2" |{{flag|China}}
| 2021
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/dongguan-international-trade-center-1/14196|title = Minying International Trade Center T2 - the Skyscraper Center}}</ref>
|-
|38
| [[Jin Mao Tower]]
| {{cvt|420.5|m|ft|disp=table|0}}
| 88 (+ 3 below ground)
| [[File:Jin Mao Tower 2007.jpg|frameless|100px]]
| Shanghai
| 1999
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/jin-mao-tower/189|title = Jin Mao Tower - the Skyscraper Center}}</ref>
|-
|39
| [[Princess Tower]]
| {{cvt|413.4|m|ft|disp=table|0}}
| 101 (+ 6 below ground)
| [[File:Princess Tower.jpg|100px]]
| Dubai
| {{Flag|United Arab Emirates}}
| 2012
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/princess-tower/206|title=Princess Tower - The Skyscraper Center|website=www.skyscrapercenter.com}}</ref>
|-
|40
| [[Al Hamra Tower]]
| {{cvt|412.6|m|ft|disp=table|0}}
| 80 (+ 3 below ground)
| [[File:Al Hamra Tower.jpg|100px]]
| [[Kuwait City]]
| {{Flag|Kuwait}}
| 2011
| Tallest building in [[List of tallest buildings in Kuwait|Kuwait]]
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/al-hamra-tower/208|title=Al Hamra Tower - The Skyscraper Center|website=www.skyscrapercenter.com}}</ref>
|-
|41
| [[International Finance Centre (Hong Kong)|Two International Finance Centre]]
| {{cvt|412.0|m|ft|disp=table|0}}
| 88 (+ 6 below ground)
| [[File:HK International Finance Centre 200809 3.jpg|frameless|100px]]
| Hong Kong
| {{Flag|China}}
| 2003
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/two-international-finance-centre/205|title=Two International Finance Centre - The Skyscraper Center|website=www.skyscrapercenter.com}}</ref>
|-
|42
| [[Haeundae LCT The Sharp|Haeundae LCT The Sharp Landmark Tower]]
| {{cvt|411.6|m|ft|disp=table|0}}
| 101 (+ 5 below ground)
| [[File:Haeundae LCT The Sharp 20200522.jpg|frameless|100px]]
| [[Busan]]
| {{Flag|South Korea}}
| 2019
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/lct-the-sharp-landmark-tower/108|title = LCT the Sharp Landmark Tower - the Skyscraper Center}}</ref>
|-
|43
|[[Ningbo Center|Ningbo Central Plaza]]
|409
|1,342
|80
|
|Ningbo
| rowspan="3" |{{Flag|China}}
|2024
|
|<ref>{{Cite web |title=Ningbo Central Plaza Tower 1 - The Skyscraper Center |url=https://www.skyscrapercenter.com/building/ningbo-central-plaza-tower-1/13153 |access-date=2024-07-13 |website=www.skyscrapercenter.com}}</ref>
|-
|44
| [[Guangxi China Resources Tower]]
| {{cvt|402.7|m|ft|disp=table|0}}
| 86 (+ 3 below ground)
|
| [[Nanning]]
| 2020
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/guangxi-china-resources-tower/33180|title = Guangxi China Resources Tower - the Skyscraper Center}}</ref>
|-
|45
| [[Guiyang International Financial Center|Guiyang International Financial Center T1]]
| {{cvt|401.0|m|ft|disp=table|0}}
| 79 (+ 5 below ground)
| [[File:Guiyang International Financial Center.jpg|frameless|100px]]
| [[Guiyang]]
| 2020
|
| <ref name="gt">{{ctbuh | id = 13896| title = Guiyang Financial Center Tower 1 }}</ref><ref>{{Cite web|url=https://www.skyscrapercenter.com/building/guiyang-international-financial-center-t1/33699|title = Guiyang International Financial Center T1 - the Skyscraper Center}}</ref>
|-
|46
| [[Iconic Tower (Egypt)|Iconic Tower]]
| {{cvt|393.8|m|ft|disp=table|0}}
| 77 (+ 2 below ground)
| [[File:Iconic_tower_of_Egypt.jpg|frameless|100px]]
| [[New Administrative Capital]]
| {{Flag|Egypt}}
| 2023
| Tallest building in [[List of tallest buildings in Africa|Africa]] and [[Egypt]]
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/iconic-tower/34420|title= Iconic Tower - The Skyscraper Center|website=www.skyscrapercenter.com}}</ref>
|-
|47
| [[China Resources Headquarters|China Resources Tower]]
| {{cvt|392.5|m|ft|disp=table|0}}
| 68 (+ 5 below ground)
| [[File:China Resources Headquarters in Dec 2020.jpg|frameless|100px]]
| Shenzhen
| {{Flag|China}} 
| 2018
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/china-resources-tower/14589|title=China Resources Tower - The Skyscraper Center|website=www.skyscrapercenter.com}}</ref>
|-
|48
| [[23 Marina]]
| {{cvt|392.4|m|ft|disp=table|0}}
| 88 (+ 4 below ground)
| [[File:23 Marina.jpg|frameless|50px]]
| Dubai
| {{Flag|United Arab Emirates}}
| 2012
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/23-marina/247|title = 23 Marina - the Skyscraper Center}}</ref>
|-
|49
| [[CITIC Plaza]]
| {{cvt|390.2|m|ft|disp=table|0}}
| 80 (+ 2 below ground)
| [[File:CITIC Plaza 2017.jpg|frameless|100px]]
| Guangzhou
| rowspan="3" |{{Flag|China}}
| 1996
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/citic-plaza/242|title=CITIC Plaza - The Skyscraper Center|website=www.skyscrapercenter.com}}</ref>
|-
|50
| Citymark Centre
| {{cvt|388.3|m|ft|disp=table|0}}
| 70 (+ 7 below ground)
|
| rowspan="2" |Shenzhen
| 2022
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/citymark-centre/22997|title=CITYMARK CENTRE - The Skyscraper Center|website=www.skyscrapercenter.com}}</ref>
|-
|51
| [[Shum Yip Upperhills Tower 1]]
| {{cvt|388.1|m|ft|disp=table|0}}
| 80 (+ 3 below ground)
| [[File:Shum Yip Upperhills Towers2020.jpg|100px]]
| 2020
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/shum-yip-upperhills-tower-1/16001|title=Shum Yip Upperhills Tower 1 - The Skyscraper Center|website=www.skyscrapercenter.com}}</ref>
|-
|52
| [[30 Hudson Yards]]
| {{cvt|387.1|m|ft|disp=table|0}}
| 73 (+ 1 below ground)
| [[File:30 Hudson Yards in 2021.jpg|frameless|100px]]
| New York City
| {{Flag|United States}}
| 2019
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/30-hudson-yards/13325|title=30 Hudson Yards - The Skyscraper Center|website=www.skyscrapercenter.com}}</ref>
|-
|53
| [[Public Investment Fund Tower]]
| {{cvt|385.0|m|ft|disp=table|0}}
| 72 (+ 4 below ground)
|
| [[Riyadh]]
| {{Flag|Saudi Arabia}}
| 2021
|
|
|-
|54
| [[Shun Hing Square]]
| {{cvt|384.0|m|ft|disp=table|0}}
| 69 (+ 3 below ground)
| [[File:Shun Hing Square 2021.jpg|frameless|100px]]
| Shenzhen
| rowspan="2" |{{Flag|China}}
| 1996
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/shun-hing-square/258|title = Shun Hing Square - the Skyscraper Center}}</ref>
|-
|55
| [[Eton Place Dalian|Eton Place Dalian Tower&amp;nbsp;1]]
| {{cvt|383.2|m|ft|disp=table|0}}
| 80 (+ 4 below ground)
| [[File:Eton Place Dalian Tower, Aug2018(cropped).jpg|frameless|100px]]
| [[Dalian]]
| 2016
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/eton-place-dalian-tower-1/249|title = Eton Place Dalian Tower 1 - the Skyscraper Center}}</ref>
|-
|56
| [[Thamrin Nine|Autograph Tower]]
| {{cvt|382.9|m|ft|disp=table|0}}
| 75 (+ 6 below ground)
| [[File:Autograph Tower, Jakarta, ID – July 2022.png|100px]]
| [[Jakarta]]
| {{Flag|Indonesia}}
| 2022
| Tallest building in [[List of tallest buildings in Indonesia|Indonesia]]. Tallest building in the Southern Hemisphere.<ref>{{cite web|url=https://indonesiaexpat.id/business-property/indonesias-tallest-skyscraper-autograph-tower-almost-completed/|title=Indonesia's Tallest Skyscraper Autograph Tower Almost Completed|website=[[Indonesia Expat]]|date=28 January 2022|access-date=31 July 2022}}</ref>
| <ref>{{cite web |title=Autograph Tower |url=https://www.skyscrapercenter.com/building/autograph-tower/39449 |website=The Skyscraper Center}}</ref>
|-
|57
| [[Logan Century Center 1]]
| {{cvt|381.3|m|ft|disp=table|0}}
| 82 (+ 4 below ground)
|
| Nanning
| {{Flag|China}}
| 2018
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/nanning-logan-century-1/10698|title = Nanning Logan Century 1 - the Skyscraper Center}}</ref>
|-
|58
| [[Burj Mohammed Bin Rashid|Burj Mohammed bin Rashid]]
| {{cvt|381.2|m|ft|disp=table|0}}
| 88 (+ 5 below ground)
| [[File:North-East Tower of Qasr Al Hosn.jpg|frameless|100px]]
| [[Abu Dhabi]]
| {{Flag|United Arab Emirates}}
| 2014
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/burj-mohammed-bin-rashid/259|title = Burj Mohammed Bin Rashid - the Skyscraper Center}}</ref>
|- style="background:#dfd;"
|59
| \'\'\'[[Empire State Building]]\'\'\'
| {{cvt|381.0|m|ft|disp=table|0}}
| 102 (+ 1 below ground)
| [[File:Empire State Building cropped.jpg|frameless|100px]]
| New York City
| {{Flag|United States}}
| 1931
|Tallest building in the world from 1931 till 1972; tallest pre-WWII building
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/empire-state-building/261|title = Empire State Building - the Skyscraper Center}}</ref>
|-
|60
| [[Elite Residence]]
| {{cvt|380.5|m|ft|disp=table|0}}
| 87 (+ 4 below ground)
| [[File:Elite Residence-Dubai UAE-Andres Larin.jpg|frameless|100px]]
| Dubai
| {{Flag|United Arab Emirates}}
| 2012
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/elite-residence/263|title = Elite Residence - the Skyscraper Center}}</ref>
|-
|61
| [[Riverview Plaza]]
| {{cvt|376.0|m|ft|disp=table|0}}
| 73 (+ 3 below ground)
| [[File:Wuhan_Riverview_Plaza_A1.jpg|frameless|100px]]
| Wuhan
| rowspan="3" | {{flag|China}}
| 2021
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/riverview-plaza-a1/9591|title = 1 Corporate Avenue - the Skyscraper Center}}</ref>
|-
|62
|Guangdong Business Center
|376
|1,234
|60
|
|Guangzhou
|2024
|
|<ref>{{Cite web |title=Guangdong Business Center - The Skyscraper Center |url=https://www.skyscrapercenter.com/building/guangdong-business-center/30032 |access-date=2024-07-13 |website=www.skyscrapercenter.com}}</ref>
|-
|63
| [[Shenzhen Center|Dabaihui Plaza]]
| {{cvt|375.6|m|ft|disp=table|0}}
| 70 (+ 4 below ground)
| [[File:Dabaihui Plaza in 2021.jpg|frameless|100px]]
| Shenzhen
| 2021
|
|
|-
|64
| [[Central Plaza (Hong Kong)|Central Plaza]]
| {{cvt|373.9|m|ft|disp=table|0}}
| 78 (+ 3 below ground)
| [[File:Hong Kong Convention and Exhibition Centre 200906(cropped).jpg|frameless|100px]]
| Hong Kong
| {{Flag|China}}
| 1992
| Contains the highest church in the world inside a skyscraper
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/central-plaza/277|title = Central Plaza - the Skyscraper Center}}</ref>
|-
|65
| [[Federation Tower|Federation Tower (East Tower)]]
| {{cvt|373.7|m|ft|disp=table|0}}
| 93 (+ 4 below ground)
| [[File:Federation Tower 2022.jpg|frameless|100px]]
| [[Moscow]]
| {{Flag|Russia}}
| 2016
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/federation-tower/118|title = Federation Tower - the Skyscraper Center}}</ref>
|-
|66
| [[Hengfeng Guiyang Center Tower 1]]
| {{cvt|373.5|m|ft|disp=table|0}}
| 77 (+ 5 below ground)
|
| Guiyang
| rowspan="3" | {{Flag|China}}
|
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/hengfeng-guiyang-center-tower-1/26766|title = Hengfeng Guiyang Center Tower 1 - the Skyscraper Center}}</ref>
|-
|67
| [[Dalian International Trade Center]]
| {{cvt|370.2|m|ft|disp=table|0}}
| 86 (+ 7 below ground)
| [[File:Dalian International Trade Center, Aug2018 (cropped).jpg|frameless|100px]]
| Dalian
| 2019
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/dalian-international-trade-center/8980|title = Dalian International Trade Center - the Skyscraper Center}}</ref>
|-
|68
|[[Xujiahui Tower|Shanghai International Trade Center Tower 1]]
|370
|1,214
|75
|
|Shanghai
|2025
|
|<ref>{{Cite web |title=Shanghai International Trade Center Tower 1 - The Skyscraper Center |url=https://www.skyscrapercenter.com/building/shanghai-international-trade-center-tower-1/354 |access-date=2024-07-13 |website=www.skyscrapercenter.com}}</ref>
|-
|69
| [[Address Boulevard]]
| {{cvt|370.0|m|ft|disp=table|0}}
| 73 (+ 3 below ground)
| [[File:The Address Boulevard.jpg|frameless|100px]]
| Dubai
| {{Flag|United Arab Emirates}}
| 2017
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/the-address-boulevard/14606|title=The Address Boulevard - The Skyscraper Center|website=www.skyscrapercenter.com}}</ref>
|-
|70
| [[Haitian Center Tower 2]]
| {{cvt|368.9|m|ft|disp=table|0}}
| 73 (+ 6 below ground)
| [[File:Qingdao Haitian Center in June 2021.jpg|frameless|100px]]
| [[Qingdao]]
| rowspan="2" | {{Flag|China}}
| 2021
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/qingdao-hai-tian-center/15639|title = Qingdao Hai Tian Center - the Skyscraper Center}}</ref>
|-
|71
| [[Golden Eagle Tiandi Tower A]]
| {{cvt|368.1|m|ft|disp=table|0}}
| 77 (+ 4 below ground)
| [[File:南京河西金鹰大楼.jpg|frameless|100px]]
| Nanjing
| 2019
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/golden-eagle-tiandi-tower-a/11463|title=Golden Eagle Tiandi Tower A - The Skyscraper Center|website=www.skyscrapercenter.com}}</ref>
|-
|72
| [[Bank of China Tower (Hong Kong)|Bank of China Tower]]
| {{cvt|367.4|m|ft|disp=table|0}}
| 72 (+ 4 below ground)
| [[File:HK Bank of China Tower 2008 (2).jpg|frameless|100px]]
| Hong Kong
| {{Flag|China}}
| 1990
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/bank-of-china-tower/287|title = Bank of China Tower - the Skyscraper Center}}</ref>
|-
|73
| [[Bank of America Tower (Manhattan)|Bank of America Tower]]
| {{cvt|365.8|m|ft|disp=table|0}}
| 55 (+ 3 below ground)
| [[File:Midtown Manhattan and Times Square district 2015 (2).jpg|frameless|100px]]
| New York City
|{{Flag|United States}}
| 2009
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/bank-of-america-tower/291|title = Bank of America Tower - the Skyscraper Center}}</ref>
|-
|74
|[[Ciel Tower]]
|365.5
|1,199
|81
|
|Dubai
|{{flag|UAE}}
|2024
|Tallest Hotel in the world
|<ref>{{Cite web |title=Ciel Tower - The Skyscraper Center |url=https://www.skyscrapercenter.com/building/ciel-tower/34561 |access-date=2024-07-13 |website=www.skyscrapercenter.com}}</ref>
|-
|75
| [[St. Regis Chicago]]
| {{cvt|362.9|m|ft|disp=table|0}}
| 101 (+ 5 below ground)
| [[File:St.Regis Chicago.jpg|frameless|100px]]
| Chicago
|{{Flag|United States}}
| 2020
| [[List of tallest buildings designed by women|Tallest structure in the world designed by a woman]]
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/st-regis-chicago/17137|title = The St. Regis Chicago - the Skyscraper Center}}</ref>
|-
| rowspan="2" | 76
| [[Almas Tower]]
| rowspan="2" | 360 || rowspan="2" | {{cvt|360|m|ft|disp=number}}
| 68 (+ 5 below ground)
| [[File:Almas Tower.jpg|frameless|100px]]
| Dubai
| {{Flag|United Arab Emirates}}
| 2008
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/almas-tower/298|title=Almas Tower - The Skyscraper Center|website=www.skyscrapercenter.com}}</ref>
|-
| [[Jinan Ping An Finance Center Tower 1]]
| 62 (+ 3 below ground)
|
| [[Jinan]]
| rowspan="4" | {{Flag|China}}
| 2023
|
| <ref>{{ctbuh | id = 32086 | title = Ping An Finance Center Tower 1}}</ref>
|-
|78
|Huiyun Center
|359.2
|1,178
|80
|
|Shenzhen
|2023
|
|<ref>{{Cite web |title=Huiyun Center - The Skyscraper Center |url=https://www.skyscrapercenter.com/building/huiyun-center/29371 |access-date=2024-07-13 |website=www.skyscrapercenter.com}}</ref>
|-
|79
| [[Hanking Center]]
| {{cvt|358.9|m|ft|disp=table|0}}
| 65 (+ 5 below ground)
| [[File:Hanking Center2021.jpg|frameless|100px]]
| Shenzhen
| 2018
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/hanking-center/15741|title = Hanking Center - the Skyscraper Center}}</ref>
|-
|80
| [[Greenland Group Suzhou Center]]
| {{cvt|358.0|m|ft|disp=table|0}}
| 77 (+ 3 below ground)
|
| Suzhou
| 2024
|
| <ref>{{cite web |url= http://skyscrapercenter.com/building/greenland-group-suzhou-center/12572|title= Greenland Group Suzhou Center|access-date= 21 October 2014|work= The Skyscraper Center|publisher= [[Council on Tall Buildings and Urban Habitat]]}}</ref><ref>{{Cite web|url=https://www.skyscrapercenter.com/building/greenland-group-suzhou-center/12572|title = Greenland Group Suzhou Center - the Skyscraper Center}}</ref>
|-
|81
| [[Gevora Hotel]]
| {{cvt|356.3|m|ft|disp=table|0}}
| 75 (+ 2 below ground)
| [[File:Gevora Hotel.jpg|frameless|100px]]
| Dubai
| {{Flag|United Arab Emirates}}
| 2017
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/gevora-hotel/348|title = Gevora Hotel - the Skyscraper Center}}</ref>
|-
| rowspan="3" | 82
| Galaxy World Tower 1
| rowspan="2" | 356.0 || rowspan="2" | {{cvt|356|m|ft|disp=number}}
| rowspan="2" |71 (+ 5 below ground)
| rowspan="2" |
| rowspan="2" |Shenzhen
| rowspan="2" |{{Flag|China}}
| rowspan="2" |2023
| rowspan="2" |
| rowspan="2" | <ref>{{ctbuh | id = 27941 | title = Galaxy Tower 1}}</ref><ref>{{ctbuh | id = 27942 | title = Galaxy Tower 2}}</ref>
|-
| {{left}} Galaxy World Tower 2
|-
| {{left}} [[Il Primo Dubai|Il Primo Tower]]
| {{cvt|356.0|m|ft|disp=table|0}}
| 79
| [[File:Il Primo Tower Dubai.jpg|frameless|100px]]
| rowspan=4 |Dubai
| rowspan=4 |{{Flag|United Arab Emirates}}
| 2022
|
| <ref>{{ctbuh|id=26116|title=Il Primo Tower}}</ref>
|-
| rowspan=2 |85
| [[JW Marriott Marquis Dubai|JW Marriott Marquis Dubai Tower&amp;nbsp;1]]
| rowspan=2 | 355.4 || rowspan=2 | {{cvt|355.4|m|ft|disp=number|0}}
| rowspan=2 | 82 (+ 2 below ground)
| rowspan=2 | [[File:JW Marriott Marquis Dubai2.jpg|frameless|100px]]
|2012
|
| rowspan=2 | <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/jw-marriott-marquis-hotel-dubai-tower-1/237|title = JW Marriott Marquis Hotel Dubai Tower 1 - the Skyscraper Center}}</ref><ref>{{Cite web|url=https://www.skyscrapercenter.com/building/jw-marriott-marquis-hotel-dubai-tower-2/238|title = JW Marriott Marquis Hotel Dubai Tower 2 - the Skyscraper Center}}</ref>
|-
| {{left}} [[JW Marriott Marquis Dubai|JW Marriott Marquis Dubai Tower&amp;nbsp;2]]
| 2013
|-
| 87
| [[Emirates Office Tower]]
| {{cvt|354.6|m|ft|disp=table|0}}
| 54
|
| 2000
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/emirates-tower-one/311|title = Emirates Tower One - the Skyscraper Center}}</ref>
|-
| rowspan=2 |88
| [[Raffles City Chongqing|Raffles City Chongqing T3N]]
| rowspan=2 | 354.5 || rowspan=2 | {{cvt|354.5|m|ft|disp=number}}
| 79 (+ 3 below ground)
| rowspan=2 |[[File:Raffles City Chongqing from Yangtze River(cropped).jpg|frameless|100px]]
| rowspan=2 |Chongqing
| rowspan=2 |{{Flag|China}}
| rowspan=2 |2019
| rowspan=2 |
| rowspan=2 | <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/raffles-city-chongqing-t3n/13610|title = Raffles City Chongqing T3N - the Skyscraper Center}}</ref><ref>{{Cite web|url=https://www.skyscrapercenter.com/building/raffles-city-chongqing-t4n/13611|title = Raffles City Chongqing T4N - the Skyscraper Center}}</ref>
|-
| {{left}} [[Raffles City Chongqing|Raffles City Chongqing T4N]]
| 74 (+ 3 below ground)
|-
|90
| [[OKO|OKO&amp;nbsp;– South Tower]]
| {{cvt|354.2|m|ft|disp=table|0}}
| 90 (+ 2 below ground)
| [[File:Oko towers1.jpg|frameless|100px]]
| Moscow
| {{Flag|Russia}}
| 2015
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/oko-residential-tower/363|title = OKO - Residential Tower - the Skyscraper Center}}</ref>
|-
| rowspan="2" |91
| [[The Marina Torch]]
| {{cvt|352.0|m|ft|disp=table|0}}
| 86 (+ 4 below ground)
| [[File:The Marina Torch.jpg|frameless|60px]]
| Dubai
| {{Flag|United Arab Emirates}}
| 2011
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/the-torch/344|title = The Torch - the Skyscraper Center}}</ref>
|-
|[[Central Bank of the Republic of Turkey]]
|352
|1,155
|59
|
|Istanbul
|{{Flag|Turkey}}
|2024
|
|
|-
|93
| [[Forum 66|Forum&amp;nbsp;66 Tower&amp;nbsp;1]]
| {{cvt|350.6|m|ft|disp=table|0}}
| 68 (+ 4 below ground)
| [[File:Forum 66, Shenyang, Oct2014.png|frameless|100px]]
| [[Shenyang]]
| rowspan="4" |{{Flag|China}}
| 2015
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/forum-66-tower-1/414|title = Forum 66 Tower 1 - the Skyscraper Center}}</ref>
|-
|94
| [[The Pinnacle (Guangzhou)|The Pinnacle]]
| {{cvt|350.3|m|ft|disp=table|0}}
| 60 (+ 6 below ground)
| [[File:花城汇 音乐喷泉 (2013-10-26) - panoramio Pinnacle(cropped).jpg|frameless|100px]]
| Guangzhou
| 2012
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/the-pinnacle/306|title = The Pinnacle - the Skyscraper Center}}</ref>
|-
|95
| [[Xi'an Glory International Financial Center]]
| {{cvt|350.0|m|ft|disp=table|0}}
| 75 (+ 4 below ground)
| [[File:20230925 Xi'an Financial Center.jpg|frameless|100px]]
| [[Xi'an]]
| 2021
|
| <ref>{{Cite web|url=https://www.skyscrapercenter.com/building/gloryxian-international-financial-center/18932|title = Glory・Xi'an International Financial Center - the Skyscraper Center}}</ref>
|}
'''

loader = ptr.MediaWikiTableTextLoader(tallest_buildings)
for table_data in loader.load():
    df = table_data.as_dataframe()
    print(df)

# import pytablereader as ptr
# import pandas as pd

# loader = ptr.MediaWikiTableTextLoader(confederation)
# for table_data in loader.load():
#     # print(table_data)
#     # Get the headers from the table_data
#     headers = table_data.headers
#     # print(table_data.rows)
#     # Create a DataFrame with the rows and all headers
#     df = pd.DataFrame(table_data.rows, columns=headers)

#     df.drop(columns=['Image', 'Comments', 'Refs'], inplace=True)
#     print(df)
#     # print(df)
#     # Save the DataFrame to a CSV file
#     df.to_csv('tallest_buildings_2.csv', index=False)
    
#     print("DataFrame has been saved to 'tallest_buildings_2.csv'")


'''
import pandas as pd
import io, csv, re

# Function to pre-process the data
def preprocess_mediawiki_table(data):
    # Remove the opening and closing table tags
    data = re.sub(r'{\|.*?\n', '', data)
    data = re.sub(r'\|}', '', data)
    
    # Replace MediaWiki formatting with CSV-compatible format
    data = re.sub(r'!\s*scope="col"\s*\|', '', data)
    data = re.sub(r'!\s*scope="row"\s*\|', '', data)
    data = re.sub(r'\|-', '', data)
    data = re.sub(r'\[\[(.*?)\]\]', r'\1', data)
    
    # Remove any remaining '|' at the beginning of lines
    data = re.sub(r'^\|', '', data, flags=re.MULTILINE)
    
    # Split the data into lines and remove empty lines
    lines = [line.strip() for line in data.split('\n') if line.strip()]
    
    # Enclose each line with double quotes
    lines = [f'"{line}"' for line in lines]

    # Join the lines back together with commas
    return '\n'.join([','.join(line.split('|')) for line in lines])

# Pre-process the data
preprocessed_data = preprocess_mediawiki_table(tallest_buildings)
print(preprocessed_data)

# Create a DataFrame from the pre-processed data
df = pd.read_csv(io.StringIO(preprocessed_data))

# Display the DataFrame
print(df)
'''
