from json import JSONEncoder
from clinic.patient import *

class PatientEncoder(JSONEncoder):
  def default(self, patient):
    if isinstance(patient, Patient):
      return {"__type__": "Patient", "phn": patient.get_phn(), "name": patient.get_name(), "birth_date": patient.get_birth_date(), "phone": patient.get_phone(), "email": patient.get_email(), "address": patient.get_address(), "autosave": True}
    return super().default(patient)