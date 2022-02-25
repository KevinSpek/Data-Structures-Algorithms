
import unittest    
from graphs.DFS import dfs_adj_matrix



class TestGraphs(unittest.TestCase):    
    def test_dfs_adj_matrix_1(self):
        matrix_graph = [
            [0,0,1,0,0,0,1],
            [1,0,1,0,0,0,0],
            [0,1,0,0,1,0,0],
            [1,0,1,0,0,0,0],
            [0,0,1,1,1,1,0],
            [1,0,0,0,0,1,0],
            [0,1,0,0,1,0,0]
          ]
        
        self.assertEqual(dfs_adj_matrix(matrix_graph, 0, 5), [0, 6, 4, 5])
      
    def test_dfs_adj_matrix_2(self):
        matrix_graph = [
            []
          ]
        
        self.assertEqual(dfs_adj_matrix(matrix_graph, 0, 0), None)
      
            
    def test_dfs_adj_matrix_3(self):
        matrix_graph = [
            [0, 0],
            [0, 0]
          ]
        
        self.assertEqual(dfs_adj_matrix(matrix_graph, 0, 1), None)
    def test_dfs_adj_matrix_3(self):
        matrix_graph = [
            [0,1,0],
            [0,0,1],
            [1,0,0]
          ]
        self.assertEqual(dfs_adj_matrix(matrix_graph, 0, 2), [0, 1, 2])
      

        
if __name__ == '__main__':
    unittest.main()
