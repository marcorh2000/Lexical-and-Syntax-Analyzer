from analizadorLexico import LexicalAnalyzer
from analizadorSintactico import SintaxAnalyzer
import sys


code = sys.argv[1]
l = LexicalAnalyzer(code)
s = SintaxAnalyzer(code)

l.getLexicalAnalysis()
s.setTokens()
s.analyzeTokens()
