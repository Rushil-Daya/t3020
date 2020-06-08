import unittest
import datamunger

class TestDatamunger(unittest.TestCase) :

    def test_calcTotal(self):
        arrayTemp= [10,9,8,7,6,5,4,3,2]     #create a temporary array which represents a link from the .csv file
        total=44                               #this is the correct total (adding T1 throught T8)
        cal = datamunger.calc_total(arrayTemp)
        self.assertEqual(cal,total)

    def test_checkRow(self):
        arrTemp= [10,9,7,6,4,3,2]
        self.assertEqual(datamunger.check_row(1,[],arrTemp), False)

    


if __name__ == "__main__":
    unittest.main()
