import os

class SintaxAnalyzer:
    def __init__(self, nameFileCode):
        self.code = nameFileCode
        self.nameFileTokens = 'analyzed/' + nameFileCode + '/' + nameFileCode + '-tokens.txt'
        self.grammarFile = "resources/fiboGrammar.txt"
    
    def setTokens(self):
        tokensFile = open(self.nameFileTokens)
        self.tokens = tokensFile.read()

    def analyzeTokens(self):
        os.system('slr ' + self.grammarFile + ' "' + self.tokens + '" > analyzed/' + self.code + '/' + self.code + '-sintaxAnalysis.txt')
