import unittest
from Patient import Patient
from PatientGenerator import patient_generator
import random

class PatientTests(unittest.TestCase): 
    def setUp(self):
        self.patients: list = patient_generator(10)

    def test_patient_generator_size(self):
        self.assertEqual(10, len(self.patients))

    def test_patient_instance_type(self):
        random_patient = self.patients[random.randint(0, 9)]
        self.assertIsInstance(random_patient, Patient)
    
    def test_patient_name(self):
        random_patient_name = self.patients[random.randint(0, 9)].name
        self.assertIsInstance(random_patient_name, str)

    def test_patient_priority(self):
        random_patient_priority = self.patients[random.randint(0, 9)].priority
        self.assertIsInstance(random_patient_priority, int)
    
    def test_patient_age(self):
        random_patient_age = self.patients[random.randint(0, 9)].age
        self.assertIsInstance(random_patient_age, int)

if __name__ == "__main__":
    unittest.main()
