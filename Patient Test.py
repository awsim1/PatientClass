from Patient import Patient

my_patient = Patient()
isRunning = True

while isRunning:

    patients_menu = int(input("Patients Menu:\n1 - Display patients list\n2 - Search for patient by ID\n3 - Add patient\n4 - Edit patient info\n5 - Back to the Main Menu\n"))

    if patients_menu == 1:
        my_patient.displayPatientInfo()
        print("Back to previous menu\n")
    if patients_menu == 2:
        my_patient.searchPatientByID()
        print("Back to previous menu\n")
    if patients_menu == 3:
        my_patient.addPatientToFile()
        print("Back to previous menu\n")
    if patients_menu == 4:
        my_patient.editPatientInfo()
        print("Back to previous menu\n")
    if patients_menu == 5:
        quit()