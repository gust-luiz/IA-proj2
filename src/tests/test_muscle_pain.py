from skfuzzy import control

from src.rules import get_muscle_pain_rules
from .class_test import ReferenceDiagnosisTest
from src.consequents import get_muscle_pain_consequent


class TestMelasmaDiagnosis(ReferenceDiagnosisTest):
    output = get_muscle_pain_consequent()

    def setUp(self):
        aedes_aegypti_diagnosis = control.ControlSystem(get_muscle_pain_rules())
        self.medical_record = control.ControlSystemSimulation(aedes_aegypti_diagnosis)

    def test_should_be_dengue(self):
        self.medical_record.input['muscle_pain_frequency'] = 10

        best_diagonis = self._get_best_diagnosis()
        print('d', self._get_diagnosis())
        print('dvalue', self.medical_record.output[self.common_consequent_name])

        self.assertEqual(best_diagonis[0], 'Dengue')


    def test_should_be_zika(self):
        self.medical_record.input['muscle_pain_frequency'] = 5

        best_diagonis = self._get_best_diagnosis()
        print('z', self._get_diagnosis())

        self.assertEqual(best_diagonis[0], 'Zika')

    def test_should_be_chikungunya(self):
        self.medical_record.input['muscle_pain_frequency'] = 1

        best_diagonis = self._get_best_diagnosis()
        print('c', self._get_diagnosis())


        self.assertEqual(best_diagonis[0], 'Chikungunya')


