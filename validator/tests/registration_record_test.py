import unittest

from validator.validator import Validator


__author__ = 'Borja'


class REGValidationTest(unittest.TestCase):
    def setUp(self):
        self._validator = Validator()

    def test_null(self):
        self.assertFalse(self._validator.validate_registration_record(None))

    def test_empty(self):
        self.assertFalse(self._validator.validate_registration_record(''))

    def test_file(self):
        with open('files/CW1328EMI_059.V21') as cwr_file:
            file_content = cwr_file.readlines()

        for line in file_content:
            if line[0:0 + 3] == 'NWR' or line[0:0 + 3] == 'REV':
                self.assertTrue(self._validator.validate_registration_record(line))