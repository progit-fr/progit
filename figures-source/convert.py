#!/usr/bin/python
import logging
logging.basicConfig(level=logging.WARNING)

from string import *
import shutil
from graffle2svg.main import GraffleParser

def transform_3_3(svg_doc):
    pass

def transform_3_4(svg_doc):
    pass

def transform_3_11(svg_doc):
    pass

def transform_3_12(svg_doc):
    pass

'''
missing 3.18 3.19 3.20 3.21 3.27 3.28 3.29 3.30 5.11 5.15 7.2 7.3 9.2
'''
conversions = {
    0	:[{'figure':'6.1'}],
    1	:[{'figure':'5.4'}],
    2	:[{'figure':'5.5'}],
    3	:[{'figure':'5.6'}],
    4	:[{'figure':'5.7'}],
    5	:[{'figure':'5.8'}],
    6	:[{'figure':'5.9'}],
    7	:[{'figure':'5.10'}],
    8	:[{'figure':'5.12'}],
    9	:[{'figure':'5.13'}],
    10	:[{'figure':'5.14'}],
    11	:[{'figure':'5.16'}],
    12	:[{'figure':'5.17'}],
    13	:[{'figure':'5.18'}],
    14	:[{'figure':'5.2'}],
    15	:[{'figure':'5.1'}],
    16	:[{'figure':'5.3'}],
    17	:[{'figure':'1.1'}],
    18	:[{'figure':'1.2'}],
    19	:[{'figure':'1.3'}],
    20	:[{'figure':'fig20'}], 
    21	:[{'figure':'3.22'}],
    22	:[{'figure':'3.23'}],
    23	:[{'figure':'3.24'}],
    24	:[{'figure':'3.25'}],
    25	:[{'figure':'3.26'}],
    26	:[{'figure':'3.36'}],
    27	:[{'figure':'3.37'}],
    28	:[{'figure':'3.38'}],
    29	:[{'figure':'3.39'}],
    30	:[{'figure':'figure30'}],
    31	:[{'figure':'5.19'}],
    32	:[{'figure':'5.20'}],
    33	:[{'figure':'5.21'}],
    34	:[{'figure':'5.22'}],
    35	:[{'figure':'5.23'}],
    36	:[{'figure':'5.24'}],
    37	:[{'figure':'5.25'}],
    38	:[{'figure':'5.26'}],
    39	:[{'figure':'5.27'}],
    40	:[{'figure':'3.10'},
          {'figure':'3.11','transform':transform_3_11},
          {'figure':'3.12','transform':transform_3_12}],
    41	:[{'figure':'figure41'}],
    42	:[{'figure':'figure42'}],
    43	:[{'figure':'figure43'}],
    44	:[{'figure':'figure44'}],
    45	:[{'figure':'figure45'}],
    46	:[{'figure':'3.31'}],
    47	:[{'figure':'3.32'}],
    48	:[{'figure':'3.33'}],
    49	:[{'figure':'3.34'}],
    50	:[{'figure':'3.35'}],
    51	:[{'figure':'figure51'}],
    52	:[{'figure':'3.13'}],
    53	:[{'figure':'3.14'}],
    54	:[{'figure':'3.15'}],
    55	:[{'figure':'3.16'}],
    56	:[{'figure':'3.17'}],
    57	:[{'figure':'1.4','boundingbox':((0,0),(756,276)) },
          {'figure':'1.5','boundingbox':((0,257),(756,553))}],
    58	:[{'figure':'1.6'}],
    59	:[{'figure':'2.1'}],
    60  :[{'figure':'figure60'}],
    61  :[{'figure':'figure61'}],
    62	:[{'figure':'9.1'}],
    63	:[{'figure':'figure63'}],  
    64	:[{'figure':'9.3'}],
    65	:[{'figure':'9.4'}],
    66	:[{'figure':'3.1'}],
    67	:[{'figure':'3.2'}],
    68	:[{'figure':'3.3','transform':transform_3_3}], 
    69  :[{'figure':'figure69'}],
    70  :[{'figure':'figure70'}],
    71  :[{'figure':'figure71'}],
    72  :[{'figure':'figure72'}],
    73  :[{'figure':'figure73'}],
    74  :[{'figure':'figure74'}],
    75  :[{'figure':'figure75'}],
    76  :[{'figure':'figure76'}],
    77	:[{'figure':'3.6'},{'figure':'3.4','transform':transform_3_4}],
    78	:[{'figure':'3.5'}],
    79	:[{'figure':'3.7'}],
    80	:[{'figure':'3.8'}],
    81	:[{'figure':'3.9'}]
    }

gp =GraffleParser()
#gp.walkGraffle(open('progit.graffle','r').read())
gp.walkGraffleFile('progit.graffle')
for source_index in conversions.keys():
    if  conversions[source_index] is not None:
        for target in conversions[source_index]:
            gp.extractPage(page=source_index,background=False,bounding_box=target.get('boundingbox',None))
            f = open(target["figure"]+".svg","w")
            f.write(gp.svg)
            f.close()
