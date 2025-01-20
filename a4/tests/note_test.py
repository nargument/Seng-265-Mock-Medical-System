from unittest import TestCase
from unittest import main
from clinic.note import Note

class NoteTest(TestCase):

	#def test_str(self):
	def test_eq(self):
		note_1 = Note(1, "Patient comes with headache and high blood pressure.")
		note_1a = Note(1, "Patient comes with headache and high blood pressure.")
		note_2 = Note(2, "Patient complains of a strong headache on the back of neck.")
		note_3 = Note(1, "Patient says high BP is controlled, 120x80 in general.")
		note_4 = Note(3, "Patient says high BP is controlled, 120x80 in general.")
		self.assertEqual(note_1, note_1a, "Identical notes should be equal")
		self.assertNotEqual(note_1, note_2, "Notes with different codes and texts should not be equal")		
		self.assertNotEqual(note_1, note_3, "Notes with different texts should not be equal")
		self.assertNotEqual(note_3, note_4, "Notes with different codes should not be equal")

