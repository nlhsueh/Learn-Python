class GradeBook:
    '記錄及管理所有學生的所有科目的成績'

    def __init__(self, students, subjects, grades):
        """
        students: list of names (string)
        subject: list of subject (float)
        grade: list of list, grade[i][j] is the grade of
            student i in subject j
        Compute the average of each student, save to 
            studentAverages
        studentAverages: list of average (float)    
        """
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
            
    def getAverage(self):
        '回傳所有科目的平均, list of float'
        return self.studentAverages

    def getStudentAverage(self, i):
        'return the average of the student i'
        return self.studentAverages[i]

    def getSubjectAverage(self, j):
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
        'show self.grades'
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