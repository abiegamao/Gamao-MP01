# CSV Merger
# Joenabie Gamao
# 01/28/2016

import csv


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
            for x in i:
                return x
    def getOffsets(self):
        strx = ""
        for i in self.actions:
            strx += i[0] + ", "
        return strx

    def getBehaviors(self):
        strx = ""
        for i in self.actions:
            strx += i[1] + ", "
        return strx

    def getAffects(self):
        strx = ""
        for i in self.actions:
            strx += i[2] + ", "
        return strx


    def __str__(self):
        strx = ""
        strx += self.id
        strx += "\n"
        #strx += "\n\nCount: " + str(self.getActionCount())

        return strx




print "hi"
theList = list()
theDict = dict()
with open('files/sample.csv', 'rb') as ifile:
    reader = csv.reader(ifile, delimiter=',')
    for row in reader:
        theList.append(row)






# COUNTER , SET THE UNIQUE IDS AND THEIR FREQUENCY
# for i in range(len(theList)):
#     if i == 0:
#         continue
#     if theList[i][0] not in theDict.keys():
#         theDict[theList[i][0]] = 1
#
#     else:
#         theDict[theList[i][0]] = theDict[theList[i][0]] + 1

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





for i in mstudents:
    print i.getID()
    print i.getOffsets()
    print i.getBehaviors()
    print i.getAffects(),"\n"
    # else:
    #     for i in students:
    #         if





    #     students[i]= Student(studentID)
    #     students[i].addActions(theList[i][0],theList[i][1],theList[i][2])
    # else: # existing , just add action
    #     students[i].addActions(theList[i][0],theList[i][1],theList[i][2])





