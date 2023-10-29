import unittest
from Patient import Patient
class PatientTests(unittest.TestCase): 
    def setUp(self):
        self._defaultPatient = Patient("Diego Trevisan", 22, 10)

    def test_patient_name(self):
        self.assertEqual("Diego Trevisan", self._defaultPatient.name)
    
    def test_patient_age(self):
        self.assertEqual(22, self._defaultPatient.age)

    def test_patient_priority(self):
        self.assertEqual(10, self._defaultPatient.priority)
    



if __name__ == "__main__":
    unittest.main()
