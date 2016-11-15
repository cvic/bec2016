import os
import sys
import glob
import numpy
from os import listdir
from os.path import isfile, join
from collections import Counter

TXT_FOLDER = "text_files/"
CSV_FOLDER = "csv_files/"
NOK_CSV_FOLDER = "nok_csv_files/"

def filter_(str):
  return str.replace("\n","")

def fix_path(file):
  return TXT_FOLDER + file

def blank_lines(file):
  with open(file) as f:
         return sum(not line.strip() for line in f)

def file2array(file):
  array = []
  with open(file) as f:
    array = f.readlines()
  return array

def ok_file(f):
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
    return True
  else:
    return False

def header_data(f):
  f2a = file2array(f)
  circumscriptia = f2a[0].replace('Circumscriptia nr.','').replace(' - ', '_').rstrip()
  return circumscriptia + "_" + f2a[2]  

def write_csv(f):
  f2a = file2array(f)
  the_name =  os.path.splitext(os.path.basename(f))[0]
  nume_candidat = f2a.index("NUMELE SI PRENUMELE\n")
  judet_domiciliu = f2a.index("JUDET DOMICILIU\n")
  localitate_domiciliu = f2a.index("LOCALITATE DOMICILIU\n")
  ocupatia = f2a.index("OCUPATIA\n")
  profesia = f2a.index("PROFESIA\n")
  circumscriptia = f2a[0].replace('Circumscriptia nr.','').replace(' - ', '_').rstrip()
  partid = f2a[2].split(' - ')[0]
  cd_s = f2a[2].split(' - ')[1]
  print ok_file(f)
  
  print "-----------------------"
 
  magic_len = len(f2a[ocupatia:profesia-1]) - 1
 
  a =  map(filter_, f2a[nume_candidat:judet_domiciliu-1])
  b = map(filter_, f2a[judet_domiciliu:localitate_domiciliu-1])
  c = map(filter_, f2a[localitate_domiciliu:ocupatia-1])
  d = map(filter_, f2a[ocupatia:profesia-1])
  circumscription_header = ["CIRCUMSCRIPTIA"]
  circumscription_array_fragment = [circumscriptia] * magic_len 
  circumscription_array =  numpy.concatenate((circumscription_header, circumscription_array_fragment), axis = 0 )

  party_header = ["PARTID"]
  party_array_fragment = [partid] * magic_len 
  party_array =  numpy.concatenate((party_header, party_array_fragment), axis = 0 )

  arr = numpy.array([a, b, c, d, party_array, circumscription_array])
  csv_data =  arr.transpose()
  # https://www.getdatajoy.com/examples/python-data-analysis/read---write-csv-file-with-numpy
  if(ok_file(f)):
    numpy.savetxt(
      CSV_FOLDER + the_name + '.csv',           # file name
      csv_data,                # array to save
      fmt='%s',             # formatting, 2 digits in this case
      delimiter=',',          # column delimiter
      newline='\n',           # new line character
      comments='#'          # character to use for comments
      # header='' + f           # file header
    )
  else:
     numpy.savetxt(
      NOK_CSV_FOLDER + the_name + '.csv',           # file name
      csv_data,                # array to save
      fmt='%s',             # formatting, 2 digits in this case
      delimiter=',',          # column delimiter
      newline='\n',           # new line character
      comments='#'          # character to use for comments
      # header='' + f           # file header
    )

def main():
  if not os.path.exists(CSV_FOLDER):
    os.makedirs(CSV_FOLDER)

  if not os.path.exists(NOK_CSV_FOLDER):
    os.makedirs(NOK_CSV_FOLDER)

  txt_files = [f for f in listdir(TXT_FOLDER) if isfile(join(TXT_FOLDER, f))]

  #blank_stuff = map(blank_lines, temp)
  fixed = map(fix_path, txt_files)

  ok_files = []
  nok_files = []

  for f in fixed: 
    the_name =  os.path.splitext(os.path.basename(f))[0] 
#   print f, ok_file(f), header_data(f)
    if(ok_file(f)):
      ok_files.append(f)
    else:
       nok_files.append(f)
  
  print ok_files     
  print nok_files     
  print len(ok_files)
  print len(nok_files)

  for nokf in nok_files:
     write_csv(nokf)
  
  for okf in ok_files:
     write_csv(okf)

#  checked =  map(ok_file, fixed)
#  print checked

# centralizator_BEJ_13_16_CD.txt - OK
# centralizator_BEJ_17_111_CD.txt  - fucked
# centralizator_BEJ_23_37_S.txt - OK
# print file2array("texts/centralizator_BEJ_42_58_CD.txt")
# print ok_file("texts/centralizator_BEJ_17_111_CD.txt")
# print ok_file("texts/centralizator_BEJ_17_111_S.txt")
# print ok_file("texts/centralizator_BEJ_13_16_CD.txt")
# print ok_file("texts/centralizator_BEJ_42_58_CD.txt")
# slice("texts/centralizator_BEJ_42_58_CD.txt")
# slice("texts/centralizator_BEJ_17_111_S.txt")
# slice("texts/centralizator_BEJ_13_111_CD.txt")

if __name__ == "__main__":
  main()
