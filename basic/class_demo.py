class GradeBook:
    '記錄所有學生的所有科目的成績'

    """
    names is a list of string, grades is a two-dim int to record the grades
    """
    def __init__(self, students, subjects, grades):
        self.students = students
        self.grades = grades
        self.subjects = subjects
        
        # compute average of each student
        self.studentAverages = []
        for s in grades:
            sum = 0
            for g in s:
                sum += g
            self.studentAverages.append(sum//len(s))  
            
        # compute average of each subject    
        
    def get_average():
        return 0

    def getStudentAverage(self, i):
        'return the average of the student i'
        return self.studentAverages[i]

    def getSubjectAverage(j):
        'return the average of the subject j'

    def getSubjectGrade(self, j):
        'retrun the greade list of the subject j'
        subjectGrades = []
        for g in self.grades[j]:
            subjectGrades.append(g[j])
            
        return subjectGrades

    def getStudentGrades(self, i):
        'return the grade list of student i'
        return self.grades[i]    

    def showGrade(self):
        'show student name, grade, average and standard deviation in each subject'
        print (self.grades)
   
    def showAverages(self):
        'show student name, grade, average and standard deviation in each subject'
        stList = ""
        for s in students:
            stList += s
            stList += ", "
        stList = stList[0:len(stList)-2] #remove the last ,
        print ("The average of students " + stList + " are: ")
        print (self.studentAverages)


grades = [[12,23,34], [45,56,67], [78,89,90]]        
students = ["Nick", "John", "Peter"]
subjects = ["English", "Math", "Physical"]

gBook = GradeBook(students, subjects, grades)

gBook.showGrade()
gBook.showAverages()