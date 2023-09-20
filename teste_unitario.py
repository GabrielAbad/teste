import unittest
from distancia_datas import *
class TestDateDistanceFunc(unittest.TestCase):
    def testExampleConsistency(self):
        #>>> calcula_datas(["31", "Agosto","2022"], ["18", "Setembro", "2023"])
        #Saida (na documentacao) : 383
        int_output = calcula_datas(['01','Agosto','2022'],['18','Setembro','2023'])
        int_expected = 383
        self.assertEqual(int_output,int_expected)
    def testKnownValue(self):
        int_output = calcula_datas(['01','01','2003'],['01','01','2004'])
        int_expected = 365
        self.assertEqual(int_output,int_expected)
    def testZeroValue(self):
        int_output = calcula_datas(['01','01','2003'],['01','01','2003'])
        int_expected = 0
        self.assertEqual(int_output,int_expected)
    def testPastDate(self):
        int_output = calcula_datas(["18", "09", "2023"],["31", "08","2022"])
        int_expected = 383
        self.assertEqual(int_output,int_expected)
    def nanDate(self):
        int_output = calcula_datas(["", "", ""],["", "",""])
        self.assertIsInstance(int_output,Exception)
if name == '__main__':
    unittest.main()