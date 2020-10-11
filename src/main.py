from skfuzzy import control

from humanized_questions import (ask_about_conjuctivitis, ask_about_fever,
                                 ask_about_ganglionic_hypertrophy,
                                 ask_about_headache,
                                 ask_about_hemorrhagic_dyscrasia,
                                 ask_about_itch, ask_about_joint_pain,
                                 ask_about_melasma, ask_about_muscle_pain,
                                 ask_about_neurological_damage,
                                 initial_questionary)
from rules import all_rules
from utils import (get_consultation_section_title, inform_diagnosis,
                   wait_any_key_press)


def run_system():
    aedes_aegypti_diagnosis = control.ControlSystem(all_rules)
    medical_record = control.ControlSystemSimulation(aedes_aegypti_diagnosis)

    questions_to_ask = [
        ('febre', ask_about_fever),
        ('manchas na pele', ask_about_melasma),
        ('dor nos músculos', ask_about_muscle_pain),
        ('dor nas juntas', ask_about_joint_pain),
        ('conjuntivite', ask_about_conjuctivitis),
        ('dor de cabeça', ask_about_headache),
        ('coceira', ask_about_itch),
        ('inchaço na região do pescoço', ask_about_ganglionic_hypertrophy),
        ('sangramento espontâneo', ask_about_hemorrhagic_dyscrasia),
        ('sequelas neurológica', ask_about_neurological_damage),
    ]

    patient, medical_record = initial_questionary(medical_record)

    for section, questions in questions_to_ask:
        get_consultation_section_title(patient, section)

        medical_record = questions(medical_record, section)

        wait_any_key_press()

    medical_record.compute()

    inform_diagnosis(medical_record.output['diagnosis'])


if __name__ == '__main__':
    run_system()
