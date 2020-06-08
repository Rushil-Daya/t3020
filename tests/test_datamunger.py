import unittest
import datamunger

class TestDatamunger(unittest.TestCase) :

    def test_calcTotal(self):
        arrayTemp= [10,9,8,7,6,5,4,3,2]
        total=44
        cal = datamunger.calc_total(arrayTemp)
        self.assertEqual(cal,total)

    


if __name__ == "__main__":
    unittest.main()