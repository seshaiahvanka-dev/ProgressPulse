import csv


class Employee():
    def __init__(self,emp_id,emp_name,emp_addrs,emp_dep):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_addrs = emp_addrs
        self.emp_dep = emp_dep

    def out(self):
        return [self.emp_id,self.emp_name,self.emp_addrs,self.emp_dep]

FILENAME = 'employee.csv'

def create_user(emp_id,emp_name,emp_addrs,emp_dep):
    emp = Employee(emp_id,emp_name,emp_addrs,emp_dep)
    with open(FILENAME,'a',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(emp.out())
        print('User Created Successfully.....')


def update_user(idk,n_id,n_name,n_addrs,n_dep):
    with open(FILENAME,'r',newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    UPDATED = False

    for emp in data:
        if emp[0] == str(idk):
            emp[0] = str(n_id)
            emp[1] = n_name
            emp[2] = n_addrs
            emp[3] = n_dep
            UPDATED = True

    if UPDATED:
        with open(FILENAME,'w',newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data)
            print('User Updated Successfully....')
    else:
        print('Invalid User....')

def delete_user(idd):
    with open(FILENAME,'r',newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    DELETED = False

    for emp in data:
        if emp[0] == idd:
            data.remove(emp)
            DELETED = True

    if DELETED:
        with open(FILENAME,'w',newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data)
            print('Deleted the user Successfully...')
    else:
        print('Invalid User...')

def main():
    print("Welcome to the Employee Management System..")
    print('Press 1 to Create the User.')
    print('Press 2 to Update the User..')
    print('Press 3 to Delete the User...')
    choice = int(input('Enter the Choice:\n'))
    if choice == 1:
        emp_id = input('Enter employee id:\n')
        emp_name = input('Enter employee name:\n')
        emp_addrs = input('Enter employee address:\n')
        emp_dep = input('Enter employee Department:\n')
        create_user(emp_id,emp_name,emp_addrs,emp_dep)
    elif choice == 2:
        idk = input('Enter the user to be updated:\n')
        n_id = input('Enter the new employee Id:\n')
        n_name = input('Enter the new employee name:\n')
        n_addrs = input('Enter the new employee address:\n')
        n_dep = input('Enter the new employee department:\n')
        update_user(idk,n_id,n_name,n_addrs,n_dep)
    elif choice == 3:
        idd = input('Enter the user to be deleted:\n')
        delete_user(idd)
    else:
        print('Enter the Valid Choice......')

if __name__ == '__main__':
    main()