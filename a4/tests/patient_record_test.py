from unittest import TestCase
from unittest import main
from clinic.patient_record import PatientRecord
from clinic.note import Note

class Patient_Record_Test(TestCase):

	#def test_str(self):
	def test_create_search_note(self):
		patient_record_1 = PatientRecord(0)
		note_0 = patient_record_1.search_note(1)
		# search in an empty note dictionary
		self.assertIsNone(note_0, 'no notes in patient record')

		patient_record_1.create_note('This is note 1')
		note_1 = patient_record_1.search_note(1)
		expected_note = Note(1,'This is note 1')
		# check if the created note is created and can be searched
		self.assertEqual(note_1, expected_note, 'note 1 create and searched in patient record')
		note_2 = patient_record_1.search_note(9)
		# searching for a note that doesn't exist
		self.assertIsNone(note_2, 'no note at code 9')

		# create and test multpile notes
		patient_record_1.create_note('This is note 2')
		patient_record_1.create_note('This is note 3')
		patient_record_1.create_note('This is note 4')
		note_3 = patient_record_1.search_note(3)
		note_4 = patient_record_1.search_note(4)
		expected_note_2 = Note(3,'This is note 3')
		expected_note_3 = Note(4,'This is note 4')
		# test notes later in the dictionary
		self.assertEqual(note_3, expected_note_2, 'note 1 create and searched in patient record')
		self.assertEqual(note_4, expected_note_3, 'note 1 create and searched in patient record')

	def test_retrieve_notes(self):
		patient_record_1 = PatientRecord(0)
		note_list = []
		# test when patient record has no notes
		self.assertEqual(patient_record_1.retrieve_notes('note'), note_list, 'there are no notes in patient record')
		patient_record_1.create_note('This is note 1')
		expected_note_1 = Note(1,'This is note 1')
		note_list.append(expected_note_1)
		# test after 1 note has been added
		self.assertEqual(patient_record_1.retrieve_notes('note'), note_list, 'theres 1 note in patient record')
		patient_record_1.create_note('This is note 2')
		patient_record_1.create_note('This is note 3')
		patient_record_1.create_note('This is note 4')
		expected_note_2 = Note(2,'This is note 2')
		expected_note_3 = Note(3,'This is note 3')
		expected_note_4 = Note(4,'This is note 4')
		note_list.append(expected_note_2)
		note_list.append(expected_note_3)
		note_list.append(expected_note_4)
		# test after multiple notes have been added
		self.assertEqual(patient_record_1.retrieve_notes('note'), note_list, 'theres 1 note in patient record')
		# test a list with only a specific sequence in it
		note_list_2 = [expected_note_3]
		self.assertEqual(patient_record_1.retrieve_notes('3'), note_list_2, 'theres 1 note in patient record')

	def test_update_note(self):
		patient_record_1 = PatientRecord(0)
		expected_note_1 = Note(1,'new note 1')
		# test update when there are no notes
		self.assertFalse(patient_record_1.update_note(1, 'new note 1'))
		patient_record_1.create_note('This is note 1')
		patient_record_1.create_note('This is note 2')
		patient_record_1.create_note('This is note 3')
		patient_record_1.create_note('This is note 4')
		# check if update returns true
		self.assertTrue(patient_record_1.update_note(1, 'new note 1'))
		# check if the note has been updated
		self.assertEqual(patient_record_1.search_note(1), expected_note_1, 'note 1 has been updated')

	def test_delete_note(self):
		patient_record_1 = PatientRecord(0)
		# delete from empty dictionary
		self.assertFalse(patient_record_1.delete_note(1), 'no notes exist')
		patient_record_1.create_note('This is note 1')
		patient_record_1.create_note('This is note 2')
		patient_record_1.create_note('This is note 3')
		patient_record_1.create_note('This is note 4')
		expected_note_3 = Note(3,'This is note 3')
		# delete non existant note
		self.assertFalse(patient_record_1.delete_note(5), 'note 5 doesnt exist')
		# delete lastest note
		self.assertTrue(patient_record_1.delete_note(4), 'delete the latest note')
		# search for note 4 after its deleted
		self.assertIsNone(patient_record_1.search_note(4), 'make sure note 4 isnt in the dictionary')
		# try deleting it again
		self.assertFalse(patient_record_1.delete_note(4), 'delete the latest deleted note')
		patient_record_1.delete_note(2)
		# check for note 2 after deleting
		self.assertIsNone(patient_record_1.search_note(2), 'make sure note 2 isnt in the dictionary')
		# check for note 3 after deleting note 2
		self.assertEqual(patient_record_1.search_note(3), expected_note_3, 'make sure note 3 is still correct')

	def test_list_notes(self):
		patient_record_1 = PatientRecord(0)
		note_list = []
		# test when there are no notes
		self.assertEqual(patient_record_1.list_notes(), note_list, 'should be an empty list')
		patient_record_1.create_note('This is note 1')
		patient_record_1.create_note('This is note 2')
		patient_record_1.create_note('This is note 3')
		patient_record_1.create_note('This is note 4')
		expected_note_1 = Note(1,'This is note 1')
		expected_note_2 = Note(2,'This is note 2')
		expected_note_3 = Note(3,'This is note 3')
		expected_note_4 = Note(4,'This is note 4')
		note_list.append(expected_note_4)
		note_list.append(expected_note_3)
		note_list.append(expected_note_2)
		note_list.append(expected_note_1)
		# test the length of the list
		self.assertEqual(len(patient_record_1.list_notes()), 4, 'length of list should be 4')
		# test after creating notes
		self.assertEqual(patient_record_1.list_notes(), note_list, 'should contain the added notes')
		patient_record_1.delete_note(3)
		note_list_2 = [Note(4,'This is note 4'), Note(2,'This is note 2'), Note(1,'This is note 1')]
		# test after deleting a note
		self.assertEqual(patient_record_1.list_notes(), note_list_2, 'should not contain note 3')





