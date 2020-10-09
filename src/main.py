from skfuzzy import control

from rules import all_rules
from utils import inform_diagnosis
from huminazed_questions import ask_about_fiver

aedes_aegypti_diagnosis = control.ControlSystem(all_rules)
medical_record = control.ControlSystemSimulation(aedes_aegypti_diagnosis)

medical_record = ask_about_fiver(medical_record)

medical_record.compute()

inform_diagnosis(medical_record.output['doenças'])
