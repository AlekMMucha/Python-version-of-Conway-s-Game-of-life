import unittest
from src.main import create_matrix
from src.cell import Cell

# class TestCreateMatrix(unittest.TestCase):
#     def test_create_matrix(self):
        # width,height = 5,5
        # matrix = create_matrix(width,height)
        # self.assertEqual(len(matrix), height)
        # print(f"\nTEST PRINT OF MATRIX: ({width}x{height})")
        # for row in matrix:
        #     print([item.index for item in row])
        # for row in matrix:
        #     print([item.state for item in row])
        # self.assertEqual(matrix[-1][-1].index, (height-1,width-1))

        ###will have to fix after altering function to take in window and list of row frames###