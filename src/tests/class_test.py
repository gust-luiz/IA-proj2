from unittest import TestCase

from src.utils import order_diagnosis


class ReferenceDiagnosisTest(TestCase):
    def _get_diagnosis(self):
        if not self.medical_record:
            self.skipTest('Attribute "medical_record" should be defined')

        self.medical_record.compute()

        return order_diagnosis(self.medical_record.output['doenças'])

    def _get_best_diagnosis(self):
        return self._get_diagnosis()[0]
