import unittest
import datamunger

#from datamunger.datamunger import *

class TestDatamunger(unittest.TestCase) :

    def test_calcTotal(self):
        arrayTemp = [0,1,2,3,4,5,6,7,8,9]   #create a temporary array which represents a line from the .csv file
        total=36                              #this is the correct total (adding T1 throught T8)
        cal = datamunger.calc_total(arrayTemp)
        self.assertEqual(cal,total)

    def test_checkRow(self):
        arrTemp= [10,9,7,6,4,3,2]    #create a temporary array with missing values
        # use this array with missing values and if the original code works it should return false
        result = datamunger.check_row(1,[],arrTemp)
        self.assertEqual(result,False)

    


if __name__ == "__main__":
	unittest.main()
