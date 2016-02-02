# CSV Merger
# Joenabie Gamao
# 01/28/2016
# References:  http://www.tutorialspoint.com/python/
import csv,os


def listdir_nohidden(path):
        for f in os.listdir(path):
            if not f.startswith('.'):

                yield f
class Initialize:

    def __init__(self, path):
        self.path = path
        self.paths = []
        self.files = []

        # counter = 0
        # for folder in listdir_nohidden(self.path):
        #     self.paths.append(self.path + folder + "/")
        #     counter += 1
        for f in listdir_nohidden(self.path):
            self.files.append(f)


    def gefFiles(self):
        return self.files




class Student:

    def __init__(self, studentID):
        self.id=studentID
        self.actions = []
        self.count = len(self.actions)

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

        return strx



theList = list()
theDict = dict()
path = raw_input("Enter Directory Path: ")
path.lower()
a = Initialize(path)

for i in a.gefFiles():
    directory = path + "/" + i
    with open(directory, 'rb') as ifile:
        reader = csv.reader(ifile, delimiter=',')
        row1 = next(reader)
        for row in reader:
            theList.append(row)






mstudents = list() # ARRAY OF STUDENT CLASSES

for i in range(len(theList)):
    # if i == 0:
    #     continue

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
    print i

    for x in mstudents:
        if i == x.getID():
            #print x.getActionCount()
            print x.getAction("offsets")
            print x.getAction("behaviors")
            print x.getAction("affects")
            print ""




