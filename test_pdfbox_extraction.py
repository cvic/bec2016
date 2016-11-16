#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from os.path import basename
import sys
from os import listdir
from os.path import isfile, join

import logging
import argparse
import numpy

logging.basicConfig(filename='java_stuff.log',level=logging.DEBUG, format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s', datefmt="%Y-%m-%d %H:%M:%S")

parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser(description='Test text files extracted by PDFbox.')

parser.add_argument("folder", help="A magic folder that contains the text files")
args = parser.parse_args()

txt_folder = args.folder

def fix_path(file):
  return txt_folder + file

def min_string(f):
  file = open(f, 'rb')
  table = [row.strip().split('\t') for row in file]
  for index, line in enumerate(table):
    temp = ''.join([str(x) for x in line])
    if (len(temp) < 40):
      print index, temp, len(temp)

def get_county(f):
  file = open(f, 'rb')
  table = [row.strip().split('\t') for row in file]
  temp = ''.join([str(x) for x in table[0]])
  return temp.split(" - ")[1]

if __name__ == "__main__":

  texts = [f for f in listdir(txt_folder) if isfile(join(txt_folder, f))]

  #stupid
  fxd_dis = map(fix_path, texts)
  #print fxd_dis

  for f in fxd_dis:
    print f, 
    print min_string(f)
