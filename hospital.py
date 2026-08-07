import csv,json
from regex_utils import is_valid_email,is_valid_phone


FILEJSON = 'patients.json'
FILECSV = 'patients.csv'

class Hospital():
    def __init__(self,patient_id,name,email,phone,age,gender,diagnosis,admission_date):
        if not is_valid_email(email):
            exit("Invalid email,Please enter a valid email..")
        if not is_valid_phone(phone):
            exit("Invalid phone,Please enter a valid phone..")
        self.patient_id = patient_id
        self.name = name
        self.email = email
        self.phone = phone
        self.age = age
        self.gender = gender
        self.diagnosis = diagnosis
        self.admission_date = admission_date

    def to_dict(self):
        return {
            "patient_id" : self.patient_id,
            "name" : self.name,
            "email" : self.email,
            "phone" : self.phone,
            "age" : self.age,
            "gender" : self.gender,
            "diagnosis" : self.diagnosis,
            "admission_date" : self.admission_date
        }

    def to_list(self):
        return [self.patient_id,self.name,self.email,self.phone,self.age,self.gender,self.diagnosis,self.admission_date]

def create_patient(patient_id,name,email,phone,age,gender,diagnosis,admission_date):
    hospital = Hospital(patient_id,name,email,phone,age,gender,diagnosis,admission_date)
    try:
        with open(FILEJSON,'r') as f:
            data = json.load(f)
    except(FileNotFoundError,json.JSONDecodeError):
        data = []
    data.append(hospital.to_dict())
    with open(FILEJSON,'w') as f:
        json.dump(data,f,indent=4)
    with open(FILECSV,'a',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(hospital.to_list())
    print('Patient Created Successfully...')

def update_patient(id_to_update,n_patient_id,n_name,n_email,n_phone,n_age,n_gender,n_diagnosis,n_admission_date):
    if not is_valid_email(n_email):
        exit("Invalid email,Please enter a valid email..")
    if not is_valid_phone(n_phone):
        exit("Invalid phone,Please enter a valid phone..")
    try:
        with open(FILEJSON,'r') as f:
            data = json.load(f)
    except(FileNotFoundError,json.JSONDecodeError):
        data = []

    UPDATEDJSON = False
    UPDATEDCSV = False

    for pt in data:
        if pt['patient_id'] == id_to_update:
            pt['patient_id'] = n_patient_id
            pt['name'] = n_name
            pt['email'] = n_email
            pt['phone'] = n_phone
            pt['age'] = n_age
            pt['gender'] = n_gender
            pt['diagnosis'] = n_diagnosis
            pt['admission_date'] = n_admission_date
            UPDATEDJSON = True

    with open(FILECSV,'r',newline='') as f:
        datax = list(csv.reader(f))

    for pt in datax:
        if pt[0] == str(id_to_update):
            pt[0] = n_patient_id
            pt[1] = n_name
            pt[2] = n_email
            pt[3] = n_phone
            pt[4] = n_age
            pt[5] = n_gender
            pt[6] = n_diagnosis
            pt[7] = n_admission_date
            UPDATEDCSV = True
    if UPDATEDJSON and UPDATEDCSV:
        with open(FILEJSON,'w') as f:
            json.dump(data,f,indent=4)
        with open(FILECSV,'w',newline='') as f:
            writer = csv.writer(f)
            writer.writerows(datax)
        print('Updated Patient Successfully...')
    else:
        print('Invalid Patient Id....')

def delete_patient(id_to_delete):
    try:
        with open(FILEJSON,'r') as f:
            data = json.load(f)
    except(FileNotFoundError,json.JSONDecodeError):
        data = []

    with open(FILECSV,'r',newline='') as f:
        datax = list(csv.reader(f))

    DELETEDCSV = False
    DELETEDJSON = False

    for pt in data:
        if pt['patient_id'] == id_to_delete:
            data.remove(pt)
            DELETEDJSON = True

    for pt in datax:
        if pt[0] == str(id_to_delete):
            datax.remove(pt)
            DELETEDCSV = True

    if DELETEDJSON and DELETEDCSV:
        with open(FILEJSON,'w') as f:
            json.dump(data,f,indent=4)

        with open(FILECSV,'w',newline='') as f:
            writer = csv.writer(f)
            writer.writerows(datax)

        print('Deleted Patient Successfully....')
    else:
        print('Invalid Patient Id...')

def read_patients():
    with open(FILEJSON,'r') as f:
        print(json.load(f))

    with open(FILECSV,'r',newline='') as f:
        print(list(csv.reader(f)))

def search_patients(name):
    with open(FILEJSON,'r') as f:
        data = json.load(f)

    with open(FILECSV,'r') as f:
        datax = list(csv.reader(f))

    for pt in data:
        if pt['name'] == name:
            print(pt)

    for pt in datax:
        if pt[1] == name:
            print(pt)

def main():
    print('Welcome to the Hospital Patients Management System..')
    print('Press 1 to Create the Patient.')
    print('Press 2 to Update the Patient..')
    print('Press 3 to Delete the Patient...')
    print('Press 4 to Read all the Patients....')
    print('Press 5 to Search the Patients based on the name.....')
    choice = int(input('Enter your Choice:\n'))
    if choice == 1:
        patient_id = int(input('Enter the Patient Id:\n'))
        name = input('Enter the Patient Name:\n')
        email = input('Enter the Patient Email:\n')
        phone = input('Enter the Patient Phone Number:\n')
        age = input('Enter the Age of the Patient:\n')
        gender = input('Enter the Gender of the Patient:\n')
        diagnosis = input('Enter the Diagnosis of the Patient:\n')
        admission_date = input('Enter the Admission Date of the Patient:\n')
        create_patient(patient_id,name,email,phone,age,gender,diagnosis,admission_date)
    elif choice == 2:
        id_to_update = int(input('Enter the Id to update:\n'))
        n_patient_id = int(input('Enter the new Patient Id:\n'))
        n_name = input('Enter the new Patient Name:\n')
        n_email = input('Enter the new Patient Email:\n')
        n_phone = input('Enter the new Patient Phone Number:\n')
        n_age = input('Enter the new Age of the Patient:\n')
        n_gender = input('Enter the new Gender of the Patient:\n')
        n_diagnosis = input('Enter the new Diagnosis of the Patient:\n')
        n_admission_date = input('Enter the new Admission Date of the Patient:\n')
        update_patient(id_to_update,n_patient_id,n_name,n_email,n_phone,n_age,n_gender,n_diagnosis,n_admission_date)
    elif choice == 3:
        id_to_delete = int(input('Enter the Id to be Deleted:\n'))
        delete_patient(id_to_delete)
    elif choice == 4:
        read_patients()
    elif choice == 5:
        name = input('Enter the name to search:\n')
        search_patients(name)
    else:
        print('Invalid Choice.....')

if __name__ == '__main__':
    main()