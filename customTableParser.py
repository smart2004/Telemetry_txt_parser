import datetime
import json

class TableParser:
    
    def __init__(self):
        self.config_name = "temetryParserConfig.json"
        self.headers = list()
        self.rawrows = list()
        self.parsedRows = list()
        self.config = self.loadConfig()
        print("my Config ", self.config)


    def loadConfig(self):
        with open(self.config_name, "r", encoding='utf-8') as configFile:
            config = json.loads(configFile.read())
            return config 


    def readAllTableTelemFile(self):
        with open(self.config['input_file'], "r", encoding='cp1251') as inputfile:
            self.rawrows = inputfile.readlines()
            print(f"rows readed: {len(self.rawrows)}")
            print(self.rawrows[0])
            print(self.rawrows[1])


    def parseTelemHeaders(self):
        if len(self.rawrows):
            headerLine =  self.rawrows[0]
            headerLine = str(headerLine).replace(self.config["row_delimeter"], "")
            headerparts = headerLine.split(self.config["cell_delimeter"])
            for part in headerparts:
                #print(type(part), part)
                self.headers.append(part)
            print("headers: ", self.headers, sep="\n")


    def parseTelemCells(self):
        #for i in range(1, len(self.rawrows)):
        print("Row iterator\n")
        for i in range(1, 5):
            arRow = str(self.rawrows[i]).split(self.config["cell_delimeter"])
            rowdict = dict(zip(self.headers, arRow))
            print(f"{rowdict=}", )


if __name__ == "__main__":
    tp = TableParser()
    tp.readAllTableTelemFile()
    tp.parseTelemHeaders()
    tp.parseTelemCells()