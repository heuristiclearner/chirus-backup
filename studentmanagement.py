class Student:
    student_dictionary = {}
    school_name = 'XYZ'
    def __init__(self):
        self.roll_no = input('\n\tEnter the Student Roll Number: ')
        self.name = input('\tEnter the Student Name: ')
        self.phone_number = input('\tEnter the Student Phone Number: ')
        self.address = input('\tEnter the Student Address: ')
        student_class = input('\tEnter the Student class [ex: 1 2 3 4 5 6 7 8 9 10]')
        
        if student_class in StudentClass.classes:
            StudentClass.classes[student_class].studentList.append(self)
        else:
            new_class = StudentClass(student_class)
            new_class.studentList.append(self)
            StudentClass.classes[student_class] = new_class
        self.student_class = StudentClass.classes[student_class]
        self.getStudent()
        print("\n Student Added Successfully")
        
    def getStudent(self):
        print("\n---STUDENT DETAILS---\n")
        print('\tRoll Number:',self.roll_no)
        print('\tName: ',self.name)
        print('\tPhone Number: ',self.phone_number)
        print('\tAddress: ',self.address)
        print('\tClass: ',self.student_class.name)
        print('\tSchool Name : XYZ')
        
    def updateStudent(self):
        print('\t\tSelect option to update student details\n')
        print('\t\t1) To Change Student Name')
        print('\t\t2)To Change Student Phoen Number')
        print('\t\t3) To Change Student Phone Number')
        print('\t\t4) To Change Student Class\n')
        option = input('\t\tEnter any above given option')
        print()
        
        if option in ['1','2','3','4']:
            if option == '1':
                self.name = input('\t\tEnter the Student New Name: ')
                print('\n\t\t Student Name Change Successfully\n')
            elif option == '2':
                self.phone_number = input('\t\tEnter the Student New Phone Number ')
                print('\n\t\tStudent Phone Number Changed Successfully\n')
                
            elif option == '3':
                self.address = input('\t\tEnter the Student New Address: ')
                print('\n\t\tStudent Adress Changed Successfully\n')
            else:
                new_class = input('\t\tEnter the Student New Class Name: ')
                self.student_class.studentList.remove(self)
                try:
                    self.student_class = StudentClass.classes[new_class]
                    self.student_class.studentList.append(self)
                except:
                    addClass = StudentClass(new_class)
                    self.student_class = addClass
                    addClass.studentList.append(self)
                print('\n\t\tStudent Class Changed Successfully\n')
            self.getStudent()
        else:
            print('\n\t\tYou have choosen wrong option')
    @classmethod
    def updateSchoolName(cls,new_school_name):
        cls.school_name = new_school_name
    @classmethod
    def getTotalStudentCount(cls):
        return len(cls.student_dictionary)


class StudentClass:
    
    classes = {}
    def __init__(self,name):
        self.name = name
        StudentClass.classes[name] = self
        self.studentList = []  

def main():
    print(f'---Welcome to {Student.school_name} school---\n')
    print('\t1) To Get Student Details')
    print('\t2) To Add New Student')
    print('\t3) To Remove Student')
    print('\t4) To Update Student Details')
    print('\t4) To Update School Name')
    print('\t6) To Get Number of Students in School')
    print('\t7)To Get All Student Details')
    print('\t8) To Get Any Class Student Details')
    
    option = input('Enter any above given options: ')
    print()
    
    if option == '1':
        roll_no = input('\tEnter the Roll Number of a Student: ')
        try:
            Student.student_dictionary[roll_no].getStudent()
        except:
            print('\t\tYou have Entered the wrong roll number')
    elif option == '2':
        new_student = Student()
        Student.student_dictionary[new_student.roll_no] = new_student
    elif option == '3':
        roll_no = input('\tEnter the Roll Number of a Student: ')
        try:
            student = Student.student_dictionary.pop(roll_no)
            student.student_class.studentList.remove(student)
            print('\t\t',"",roll_no,"",'Student Deleted Successfully')
        except:
            print("\t\tNo Student there to delete")
    elif option == '4':
        roll_no = input('\tEnter the Roll Number of a Student: ')
        print()
        try:
            Student.student_dictionary[roll_no].updateStudent()
        except:
            print('\n\t\tYou have entered the wrong roll number')  
    elif option == '5':
        new_school_name = input('\tEnter the New School Name: ')
        Student.updateSchoolName(new_school_name)
        print('School Name Changed Successfully')
    elif option == '6':
        print("Total Number of Student in School: ",Student.getTotalStudentCount())
    elif option == '7':
        if Student.student_dictionary:
            print("Total Number of Student in School: ",Student.getTotalStudentCount())
            print('\nTotal Student List with Details\n')
            for sNo, student in enumerate(Student.student_dictionary.values()):
                print('Student -',sNo+1)
                student.getStudent()
                print()
        else:
            print('\tNo student present')
    elif option == '8':
        try:
            students = StudentClass.classes[input('\tEnter the Class Name:')]
            print('\nStudents of class -',students.name)
            print(f'\nTotal Number Of students in Class {students.name}:{len(students.studentList)}')
            print()
            for sNo, student in enumerate(students.studentList):
                print('Student -',sNo+1)
                student.getStudent()
                print()
        except:
            print('\nYou entered wrong class name or no students there')
            
if __name__ == '__main__':
    option = 'y'
    while option == 'y':
        main()
        option = input('\n Do you want to Continue [y/n?]:')
        print()
        
    