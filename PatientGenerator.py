from Patient import Patient
import random

def patient_generator(number_of_patients: int):
    patient_names = [
    "Luca Rossi",
    "Sofia Bianchi",
    "Marco Russo",
    "Elena Martini",
    "Alessio Conti",
    "Valentina Ferrari",
    "Giovanni Romano",
    ]
    patients = []
    for i in range(0, number_of_patients, 1):
        name_random = patient_names[random.randint(0, 6)]
        age_random = random.randint(1, 110)
        priority = random.randint(1, 10)
        patient = Patient(name_random, age_random, priority)
        patients.append(patient)
    return patients
