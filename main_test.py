import unittest

from main import assess_skin, assess_eyes, save_new_diagnosis, patients_and_diagnosis

var = patients_and_diagnosis == [
    "Mike - Severe dehydration",
    "Sally - No dehydration",
    "Kate - Some dehydration"
]


class TestMain(unittest.TestCase):
    def test_assess_skin(self):
        self.assertEqual(assess_skin("1"), "No Irritation", "No Irritation")
        self.assertEqual(assess_skin("2"), "Severe Irritation", "Severe Irritation")
        self.assertEqual(assess_skin(""), "", "")

    def test_assess_eyes(self):
        self.assertEqual(assess_eyes("1"), "No dehydration", "No dehydration")
        self.assertEqual(assess_eyes("2"), "Severe dehydration", "Severe dehydration")
        self.assertEqual(assess_eyes(""), "", "")

    def test_save_new_diagnosis(self):
        no_diagnosis = save_new_diagnosis("", "")
        self.assertEqual(no_diagnosis, patients_and_diagnosis.append(no_diagnosis),
                         patients_and_diagnosis.append(no_diagnosis))

        only_name = save_new_diagnosis("Nimish", "")
        self.assertEqual(only_name, patients_and_diagnosis.append(only_name), patients_and_diagnosis.append(only_name))

        only_diagnosis = save_new_diagnosis("", "No dehydration")
        self.assertEqual(only_diagnosis, patients_and_diagnosis.append(only_diagnosis),
                         patients_and_diagnosis.append(only_diagnosis))

        valid_diagnosis = save_new_diagnosis("Kelly", "Severe dehydration")
        self.assertEqual(valid_diagnosis,
                         patients_and_diagnosis.append(valid_diagnosis),
                         patients_and_diagnosis.append(valid_diagnosis))


if __name__ == '__main__':
    unittest.main()
