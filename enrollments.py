import csv
from regex_utils import is_valid_phone,is_valid_email


FILENAME = 'enrollments.csv'

class InvalidEmailError(Exception):
    pass

class InvalidPhoneError(Exception):
    pass

class Enrollments():
    def __init__(self,enrollment_id,student_name,student_email,student_phone,course_name,course_id,enrollment_date):
        if not is_valid_email(student_email):
            raise InvalidEmailError('Invalid Email, Please Enter a Valid Email')
        if not is_valid_phone(student_phone):
            raise InvalidPhoneError('Invalid Phone Number, Please Enter a Valid Phone Number')
        self.enrollment_id = enrollment_id
        self.student_name = student_name
        self.student_email = student_email
        self.student_phone = student_phone
        self.course_name = course_name
        self.course_id = course_id
        self.enrollment_date = enrollment_date

    def to_list(self):
        return [self.enrollment_id,self.student_name,self.student_email,self.student_phone,self.course_name,self.enrollment_id,self.enrollment_date]

def create_enrollment(enrollment_id,student_name,student_email,student_phone,course_name,course_id,enrollment_date):
    enr = Enrollments(enrollment_id,student_name,student_email,student_phone,course_name,course_id,enrollment_date)
    try:
        with open(FILENAME,'a',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(enr.to_list())
    except(FileNotFoundError):
        data = []
    print('Enrollement Created Successfully...')

def update_enrollment(id_to_update,n_enrollment_id,n_student_name,n_student_email,n_student_phone,n_course_name,n_course_id,n_enrollment_date):
    if not is_valid_email(n_student_email):
        raise InvalidEmailError('Invalid Email, Please Enter a Valid Email')
    if not is_valid_phone(n_student_phone):
        raise InvalidPhoneError('Invalid Phone Number, Please Enter a Valid Phone Number')
    with open(FILENAME,'r',newline='') as f:
        data = list(csv.reader(f))

    UPDATED = False

    for enr in data:
        if enr[0] == str(id_to_update):
            enr[0] = n_enrollment_id
            enr[1] = n_student_name
            enr[2] = n_student_email
            enr[3] = n_student_phone
            enr[4] = n_course_name
            enr[5] = n_course_id
            enr[6] = n_enrollment_date
            UPDATED = True

    if UPDATED:
        with open(FILENAME,'w',newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data)
            print('Updated Enrollment Successfully...')
    else:
        print('Invalid Enrollment ID....')

def delete_enrollment(id_to_delete):
    with open(FILENAME,'r',newline='') as f:
        data = list(csv.reader(f))

    DELETED = False

    for enr in data:
        if enr[0] == str(id_to_delete):
            data.remove(enr)
            DELETED = True

    if DELETED:
        with open(FILENAME,'w',newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data)
            print('Deleted the Enrollment Successfully...')
    else:
        print('Invalid Enrollment Id....')

def read_enrollments():
    with open(FILENAME,'r',newline='') as f:
        data = list(csv.reader(f))
    print(data)

def search_enrollments(course_name):
    with open(FILENAME,'r',newline='') as f:
        data = list(csv.reader(f))

    for enr in data:
        if enr[4] == course_name:
            print(enr)

def main():
    print('Welcome to the Online Course Enrollment System..')
    print('Press 1 to Create the Enrollment.')
    print('Press 2 to Update the Enrollment..')
    print('Press 3 to Delete the Enrollment...')
    print('Press 4 to Read all the Enrollments....')
    print('Press 5 to Search the Enrollments based on the course.....')
    choice = int(input('Enter Your Choice:\n'))
    if choice == 1:
        enrollment_id = int(input('Enter the Enrollment Id:\n'))
        student_name = input('Enter the Student Name:\n')
        student_email = input('Enter the Student Email:\n')
        student_phone = input('Enter the Student Phone:\n')
        course_name = input('Enter the Course name:\n')
        course_id = int(input('Enter the course Id:\n'))
        enrollment_date = input('Enter the Enrollment Date:\n')
        create_enrollment(enrollment_id,student_name,student_email,student_phone,course_name,course_id,enrollment_date)
    elif choice == 2:
        id_to_update = int(input('Enter the Enrollment id to Update:\n'))
        n_enrollment_id = int(input('Enter the new Enrollment Id:\n'))
        n_student_name = input('Enter the new Student Name:\n')
        n_student_email = input('Enter the new Student Email:\n')
        n_student_phone = input('Enter the new Student Phone:\n')
        n_course_name = input('Enter the new Course name:\n')
        n_course_id = int(input('Enter the new course Id:\n'))
        n_enrollment_date = input('Enter the new Enrollment Date:\n')
        update_enrollment(id_to_update,n_enrollment_id,n_student_name,n_student_email,n_student_phone,n_course_name,n_course_id,n_enrollment_date)
    elif choice == 3:
        id_to_delete = int(input('Enter the id to be Deleted:\n'))
        delete_enrollment(id_to_delete)
    elif choice == 4:
        read_enrollments()
    elif choice == 5:
        course_name = input('Enter the course name to search:\n')
        search_enrollments(course_name)
    else:
        print('Invalid Choice...')

if __name__ == '__main__':
    main()