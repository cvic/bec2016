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

def file2array(file):
  array = []
  with open(file) as f:
    array = f.readlines()
  return array

def check_file(f):
  f2a = file2array(f)
  nume = f2a.index("NUMELE SI PRENUMELE\n")
  judet_domiciliu = f2a.index("JUDET DOMICILIU\n")
  localitate_domiciliu = f2a.index("LOCALITATE DOMICILIU\n")
  ocupatia = f2a.index("OCUPATIA\n")
  profesia = f2a.index("PROFESIA\n")
  i1 = judet_domiciliu - nume
  i2 = localitate_domiciliu - judet_domiciliu
  i3 = ocupatia - localitate_domiciliu
  i4 = profesia - ocupatia
  if ( i1 == i2 and i2 == i3 and i3 == i4 ):
    return f, "OK"
  else:
    return f, "NOK"

if __name__ == "__main__":
  NO_OK_LINES = 9
  txt_folder = "texts/"
  
  txt_files = [f for f in listdir(txt_folder) if isfile(join(txt_folder, f))]

  temp = map(fix_path, txt_files)

  blank_stuff = map(blank_lines, temp)

#  print file2array("texts/centralizator_BEJ_42_58_CD.txt")

## centralizator_BEJ_13_16_CD.txt
## centralizator_BEJ_17_111_CD.txt  - fucked
## centralizator_BEJ_23_37_S.txt - OK
  print check_file("texts/centralizator_BEJ_17_111_CD.txt")
  print check_file("texts/centralizator_BEJ_17_111_S.txt")
  print check_file("texts/centralizator_BEJ_13_16_CD.txt")
  print check_file("texts/centralizator_BEJ_42_58_CD.txt")

  for m in  map(check_file, temp):
    print m

"""
  for f in temp:
    arr = []
    with open(f) as f_:
      arr = f_.readlines()
    if(blank_lines(f) > NO_OK_LINES):
      print f, Counter(arr)['\n']+1, blank_lines(f)
"""
