from skfuzzy import control

from src.rules import get_conjunctivitis_rules
from .class_test import ReferenceDiagnosisTest
from src.consequents import get_conjunctivitis_consequent


class TestMelasmaDiagnosis(ReferenceDiagnosisTest):
    output = get_conjunctivitis_consequent()

    def setUp(self):
        aedes_aegypti_diagnosis = control.ControlSystem(get_conjunctivitis_rules())
        self.medical_record = control.ControlSystemSimulation(aedes_aegypti_diagnosis)

    def test_should_be_dengue(self):
        self.medical_record.input['conjunctivitis'] = 0

        best_diagonis = self._get_best_diagnosis()
        print('d', self._get_diagnosis())
        print('dvalue', self.medical_record.output[self.common_consequent_name])

        self.assertEqual(best_diagonis[0], 'Unidentified')

        for disease, value in self._get_diagnosis():
            if disease != 'Dengue':
                continue

            self.assertGreaterEqual(20, value)


    def test_should_be_zika(self):
        self.medical_record.input['conjunctivitis'] = 1

        best_diagonis = self._get_best_diagnosis()
        print('z', self._get_diagnosis())

        self.assertEqual(best_diagonis[0], 'Zika')

    def test_should_be_chikungunya(self):
        self.medical_record.input['conjunctivitis'] = 1

        best_diagonis = self._get_best_diagnosis()
        print('c', self._get_diagnosis())


        self.assertEqual(best_diagonis[0], 'Chikungunya')


