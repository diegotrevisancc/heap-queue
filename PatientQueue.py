import heapq
from PatientGenerator import patient_generator

class PatientQueue:
    def __init__(self):
        self.patients = patient_generator(10)
        heapq.heapify(self.patients)
        self.attended_patients = []
    
    def add_patient(self, patient):
        heapq.heappush(self.patients, patient)

