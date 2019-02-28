import ZODB, ZODB.FileStorage
import persistent
import transaction

class Student(persistent.Persistent):
    studentName = ''
    def setStudentName(self, sName):
        self.studentName = sName
    def getStudentName(self):
        return self.studentName


