import os
import sys
from os import listdir
from os.path import isfile, join
from subprocess import call
import logging

logging.basicConfig(filename='java_stuff.log',level=logging.DEBUG, format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s', datefmt="%Y-%m-%d %H:%M:%S")

# ok, but not ok
SOK_FOLDER = "/home/vic/playground/bec2016/sok_utf8_txt_files/"
PDF_FOLDER = "/home/vic/playground/bec2016/test_pdfs/"
TXT_FOLDER = "/home/vic/playground/bec2016/text_files/"

def fix_path(file):
  return TXT_FOLDER + file

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

# http://stackoverflow.com/questions/26233387/extract-pdf-text-by-columns
def pdfbox_foo(f):
  filename = os.path.splitext(os.path.basename(f))[0]
  logging.debug('Extracting text from = %s' % filename) 
  call(["java", "-jar", "pdfbox-app-2.0.3.jar", "ExtractText", PDF_FOLDER + filename + ".pdf", SOK_FOLDER + filename + ".txt" ])

def main(): 
  if not os.path.isdir(PDF_FOLDER):
    print "No pdf folder. Exiting!"
    sys.exit(0)

  if not os.path.isdir(TXT_FOLDER):
    print "No txt folder either, pfff..."
    sys.exit(0)

  if not os.path.exists("pdfbox-app-2.0.3.jar"):
    print "pdfbox jar not found, bye!"
    sys.exit(0)

  if not os.path.exists(SOK_FOLDER):
    os.makedirs(SOK_FOLDER)

  txt_files = [f for f in listdir(TXT_FOLDER) if isfile(join(TXT_FOLDER, f))]

  fixed = map(fix_path, txt_files)
 
  for f in fixed:
    if(not ok_file(f)):
      pdfbox_foo(f)
 
if __name__ == "__main__":
  main()
