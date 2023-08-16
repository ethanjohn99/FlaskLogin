from app import app
from application import * 
import unittest
from flask_testing import TestCase
import unittest
from unittest import mock
from sqlite3 import * 



dbc = mock.MagicMock()

class TestInit(TestCase):
    def create_app(self):
        config_name = 'testing'
        app.config.update(
            WTF_CSRF_ENABLED=False,
            DEBUG=True
            )
        return app

    def setUp(self):
        print("-----------")

    def tearDown(self):
        print("--------")


class Test_insert_rows(TestInit):

    dbc = mock.MagicMock()

    def insert_rows(self, rows, table_name, dbc):
        field_names = rows[0].keys()
        field_names_str = ', '.join(field_names)
        placeholder_str = ','.join('?'*len(field_names))
        insert_sql = f'INSERT INTO {table_name}({field_names_str}) VALUES ({placeholder_str})'
        saved_autocommit = dbc.autocommit
        with dbc.cursor() as cursor:
            try:
                dbc.autocommit = False
                tuples = [ tuple((row[field_name] for field_name in field_names)) for row in rows ]
                cursor.executemany(insert_sql, tuples)
                cursor.commit()
            except Exception as exc:
                cursor.rollback()
                raise exc
            finally:
                dbc.autocommit = saved_autocommit

    
    def fix_dbc(self):
        dbc = mock.MagicMock(spec=['cursor'])
        dbc.autocommit = True
        return dbc

    def fix_rows_a(self):
        rows = [{'id':1,'name':'Platoon'}, 
                {'id':2,'name':'Blazing Saddles'},]
        return rows

    
    def test_insert_rows_calls_cursor_method(self):
        dbc = self.fix_dbc()
        rows = self.fix_rows_a()
        self.insert_rows(rows, 'movies', dbc)
        self.assertTrue(dbc.cursor.called)

    
    def fix_rows_b(self):
        rows = [{'id':1,'rev':'good', 'rating':'7', 'movies_id':'1'}, 
                {'id':2,'rev':'good', 'rating':'7', 'movies_id':'2'},]
        return rows

    
    def test_insert_rows_calls_cursor_method(self):
        dbc = self.fix_dbc()
        rows = self.fix_rows_b()
        self.insert_rows(rows, 'reviews', dbc)
        self.assertTrue(dbc.cursor.called)


class TestDelete(TestInit):

    dbc = mock.MagicMock()

    def insert_rows(self, rows, table_name, dbc):
        field_names = rows[0].keys()
        field_names_str = ', '.join(field_names)
        placeholder_str = ','.join('?'*len(field_names))
        insert_sql = f'DELETE FROM {table_name} WHERE ({field_names_str})=({placeholder_str})'
        saved_autocommit = dbc.autocommit
        with dbc.cursor() as cursor:
            try:
                dbc.autocommit = False
                tuples = [ tuple((row[field_name] for field_name in field_names)) for row in rows ]
                cursor.executemany(insert_sql, tuples)
                cursor.commit()
            except Exception as exc:
                cursor.rollback()
                raise exc
            finally:
                dbc.autocommit = saved_autocommit

    
    def fix_dbc(self):
        dbc = mock.MagicMock(spec=['cursor'])
        dbc.autocommit = True
        return dbc

    def fix_rows_a(self):
        rows = [{'id':1}]
        return rows

    
    def test_insert_rows_calls_cursor_method(self):
        dbc = self.fix_dbc()
        rows = self.fix_rows_a()
        self.insert_rows(rows, 'movies', dbc)
        self.assertTrue(dbc.cursor.called)

    
    def fix_rows_b(self):
        rows = [{'id':1}]
        return rows

    
    def test_insert_rows_calls_cursor_method(self):
        dbc = self.fix_dbc()
        rows = self.fix_rows_b()
        self.insert_rows(rows, 'reviews', dbc)
        self.assertTrue(dbc.cursor.called)


class FlaskTestCase(TestInit):

    num = 1
    id_num = str(num)

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    
    def test_add(self):
        tester = app.test_client(self)
        response = tester.get('/add', content_type='html/text')
        self.assertEqual(response.status_code, 200)


    def test_update(self):
        id_num = self.id_num 
        tester = app.test_client(self)
        response = tester.get(f'/update/{id_num}', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    
    def test_add_review(self):
        id_num = self.id_num
        tester = app.test_client(self)
        response = tester.get(f'/add_review/{id_num}', content_type='html/text')
        self.assertEqual(response.status_code, 200)


    def test_reviews(self):
        id_num = self.id_num
        tester = app.test_client(self)
        response = tester.get(f'/reviews/{id_num}', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    

if __name__ == '__main__':
    unittest.main(argv=['', '-v'])