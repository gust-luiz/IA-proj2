from skfuzzy import control

from humanized_questions import (ask_about_conjuctivitis, ask_about_fever,
                                 ask_about_ganglionic_hypertrophy,
                                 ask_about_headache, ask_about_itch,
                                 ask_about_joint_pain, ask_about_melasma,
                                 ask_about_muscle_pain, ask_about_ganglionic_hypertrophy,
                                 ask_about_hemorrhagic_dyscrasia, ask_about_neurological_damage)
from rules import all_rules
from utils import inform_diagnosis


def run_system():
    aedes_aegypti_diagnosis = control.ControlSystem(all_rules)
    medical_record = control.ControlSystemSimulation(aedes_aegypti_diagnosis)

    questions_to_ask = [
        ask_about_fever,
        ask_about_melasma,
        ask_about_muscle_pain,
        ask_about_joint_pain,
        ask_about_conjuctivitis,
        ask_about_headache,
        ask_about_itch,
        ask_about_ganglionic_hypertrophy,
        ask_about_hemorrhagic_dyscrasia,
        ask_about_neurological_damage,
    ]

    for questions in questions_to_ask:
        medical_record = questions(medical_record)

    medical_record.compute()

    inform_diagnosis(medical_record.output['doenças'])


if __name__ == '__main__':
    run_system()
