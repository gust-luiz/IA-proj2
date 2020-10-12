from skfuzzy import control

from src.rules import get_fever_rules
from .class_test import ReferenceDiagnosisTest
from src.consequents import get_fever_consequent

class TestFeverDiagnosis(ReferenceDiagnosisTest):
    output = get_fever_consequent()

    def setUp(self):
        aedes_aegypti_diagnosis = control.ControlSystem(get_fever_rules())
        self.medical_record = control.ControlSystemSimulation(aedes_aegypti_diagnosis)

    def test_should_be_dengue(self):
        self.medical_record.input['body_temperature'] = 40.1
        self.medical_record.input['fever_duration'] = 7

        best_diagonis = self._get_best_diagnosis()
        print('d', self._get_diagnosis())

        self.assertEqual(best_diagonis[0], 'Dengue')

    def test_should_be_zika(self):
        self.medical_record.input['body_temperature'] = 35.7
        self.medical_record.input['fever_duration'] = 1

        best_diagonis = self._get_best_diagnosis()
        print('z', self._get_diagnosis())

        self.assertEqual(best_diagonis[0], 'Zika')

    def test_should_be_chikungunya(self):
        self.medical_record.input['body_temperature'] = 39.7
        self.medical_record.input['fever_duration'] = 3

        best_diagonis = self._get_best_diagnosis()
        print('c', self._get_diagnosis())

        self.assertEqual(best_diagonis[0], 'Chikungunya')
