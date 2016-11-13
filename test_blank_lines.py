import os
import glob
from os import listdir
from os.path import isfile, join
from collections import Counter

def fix_path(file):
  return txt_folder + file

def blank_lines(file):
  with open(file) as f:
         return sum(not line.strip() for line in f)

if __name__ == "__main__":
  NO_OK_LINES = 9
  txt_folder = "texts/"
  
  txt_files = [f for f in listdir(txt_folder) if isfile(join(txt_folder, f))]
  print txt_files

  temp = map(fix_path, txt_files)

  blank_stuff = map(blank_lines, temp)
  print blank_stuff

  for f in temp:
    arr = []
    with open(f) as f_:
      arr = f_.readlines()
    if(blank_lines(f) > NO_OK_LINES):
      print f, Counter(arr)['\n']+1, blank_lines(f)
