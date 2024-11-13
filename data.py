class Data:
    def __init__(self, database = None, input='', output=''):
        self.setDatabase(database)
        self.setInput(input)
        self.setOutput(output)
    def setDatabase(self, value):
        self.__database = value
    def setInput(self, value):
        self.__input = value
    def setOutput(self, value):
        self.__output = value
    def getDatabase(self): return self.__database
    def getInput(self): return self.__input
    def getOutput(self): return self.__output

    def readFile(self, filename):
        self.setInput(filename)
        self.read()
    
    def writeFile(self, filename):
        self.setOutput(filename)
        self.write()
    
    def read(self): pass
    def write(self): pass