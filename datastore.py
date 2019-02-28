import ZODB, ZODB.FileStorage
import persistent
import transaction



class Student(persistent.Persistent):
    studentName = ''
    secondName = ''
    def setStudentName(self, sName):
        self.studentName = sName
    def getStudentName(self):
        return self.studentName

    def setStudentSecondName(self, s2Name):
        self.secondName = s2Name
    def getStudentSecondName(self):
        return self.secondName 



storage = ZODB.FileStorage.FileStorage('mydata.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root



root.s1 = Student()

# set the data into the node
root.s1.setStudentName("james")
root.s1.setStudentSecondNames("aslkdja")
# save the changes!
transaction.commit()
