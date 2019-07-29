import unittest

from task_solver import TaskSolver

class TestTaskSolver(unittest.TestCase):
    def setUp(self):
        self.solver = TaskSolver()

    def test_get_next_id_returns_int_if_number_in_string(self):
        input_string = 'and the next nothing is 45439'
        expected_result = 45439
        self.assertEqual(self.solver.get_id_from_response(input_string), expected_result)

    def test_get_next_id_returns_none_if_number_not_in_string(self):
        input_string = 'and the next nothing is None'
        expected_result = None
        self.assertEqual(self.solver.get_id_from_response(input_string), expected_result)

    def test_url_from_id_returns_valid_url_if_int_is_passed(self):
        url_id = 29891
        expected_url = f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={url_id}'
        self.assertEqual(self.solver.url_from_id(url_id), expected_url)
        
    def test_url_from_id_rases_value_error_if_not_int_passed(self):
        url_id = '29891'
        with self.assertRaises(ValueError):
            self.solver.url_from_id(url_id)

    