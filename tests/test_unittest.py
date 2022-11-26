import unittest
from unittest.mock import patch
from Tests.func_secretary import documents, directories, get_doc_owner_name, \
    get_all_doc_owners_names, get_doc_shelf, add_new_doc, delete_doc, \
    move_doc_to_shelf, add_new_shelf


class TestFunctions(unittest.TestCase):

    def test_get_doc_owner_name(self):
        with unittest.mock.patch('builtins.input',
                                 return_value=documents[0]["number"]):
            self.assertEqual(get_doc_owner_name(), documents[0]["name"])
        with unittest.mock.patch('builtins.input',
                                 return_value='InvalidDocNumber'):
            self.assertIsNone(get_doc_owner_name())

    def test_get_all_doc_owners_names(self):
        result = get_all_doc_owners_names()
        names = []
        for doc in documents:
            names.append(doc['name'])
        self.assertEqual(result, set(names))

    def test_get_doc_shelf(self):
        with unittest.mock.patch('builtins.input',
                                 return_value='10006'):
            self.assertEqual(get_doc_shelf(), '2')
        with unittest.mock.patch('builtins.input',
                                 return_value='InvalidDocNumber'):
            self.assertIsNone(get_doc_shelf())

    def test_add_new_doc(self):
        with patch('builtins.input', side_effect=['3333', 'passport',
                                                  'Иванов Иван', '3']):
            add_new_doc()
            self.assertIn('3333', documents[3]['number'])
            self.assertIn('passport', documents[3]['type'])
            self.assertIn('Иванов Иван', documents[3]['name'])
            with unittest.mock.patch('builtins.input', return_value='3333'):
                self.assertEqual(get_doc_shelf(), '3')

    def test_delete_doc(self):
        with unittest.mock.patch('builtins.input',
                                 return_value='11-2'):
            delete_doc()
            self.assertNotIn('11-2', documents[1]['number'])
            self.assertNotIn('invoice', documents[1]['type'])
            self.assertNotIn('Геннадий Покемонов', documents[1]['name'])
            self.assertNotIn('11-2', directories['1'])

    def test_move_doc_to_shelf(self):
        with patch('builtins.input', side_effect=['10006', '3']):
            move_doc_to_shelf()
            self.assertNotIn('10006', directories['2'])
            self.assertIn('10006', directories['3'])

    def test_add_new_shelf(self):
        with patch('builtins.input', side_effect='4'):
            add_new_shelf()
            self.assertIn('4', directories)
        with unittest.mock.patch('builtins.input', return_value='2'):
            self.assertFalse(get_doc_shelf())














