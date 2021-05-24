import unittest
from pprint import pprint
import copy
from virus.virus import *

def convert_field(field_string):
    return [list(field_string.split('\n')[j]) for j in range(10)]

def convert_dist(field):
    ret = []
    for i in field:
        ret.append([])
        for j in i:
            if j == float('inf'):
                ret[-1].append('u')
            else:
                ret[-1].append(str(j))
    return ret

class CalcDistanceTest(unittest.TestCase):


    def test_empty(self):
        with open("tests/fields/empty_field") as f, open("tests/fields/empty_field_ans_dist") as ans:
            vir = AggressiveVirus(convert_field(f.read()), '1')
            self.assertEqual(convert_dist(vir.distances), convert_field(ans.read()))
        
    def test_first_o_turn_triangular(self):
        with open("tests/fields/first_o_turn_triangular") as f, open("tests/fields/first_o_turn_triangular_ans_dist") as ans:
            vir = AggressiveVirus(convert_field(f.read()), '2')
            self.assertEqual(convert_dist(vir.distances), convert_field(ans.read()))

    def test_advanced_case(self):
        with open("tests/fields/advanced_case") as f, open("tests/fields/advanced_case_ans_dist") as ans:
            vir = AggressiveVirus(convert_field(f.read()), '1')
            self.assertEqual(convert_dist(vir.distances), convert_field(ans.read()))
class MoveTest(unittest.TestCase):
    def test_empty(self):
        with open("tests/fields/empty_field") as f, open("tests/fields/empty_field_ans_move") as ans:
            vir = AggressiveVirus(convert_field(f.read()), '1')
            ans_field = convert_field(ans.read())
            vir.move()
            self.assertEqual(vir.field, ans_field)
            vir.move()
            second_move_case1 = copy.deepcopy(ans_field)
            second_move_case1[8][0] = '1'
            second_move_case2 = copy.deepcopy(ans_field)
            second_move_case2[9][1] = '1'
            second_move_case3 = copy.deepcopy(ans_field)
            second_move_case3[8][1] = '1'
            self.assertTrue(vir.field in [second_move_case1, second_move_case2, second_move_case3])

    def test_first_o_turn_triangular(self):
        with open("tests/fields/first_o_turn_triangular") as f, open("tests/fields/first_o_turn_triangular_ans_move") as ans:
            vir = AggressiveVirus(convert_field(f.read()), '2')
            vir.move()
            self.assertEqual(vir.field, convert_field(ans.read()))

    def test_advanced_case(self):
        with open("tests/fields/advanced_case") as f, open("tests/fields/advanced_case_ans_move") as ans:
            vir = AggressiveVirus(convert_field(f.read()), '1')
            vir.move()
            vir.move()
            vir.move()
            ans_field = convert_field(ans.read())
            self.assertEqual(vir.field, ans_field)

    def test_diagonal_case(self):
        with open("tests/fields/diagonal_case") as f, open("tests/fields/diagonal_case_ans_move") as ans:
            vir = AggressiveVirus(convert_field(f.read()), '1')
            vir.move()
            vir.move()
            vir.move()
            ans_field = convert_field(ans.read())
            self.assertEqual(vir.field, ans_field)


if __name__ == "__main__":
    unittest.main()
