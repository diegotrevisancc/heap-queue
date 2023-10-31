import heapq
from PatientGenerator import patient_generator

class PatientQueue:
    def __init__(self):
        self._patients = patient_generator(10)
        heapq.heapify(self._patients)
        self._attended_patients = []
    
    def add_patient(self, patient):
        heapq.heappush(self._patients, patient)
    
    def attend_highest_priority_patient(self):
        patient = max(self._patients)
        self._patients.remove(patient)
        heapq.heapify(self._patients)
        self._attended_patients.append(patient)

    def get_next_patient(self):
        return max(self._patients)
    
    @property
    def patients(self):
        return self._patients
    
    @property
    def attended_patients(self):
        return self._attended_patients


