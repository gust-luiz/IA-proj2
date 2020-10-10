from skfuzzy import control

from humanized_questions import ask_about_fiver
from rules import all_rules
from utils import inform_diagnosis


def run_system():
    aedes_aegypti_diagnosis = control.ControlSystem(all_rules)
    medical_record = control.ControlSystemSimulation(aedes_aegypti_diagnosis)

    medical_record = ask_about_fiver(medical_record)

    medical_record.compute()

    inform_diagnosis(medical_record.output['doenças'])

if __name__ == '__main__':
    run_system()
