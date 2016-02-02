# CSV Merger
# Joenabie Gamao
# 01/28/2016
# References:  http://www.tutorialspoint.com/python/
import csv,os


class Student:

    def __init__(self, studentID):
        self.id=studentID
        self.actions = []

    def getID(self):
        return self.id

    def setID(self,studentID):
        self.id = studentID

    def getActionCount(self):
        return len(self.actions)

    def addActions(self,offset, behavior,affect):
        self.actions.append([offset,behavior,affect])

    def getActions(self):
        for i in self.actions:
            return i
    def getEquiv(self,argument):
        switcher = {
        "offsets": 0,
        "behaviors": 1,
        "affects": 2,
        }
        return switcher.get(argument, "nothing")

    def getAction(self,action):
        action.lower()
        num = self.getEquiv(action)
        strx = ""
        for i in self.actions:
            strx += i[num] + ", "
        return strx

    def __str__(self):
        strx = ""
        strx += self.id
        strx += "\n"
        #strx += "\n\nCount: " + str(self.getActionCount())

        return strx




directory = raw_input("Enter Directory Path: ")
directory.lower()

print directory


theList = list()
theDict = dict()
with open('files/sample.csv', 'rb') as ifile:
    reader = csv.reader(ifile, delimiter=',')
    for row in reader:
        theList.append(row)


mstudents = list() # ARRAY OF STUDENT CLASSES

for i in range(len(theList)):
    if i == 0:
        continue

    studentID = theList[i][0]
    if studentID not in theDict: # new entry
        theDict[studentID] = 1
        newStud = Student(studentID)
        newStud.addActions(theList[i][1],theList[i][2],theList[i][3])
        mstudents.append(newStud)
    else: #just update old student class
        for x in mstudents:
            if studentID == x.getID():
                x.addActions(theList[i][1],theList[i][2],theList[i][3])



studentIDs=[]
theDict.keys().sort()
for i in theDict.keys():
    studentIDs.append(i)

studentIDs.sort()
for i in studentIDs:
    print i + "\n"
    for x in mstudents:
        if i == x.getID():
            print x.getAction("offsets")
            print x.getAction("behaviors")
            print x.getAction("affects")
