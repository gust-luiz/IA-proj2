from skfuzzy import control

from src.rules import get_fever_rules
from .class_test import ReferenceDiagnosisTest
from src.consequents import disease

class TestFeverDiagnosis(ReferenceDiagnosisTest):
    output = disease
    output_name = 'doenças'

    def setUp(self):
        aedes_aegypti_diagnosis = control.ControlSystem(get_fever_rules())
        self.medical_record = control.ControlSystemSimulation(aedes_aegypti_diagnosis)

    def test_should_be_dengue(self):
        self.medical_record.input['body_temperature'] = 40.1
        self.medical_record.input['fever_duration'] = 7

        best_diagonis = self._get_best_diagnosis()

        self.assertEqual(best_diagonis[0], 'Dengue')
        self.assertGreaterEqual(best_diagonis[1], self.FOR_SURE_LEVEL)

    def test_should_be_zika(self):
        self.medical_record.input['body_temperature'] = 35.7
        self.medical_record.input['fever_duration'] = 1

        best_diagonis = self._get_best_diagnosis()

        self.assertEqual(best_diagonis[0], 'Zika')
        self.assertGreaterEqual(best_diagonis[1], self.FOR_SURE_LEVEL)

    def test_should_be_chikungunya(self):
        self.medical_record.input['body_temperature'] = 39.7
        self.medical_record.input['fever_duration'] = 3

        best_diagonis = self._get_best_diagnosis()

        self.assertEqual(best_diagonis[0], 'Chikungunya')
        self.assertGreaterEqual(best_diagonis[1], self.FOR_SURE_LEVEL)

    def test_could_be_dengue_or_chikungunya(self):
        self.medical_record.input['body_temperature'] = 38
        self.medical_record.input['fever_duration'] = 4

        expected = {
            'Dengue': (30, self.FOR_SURE_LEVEL),
            'Chikungunya': (30, self.FOR_SURE_LEVEL),
            'Zika': (0, 10),
        }

        with self.subTest():
            for disease, perc in self._get_diagnosis():
                print('disease', disease)
                self.assertGreaterEqual(perc, expected[disease][0])
                self.assertLessEqual(perc, expected[disease][1])
