#Justin Trebour
#COP2002.0M1
#04/17/2023
#Project 7 - Files and Classes
#This program should allow for the converting of data from one format (CSV) to another (JSON)


class CSVtoJSON:

    def __init__ (self, headings, ID, inputFileName, outputFileName="Project7Output - Test File.txt"):
        self.headings = headings
        self.ID = ID
        self.linesFromFile = linesFromFile
        self.outputFileName = outputFileName
        self.inputFileName = inputFileName

    def createKeyValuePair(self, key, value):
        result ="\"" + key + "\":\"" + value+"\""

        return result



def main():

    fileName = input("Enter the filename:  ")


# headings=[]
# ID = 1
# inputFileName = "Input1.txt"

# example1=CSVtoJSON(headings, ID, inputFileName)
# example2=CSVtoJSON(headings, ID, inputFileName, "Output.txt")


# keyValuePairExample = example1.createKeyValuePair("First Name", "James")
# print(keyValuePairExample)





if (__name__ == "__main__"):
    main()