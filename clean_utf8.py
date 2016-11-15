#!/usr/bin/python
# -*- coding: utf-8 -*-

import unicodedata
import os
from os.path import basename
import codecs
import sys
from os import listdir
from os.path import isfile, join
import logging

UTF8_TXT_FOLDER = "sok_utf8_txt_files/"
CLEAN_TXT_FOLDER = "new_texts/"

reload(sys)  
sys.setdefaultencoding('utf8')

def fix_path(file):
  return UTF8_TXT_FOLDER + file

def kiss_my_ascii(utf8_file):
  logging.debug('Extracting ascii from %s' % file)

  file_stream = codecs.open(utf8_file, 'r', 'utf-8').read()
  output_txt = unicodedata.normalize('NFD', file_stream).encode('ascii', 'ignore')
  #hey, meatball, some pdfs have 2 pages! Use re.sub instead
  output_txt = output_txt.replace("Page 1/1",'')

  txt_file = CLEAN_TXT_FOLDER + os.path.splitext(os.path.basename(utf8_file))[0] + ".txt_"
  with codecs.open(txt_file,'w', encoding='utf-8') as f:
    f.write(output_txt)

def main():
  if not os.path.exists(UTF8_TXT_FOLDER):
    print "No UTF8 txt folder :-("
    sys.exit(0) 

  if not os.path.exists(CLEAN_TXT_FOLDER):
    os.makedirs(CLEAN_TXT_FOLDER)

  utf8_texts = [f for f in listdir(UTF8_TXT_FOLDER) if isfile(join(UTF8_TXT_FOLDER, f))]

  fxd_dis = map(fix_path, utf8_texts)

  for f in fxd_dis:
    print f
    kiss_my_ascii(f)

if __name__ == "__main__":
  main() 
