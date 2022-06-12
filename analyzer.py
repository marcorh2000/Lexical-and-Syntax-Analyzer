from LexicalAnalyzer import LexicalAnalyzer
from SintaxAnalyzer import SintaxAnalyzer
import sys
import os
import shutil

code = sys.argv[1]

file_path = 'analyzed/' + code

if os.path.exists(file_path):
    shutil.rmtree(file_path)

os.mkdir(file_path, 0o777)

l = LexicalAnalyzer(code)
s = SintaxAnalyzer(code)

l.getLexicalAnalysis()
s.setTokens()
s.analyzeTokens()
