from PatientQueue import PatientQueue
from Patient import Patient
import os

def main(): 
    patient_queue = PatientQueue()
    
    options_dict = {
        1: showNextPatientView,
        2: addNewPatientView,
        3: attentPatientView,
        4: showLastFiveView,
    }

    while True:
        os.system('cls')
        print("\033[92mHello!\033[0m") 
        print("Choose an option:")
        print("1 - \033[94mShow next patient\033[0m") 
        print("2 - \033[94mAdd new patient to queue\033[0m") 
        print("3 - \033[94mAttend patient\033[0m") 
        print("4 - \033[94mShow last five attended patients\033[0m")
        print("\033[91m5 - Exit\033[0m")

        option = int(input("Choose an option: "))
        

        if (option >= 5 or option < 1):
            break
        
        options_dict[option](patient_queue)
    

def attentPatientView(patient_queue: PatientQueue):
    print("-----------------------")
    showNextPatientView(patient_queue)
    patient_queue.attend_highest_priority_patient()

def showLastFiveView(patient_queue: PatientQueue):
    print("----------------")
    print("This is the last five attended patients")
    for patient in patient_queue._attended_patients:
        print("*******************")
        print("Name: ", patient.name)
        print("Age: ", patient.age, " years old")
        print("Priority: ", patient.priority)
        print("*******************")
    input("Press enter to continue")
        

def addNewPatientView(patient_queue):
    name = str(input("Please insert patient's name: "))
    age = int(input("Please insert patient's age: "))
    priority = int(input("Please insert patient's priority: "))

    patient = Patient(name, age, priority)

    patient_queue.add_patient(patient)


def showNextPatientView(patient_queue):
    print("Your next patient is: ")
    next = patient_queue.get_next_patient()
    print("Name: ", next.name)
    print("Age: ", next.age, " years old")
    print("Priority: ", next.priority)
    input("Press enter to continue")

main()