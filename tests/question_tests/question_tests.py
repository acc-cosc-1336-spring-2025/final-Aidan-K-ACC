#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config
#from src.question_b.question_b import
#from src.question_c.question_c import 
from src.question_d.question_d import table

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())
    def test_question_b_config(self):
        self.assertEqual(True, test_config())
    def test_question_c_config(self):
        self.assertEqual(True, test_config())
    def test_question_d_config(self):
        self.assertEqual(table([1,2,3],[1,2,3]),'1 2 3 \n2 4 6 \n3 6 9 \n')
        self.assertEqual(table([1,2,3],[1]),'1 2 3 \n')

