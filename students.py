import json


FILENAME = 'students.json'

class Student():
    def __init__(self,roll_no,name,course,grade):
        self.roll_no = roll_no
        self.name = name
        self.course = course
        self.grade = grade

    def to_dict(self):
        return {
            "roll_no" : self.roll_no,
            "name" : self.name,
            "course" : self.course,
            "grade" : self.grade
        }

def create_user(roll_no,name,course,grade):
    try:
        with open(FILENAME,'r') as f:
            data = json.load(f)
    except(FileNotFoundError,json.JSONDecodeError):
        data = []

    std = Student(roll_no,name,course,grade)
    data.append(std.to_dict())

    with open(FILENAME,'w') as f:
        json.dump(data,f,indent=4)

    print('User Created Successfully.....')

def read_users():
    with open(FILENAME,'r') as f:
        data = json.load(f)
        print(data)

def update_users(rlk,n_roll_no,n_name,n_course,n_grade):
    try:
        with open(FILENAME,'r') as f:
            data = json.load(f)
    except(FileNotFoundError,json.JSONDecodeError):
        data = []

    UPDATED = False

    for std in data:
        if std['roll_no'] == rlk:
            std['roll_no'] = n_roll_no
            std['name'] = n_name
            std['course'] = n_course
            std['grade'] = n_grade
            UPDATED = True

    if UPDATED:
        with open(FILENAME,'w') as f:
            json.dump(data,f,indent=4)
            print('User Updated Successfully.....')
    else:
        print('Invalid User....')

def delete_users(drl):
    try:
        with open(FILENAME,'r') as f:
            data = json.load(f)
    except(FileNotFoundError,json.JSONDecodeError):
        data =[]

    DELETED = False

    for std in data:
        if std['roll_no'] == drl:
            data.remove(std)
            DELETED = True

    if DELETED:
        with open(FILENAME,'w') as f:
            json.dump(data,f,indent=4)
            print('User Deleted Successfully...')
    else:
        print('Invalid User.....')

def search_users(n_course):
    try:
        with open(FILENAME,'r') as f:
            data = json.load(f)
    except(FileNotFoundError,json.JSONDecodeError):
        data = []

    for std in data:
        if std['course'] == n_course:
            print(std)

def main():
    print("Welcome to Student Progress Report!")
    print("Press 1 to Create the User.")
    print("Press 2 to Read all the Users..")
    print("Press 3 to Update the User...")
    print("Press 4 to Delete the user....")
    print("Press 5 to Search users in the specific course.....")
    choice = int(input('Enter the Choice:\n'))
    if choice == 1:
        roll_no = int(input('Enter the Roll No of the Student:\n'))
        name = input('Enter the Name of the Student:\n')
        course = input('Enter the Course of the Student:\n')
        grade = input('Enter the Grade of the Student:\n')
        create_user(roll_no,name,course,grade)
    elif choice == 2:
        read_users()
    elif choice == 3:
        rlk = int(input('Enter the user to be Updated:\n'))
        n_roll_no = int(input('Enter the new Roll No:\n'))
        n_name = input('Enter the new Name:\n')
        n_course = input('Enter the new Course:\n')
        n_grade = input('Enter the new Grade:\n')
        update_users(rlk,n_roll_no,n_name,n_course,n_grade)
    elif choice == 4:
        drl = int(input('Enter the user to be Deleted:\n'))
        delete_users(drl)
    elif choice == 5:
        n_course = input('Enter the course:\n')
        search_users(n_course)
    else:
        print("Invalid Choice.......")
if __name__ == '__main__':
    main()