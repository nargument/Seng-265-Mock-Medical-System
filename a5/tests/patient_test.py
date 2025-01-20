from unittest import TestCase
from unittest import main
from clinic.patient import Patient

class PatientTest(TestCase):

	#def test_str(self):
	def test_eq(self):
		patient_1 = Patient(9798884444, "Ali Mesbah", "1980-03-03", "250 301 6060", "mesbah.ali@gmail.com", "500 Fairfield Rd, Victoria")
		patient_1a = Patient(9798884444, "Ali Mesbah", "1980-03-03", "250 301 6060", "mesbah.ali@gmail.com", "500 Fairfield Rd, Victoria")
		patient_2 = Patient(9792226666, "Jin Hu", "2002-02-28", "278 222 4545", "jinhu@outlook.com", "200 Admirals Rd, Esquimalt")
		patient_3 = Patient(9790012000, "John Doe", "2002-02-28", "250 203 1010", "john.doe@gmail.com", "300 Moss St, Victoria")
		patient_4 = Patient(9790014444, "Mary Doe", "1995-07-01", "250 203 2020", "mary.doe@gmail.com", "300 Moss St, Victoria")
		patient_5 = Patient(9792225555, "Joe Hancock", "1990-01-15", "278 456 7890", "john.hancock@outlook.com", "5000 Douglas St, Saanich")
		self.assertEqual(patient_1, patient_1a, "Identical patients should be equal")
		self.assertNotEqual(patient_1, patient_2, "Patients with different info should not be equal")		
		self.assertNotEqual(patient_2, patient_3, "Patients with same birthday but different names should not be equal")
		self.assertNotEqual(patient_3, patient_4, "Patients with the same address but different names should not be equal")
		self.assertEqual(patient_5, patient_5, "The same patient should be equal")
