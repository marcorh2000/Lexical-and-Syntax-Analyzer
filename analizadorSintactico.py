import os

class SintaxAnalyzer:
    def __init__(self, nameFileCode):
        self.nameFileTokens = nameFileCode + '-tokens.txt'
        self.grammarFile = "gramaticaFibo.txt"
    
    def setTokens(self):
        tokensFile = open(self.nameFileTokens)
        self.tokens = tokensFile.read()

    def analyzeTokens(self):
        os.system('slr ' + self.grammarFile + ' "' + self.tokens + '"')

#s = SintaxAnalyzer('testCode')
#s.setTokens()
#s.analyzeTokens()
