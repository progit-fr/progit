#!/usr/bin/python
import logging
logging.basicConfig(level=logging.WARNING)

from string import *
import shutil

for line in open('mapping.txt','r'):
    split_line= split(line,'#')
    values= split(split_line[0])
    if len(values)>1:
        logging.debug(values)
        shutil.copyfile("progit%s.svg" % values[0],"%s.svg" % values[1])
