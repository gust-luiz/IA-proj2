from skfuzzy import control

from src.rules import get_headache_rules
from .class_test import ReferenceDiagnosisTest
from src.consequents import get_headache_consequent


class TestMelasmaDiagnosis(ReferenceDiagnosisTest):
    output = get_headache_consequent()

    def setUp(self):
        aedes_aegypti_diagnosis = control.ControlSystem(get_headache_rules())
        self.medical_record = control.ControlSystemSimulation(aedes_aegypti_diagnosis)

    def test_should_be_dengue(self):
        self.medical_record.input['headache_frequency'] = 10
        self.medical_record.input['headache_intensity'] = 10

        best_diagonis = self._get_best_diagnosis()
        print('d', self._get_diagnosis())
        print('dvalue', self.medical_record.output[self.common_consequent_name])

        self.assertEqual(best_diagonis[0], 'Dengue')


    def test_should_be_zika(self):
        self.medical_record.input['headache_frequency'] = 5
        self.medical_record.input['headache_intensity'] = 5

        best_diagonis = self._get_best_diagnosis()
        print('z', self._get_diagnosis())

        self.assertEqual(best_diagonis[0], 'Zika')

    def test_should_be_chikungunya(self):
        self.medical_record.input['headache_frequency'] = 0
        self.medical_record.input['headache_intensity'] = 0

        best_diagonis = self._get_best_diagnosis()
        print('c', self._get_diagnosis())


        self.assertEqual(best_diagonis[0], 'Chikungunya')


