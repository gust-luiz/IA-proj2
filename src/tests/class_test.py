from unittest import TestCase

from src.utils import order_diagnosis


class ReferenceDiagnosisTest(TestCase):
    FOR_SURE_LEVEL = 60
    output_name = None
    output = None

    def _get_diagnosis(self):
        if not self.medical_record:
            self.skipTest('Attribute "medical_record" should be defined')

        if not self.output:
            self.skipTest('Should have a "output" set')

        self.medical_record.compute()

        return order_diagnosis(self.output, self.medical_record.output[self.output_name])

    def _get_best_diagnosis(self):
        return self._get_diagnosis()[0]
