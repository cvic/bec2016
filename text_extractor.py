#!/usr/bin/python
# -*- coding: utf-8 -*-

import unicodedata
import os
from os.path import basename
import codecs
import textract 
import sys
from os import listdir
from os.path import isfile, join
import logging
import argparse

logging.basicConfig(filename='extractor.log', level=logging.DEBUG)

parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser(description='Process tables stuck in pdf files.')

parser.add_argument("folder", help="A magic folder that contains the pdfs")
args = parser.parse_args()

# ¯\_(.)_/¯ 
# http://stackoverflow.com/questions/21129020/how-to-fix-unicodedecodeerror-ascii-codec-cant-decode-byte
reload(sys)  
sys.setdefaultencoding('utf8')

def fix_path(file):
  return pdf_folder + file

def extract_text(file):
  utf8_text = textract.process(file)
  logging.debug('Extracting text from %s' % file)
  print "Processing ", os.path.splitext(os.path.basename(file))[0]
  utf8_txt_file = utf8_txt_folder + "utf8_" + os.path.splitext(os.path.basename(file))[0] + ".txt"
  with codecs.open(utf8_txt_file,'w', encoding='utf-8') as f8:
    f8.write(utf8_text)

  file_stream = codecs.open(utf8_txt_file, 'r', 'utf-8').read()
  output_txt = unicodedata.normalize('NFD', file_stream).encode('ascii', 'ignore')
  output_txt = output_txt.replace("Page 1/1",'')

  txt_file = txt_folder + os.path.splitext(os.path.basename(file))[0] + ".txt"
  with codecs.open(txt_file,'w', encoding='utf-8') as f:
    f.write(output_txt)

if __name__ == "__main__":
  pdf_folder = args.folder
  utf8_txt_folder = "utf8_texts/"
  txt_folder = "texts/"
  
  if not os.path.exists(utf8_txt_folder):
    os.makedirs(utf8_txt_folder)

  if not os.path.exists(txt_folder):
    os.makedirs(txt_folder)

  pdfs = [f for f in listdir(pdf_folder) if isfile(join(pdf_folder, f))]

  #stupid
  fxd_dis = map(fix_path, pdfs)

  map(extract_text, fxd_dis)

  texts = [f for f in listdir(txt_folder) if isfile(join(txt_folder, f))] 
  utf8_texts = [f for f in listdir(utf8_txt_folder) if isfile(join(utf8_txt_folder, f))]

  print "{} pdfs, {} texts, {} utf8 texts".format( len(pdfs), len(texts), len(utf8_texts))
