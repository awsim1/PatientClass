file_for_patients = 'patients.txt'
list_of_patients = []

'''Patient class has 5 properties (pid, name, disease, gender, age) and 9 methods'''


class Patient:
    def __init__(self, pid=-1, name='', disease='', gender='', age=-1):
        if pid != -1:
            self.pid = pid
        if name != '':
            self.name = name
        if disease != '':
            self.disease = disease
        if gender != '':
            self.gender = gender
        if age != -1:
            self.age = age

    def formatPatientInfo(self, txt_to_format):
        formatted = '_'.join(txt_to_format)
        return formatted

    def enterPatientInfo(self):
        self.pid = int(input("Enter patients’s ID: \n"))
        self.name = input("Enter patient’s name: \n")
        self.disease = input("Enter patient's disease: \n")
        self.gender = input("Enter patient's gender: \n")
        self.age = int(input("Enter patient's age: \n"))
        return [str(self.pid), self.name, self.disease, self.gender, str(self.age)]

    def readPatientsFile(self):
        file = open(file_for_patients, 'r')
        list_of_patients = []
        for each_line in file:
            list_of_patients.append(each_line.rstrip().split('_'))
        file.close()
        return list_of_patients

    def searchPatientByID(self):
        id_number = int(input("Enter the Patient's ID: \n"))
        list_of_patients = self.readPatientsFile()
        total_rows = len(list_of_patients)
        current_row = 1
        last_row = total_rows - 1
        patient_found = ''
        while current_row < total_rows:
            if str(id_number) == list_of_patients[current_row][0]:
                print(f'{"ID":<10}' + f'{"Name":<15}' + f'{"Disease":<15}' + f'{"Gender":<15}' + "Age")
                print(
                    f'{list_of_patients[current_row][0]:<10}' + f'{list_of_patients[current_row][1]:<15}' + f'{list_of_patients[current_row][2]:<15}' + f'{list_of_patients[current_row][3]:<15}' +
                    list_of_patients[current_row][4])
                patient_found = 'yes'
            if patient_found != 'yes' and current_row == last_row:
                print("Can't find the patient with the same ID on the system.\n")
            current_row += 1

    def displayPatientInfo(self):
        list_of_patients = self.readPatientsFile()
        total_rows = len(list_of_patients)
        current_row = 1
        print(f'{"ID":<10}' + f'{"Name":<15}' + f'{"Disease":<15}' + f'{"Gender":<15}' + "Age")
        while current_row < total_rows:
            print(
                f'{list_of_patients[current_row][0]:<10}' + f'{list_of_patients[current_row][1]:<15}' + f'{list_of_patients[current_row][2]:<15}' + f'{list_of_patients[current_row][3]:<15}' +
                list_of_patients[current_row][4])
            current_row += 1

    def editPatientInfo(self, list_of_patients):
        id_number = int(input("Please enter the id of the patient that you want to edit their information: \n"))
        self.pid = id_number
        total_rows = len(list_of_patients)
        current_row = 1
        last_row = total_rows - 1
        patient_found = ''
        self.name = input("Enter new Name: \n")
        self.disease = input("Enter new disease: \n")
        self.gender = input("Enter new gender: \n")
        self.age = input("Enter new age: \n")
        while current_row < total_rows:
            if str(id_number) == list_of_patients[current_row][0]:
                list_of_patients[current_row][1] = self.name
                list_of_patients[current_row][2] = self.disease
                list_of_patients[current_row][3] = self.gender
                list_of_patients[current_row][4] = self.age
                patient_found = 'yes'
            if patient_found != 'yes' and current_row == last_row:
                print("Can't find the patient with the same ID on the system\n")
            current_row += 1
        self.writeListOfPatientsToFile(list_of_patients)

    def writeListOfPatientsToFile(self, list_of_patients):
        patients_file = open(file_for_patients, 'w')
        for each_line in list_of_patients:
            add_line = self.formatPatientInfo(each_line)
            patients_file.write(add_line)
            patients_file.write('\n')
        patients_file.close()

    def addPatientToFile(self):
        list_of_patients = self.readPatientsFile()
        self.writeListOfPatientsToFile(list_of_patients)
        patient_to_add = self.enterPatientInfo()
        patients_file = open(file_for_patients, 'a')
        patients_file.write(self.formatPatientInfo(patient_to_add))
        patients_file.write('\n')
        patients_file.close()
