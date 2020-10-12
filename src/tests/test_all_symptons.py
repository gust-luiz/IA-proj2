from skfuzzy import control

from src.rules import all_rules
from .class_test import ReferenceDiagnosisTest
from src.consequents import get_fever_consequent

class TestFeverDiagnosis(ReferenceDiagnosisTest):
    output = get_fever_consequent()

    def setUp(self):
        aedes_aegypti_diagnosis = control.ControlSystem(all_rules)
        self.medical_record = control.ControlSystemSimulation(aedes_aegypti_diagnosis)

    def test_should_be_dengue(self):
        # fever
        self.medical_record.input['body_temperature'] = 40.1
        self.medical_record.input['fever_duration'] = 7

        self.medical_record.input['melasma'] = 3.5

        self.medical_record.input['muscle_pain_frequency'] = 10

        # joint pain
        self.medical_record.input['joint_pain_freq'] = 1
        self.medical_record.input['joint_pain_intensity'] = 1
        self.medical_record.input['joint_edema'] = 1
        self.medical_record.input['joint_edema_intensity'] = 1

        self.medical_record.input['conjunctivitis'] = 0

        self.medical_record.input['headache_frequency'] = 9
        self.medical_record.input['headache_intensity'] = 9

        self.medical_record.input['itch_intensity'] = 1

        self.medical_record.input['ganglionic_hypertrophy_frequency'] = 1

        self.medical_record.input['hemorrhagic_dyscrasia_frequency'] = 9

        self.medical_record.input['neurological_damage'] = 1
        self.medical_record.input['neurological_damage_newborn'] = 0

        best_diagonis = self._get_best_diagnosis()

        print(self._get_diagnosis())

        self.assertEqual(best_diagonis[0], 'Dengue')
        self.assertGreaterEqual(best_diagonis[1], self.FOR_SURE_LEVEL)
