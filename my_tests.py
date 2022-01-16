import unittest
from main import get_name, get_shelf, del_doc, add_doc, get_doc_info
from ya import YaUpLoader

with open('toc_ya.txt') as f:
    token_ya = f.read().strip()


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('Начало тестов.')

    def setUp(self) -> None:
        self.ya = YaUpLoader(token_ya)
        self.docs = [
            {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
            {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
            {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
        ]
        self.dirs = {
            '1': ['2207 876234', '11-2'],
            '2': ['10006'],
            '3': []
        }

    def test_get_name(self):
        self.assertEqual(get_name('11-2', documents=self.docs), 'Геннадий Покемонов')

    def test_get_name_two(self):
        self.assertEqual(get_name('10006', documents=self.docs), 'Аристарх Павлов')

    def test_get_shelf(self):
        self.assertEqual(get_shelf('11-2', directories=self.dirs), '1')

    def test_get_doc_info(self):
        self.assertEqual(get_doc_info(documents=self.docs),
                         'passport 2207 876234 Василий Гупкин\ninvoice 11-2 Геннадий Покемонов\n'
                         'insurance 10006 Аристарх Павлов')

    def test_add_doc(self):
        test_dict = {"type": "passport", "number": "144531", "name": "Джон Уик"}
        self.assertIn(str(test_dict),
                      add_doc('2', 'passport', '144531', 'Джон Уик', documents=self.docs, directories=self.dirs))

    def test_add_doc_negative(self):
        res = 'Такой полки не существует.'
        self.assertEqual(add_doc('7', 'passport', '144531', 'Джон Уик', documents=self.docs, directories=self.dirs),
                         res)

    def test_del_doc(self):
        self.assertIn('10006', del_doc('10006', documents=self.docs, directories=self.dirs))

    def test_del_doc_negative(self):
        res = 'Документ с указанным Вами номером не существует.'
        self.assertEqual(del_doc('76868444', documents=self.docs, directories=self.dirs), res)

    @classmethod
    def tearDownClass(cls) -> None:
        print('Завершение тестов.')

    def test_create_dir(self):
        self.assertEqual(201, self.ya.create_dir())
        self.assertIn('Файлы', self.ya.get_list_files())

    def test_create_dir_access_ban(self):
        self.assertEqual(401, self.ya.create_dir())


if __name__ == '__main__':
    unittest.main()
