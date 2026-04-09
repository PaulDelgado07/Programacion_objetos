import unittest

def sumar(a,b):
    return a + b

def espar(numero):
    return numero % 2==0 

class TestSumar(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(sumar(3,2),5)

print("------------------------------------")

class TestPar(unittest.TestCase):
    def Test_es_par_True(self):
        self.assertEqual(espar(4))
    def Test_es_par_false(self):
        self.assertEqual(espar(5))



if __name__ == "__main__":
    unittest.main()