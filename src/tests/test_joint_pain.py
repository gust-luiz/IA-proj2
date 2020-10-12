from skfuzzy import control

from src.rules import get_joint_pain_rules
from .class_test import ReferenceDiagnosisTest
from src.consequents import get_joint_pain_consequent


class TestJointPainDiagnosis(ReferenceDiagnosisTest):
    output = get_joint_pain_consequent()

    def setUp(self):
        aedes_aegypti_diagnosis = control.ControlSystem(get_joint_pain_rules())
        self.medical_record = control.ControlSystemSimulation(aedes_aegypti_diagnosis)

    def test_should_be_dengue(self):
        self.medical_record.input['joint_pain_freq'] = 2
        self.medical_record.input['joint_pain_intensity'] = 1
        self.medical_record.input['joint_edema'] = 0
        self.medical_record.input['joint_edema_intensity'] = 0

        best_diagonis = self._get_best_diagnosis()

        self.assertEqual(best_diagonis[0], 'Dengue')
        self.assertGreaterEqual(best_diagonis[1], self.FOR_SURE_LEVEL)

    def test_should_be_zika(self):
        self.medical_record.input['joint_pain_freq'] = 5
        self.medical_record.input['joint_pain_intensity'] = 4
        self.medical_record.input['joint_edema'] = 8
        self.medical_record.input['joint_edema_intensity'] = 1

        best_diagonis = self._get_best_diagnosis()

        self.assertEqual(best_diagonis[0], 'Zika')
        self.assertGreaterEqual(best_diagonis[1], self.FOR_SURE_LEVEL)

    def test_should_be_chikungunya(self):
        self.medical_record.input['joint_pain_freq'] = 8
        self.medical_record.input['joint_pain_intensity'] = 8
        self.medical_record.input['joint_edema'] = 8
        self.medical_record.input['joint_edema_intensity'] = 6

        best_diagonis = self._get_best_diagnosis()

        self.assertEqual(best_diagonis[0], 'Chikungunya')
        self.assertGreaterEqual(best_diagonis[1], self.FOR_SURE_LEVEL)
