from skfuzzy import control

from humanized_questions import (ask_about_conjuctivitis, ask_about_fever,
                                 ask_about_headache, ask_about_itch,
                                 ask_about_joint_pain, ask_about_melasma,
                                 ask_about_muscle_pain)
from rules import all_rules
from src.humanized_questions import ask_about_conjuctivitis
from utils import inform_diagnosis


def run_system():
    aedes_aegypti_diagnosis = control.ControlSystem(all_rules)
    medical_record = control.ControlSystemSimulation(aedes_aegypti_diagnosis)

    medical_record = ask_about_fever(medical_record)
    medical_record = ask_about_melasma(medical_record)
    medical_record = ask_about_muscle_pain(medical_record)
    medical_record = ask_about_joint_pain(medical_record)
    medical_record = ask_about_conjuctivitis(medical_record)
    medical_record = ask_about_headache(medical_record)
    medical_record = ask_about_itch(medical_record)

    medical_record.compute()

    inform_diagnosis(medical_record.output['doenças'])


if __name__ == '__main__':
    run_system()
