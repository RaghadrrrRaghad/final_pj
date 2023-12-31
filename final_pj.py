import uuid

"""ITF 07 Final Project Attendance System
# TODO 1 Enter your name and submission date
Name : "Raghad Haniya"
Delivery Date : 22-6-23
"""


# TODO 2 Define Course Class and define constructor with
# course_id (generated using uuid4) ,
# course name (user_input) and
# course mark (user_input)
class Course:
    def __init__(self, name, mark):
        self.course_id = str(uuid.uuid4().int)
        self.course_name = name
        self.course_mark = mark


class Student:
    # TODO 3 define static variable indicates total student count
    student_count = 0

    # TODO 4 define a constructor which includes
    # student_id (unique using uuid module)
    # student_name (user input)
    # student_age (user input)
    # student_number (user_input)
    # courses_list (List of Course Objects)

    def __init__(self, name=None, age=0, st_num=0, *courses_list):
        self.st_id = str(uuid.uuid4().int)
        self.name = name
        self.age = age
        self.st_num = st_num
        self.courses_list = [courses_list]

    # TODO 5 define a method to enroll new course to student courses list
    def enroll_new_course(self, name, mark):
        new_course = Course(name, mark)
        Student().courses_list.append(new_course)

    # method to get_student_details as dict
    def get_student_details(self):
        return self.__dict__

    # method to get_student_courses
    def get_student_courses(self):
        # TODO 6 print student courses with their marks
        for i in self.courses_list:
            print(i)

    # method to get student_average as a value
    def get_student_average(self):
        # TODO 7 return the student average
        sum = 0
        for i in range(Course.student_count):
            sum += Course.course_mark
        return sum / Course.student_count


# in Global Scope
# TODO 8 declare empty students list

students_list = []

while True:

    # TODO 9 handle Exception for selection input
    try:
        selection = int(input("1.Add New Student\n"
                              "2.Delete Student\n"
                              "3.Display Student\n"
                              "4.Get Student Average\n"
                              "5.Add Course to student with mark.\n"
                              "6.Exit"))

        if selection == 1:

            # TODO 10 make sure that Student number is not exists before
            student_number = input("Enter Student Number")
            for i in students_list:
               if i.st_num.__eq__(student_number):
                   print(f'{student_number} is exists')
                   break


            student_name = input("Enter Student Name")
            while True:
                try:
                    student_age = int(input("Enter Student Age"))
                    break
                except:
                    print("Invalid Value")

            # TODO 11 create student object and append it to students list
            new_student = Student(student_name, student_age, student_number)
            students_list.append(new_student)

            print("Student Added Successfully")

        elif selection == 2:
            student_number = input("Enter Student Number")
            # TODO 12 find the target student using loops and delete it if exist , if not print ("Student Not Exist")
            for i in students_list:
                if i.st_num.__eq__(student_number):
                    students_list.remove(i)
                    break
                elif i == len(students_list)-1:
                    print("Student Not Exist")
        elif selection == 3:
            student_number = input("Enter Student Number")
            # TODO 13 find the target student using loops and print student detials  if exist , if not print ("Student Not Exist")
            for i in students_list:
                if student_number in i:
                    print(i.get_student_details())
                    break
                elif i == len(students_list)-1:
                    print("Student Not Exist")

        elif selection == 4:
            student_number = input("Enter Student Number")
            # TODO 14 find the target student using loops and get student average  if exist , if not print ("Student Not Exist")
            for i in students_list:
                if student_number in i:
                    print(i.get_student_average())
                    break
                elif i == len(students_list)-1:
                    print("Student Not Exist")

        elif selection == 5:
            student_number = input("Enter Student Number")
            # TODO 15 ask user to enter course name and course mark then create coures object then append it to target student courses
            for i in students_list:
                if student_number in i:
                    course_name = input("Enter course name :")
                    course_mark = input("Enter course mark :")
                    i.enroll_new_course(course_name, course_mark)
                    break
                elif i == len(students_list)-1:
                    print("Student Not Exist")

        else:
            # TODO 16 call a function to exit the program
            break

    except Exception as e:
        print("please enter from one to six")
        print(e)