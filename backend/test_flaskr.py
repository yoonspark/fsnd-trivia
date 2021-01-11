import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    def setUp(self):
        """Define test variables and initialize app"""

        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # Bind the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_retrieve_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsInstance(data['categories'], dict)
        self.assertEqual(len(data['categories']), 6)

    # --- VIEW QUESTIONS --- #

    def test_retrieve_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsInstance(data['categories'], dict)
        self.assertIsInstance(data['questions'], list)
        self.assertIsInstance(data['total_questions'], int)
        self.assertEqual(len(data['categories']), 6)
        self.assertEqual(len(data['questions']), 10)

    def test_paginate_beyond_valid_page(self):
        res = self.client().get('/questions?page=100')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_retrieve_questions_by_category(self):
        res = self.client().get('/categories/1/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsInstance(data['current_category'], int)
        self.assertIsInstance(data['questions'], list)
        self.assertIsInstance(data['total_questions'], int)
        self.assertEqual(data['current_category'], 1)
        # self.assertEqual(len(data['questions']), 10)

    # --- SEARCH QUESTIONS --- #

    def test_search_questions(self):
        res = self.client().post('/questions/search', json={'searchTerm': 'medicine'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsInstance(data['questions'], list)
        self.assertIsInstance(data['total_questions'], int)
        self.assertEqual(len(data['questions']), 1)

    def test_search_questions_no_match(self):
        res = self.client().post('/questions/search', json={'searchTerm': '한국'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsInstance(data['questions'], list)
        self.assertIsInstance(data['total_questions'], int)
        self.assertEqual(len(data['questions']), 0)

    def test_search_questions_no_args_passed(self):
        res = self.client().post('/questions/search')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request')

    # --- CREATE QUESTION --- #

    def test_create_question(self):
        res = self.client().post('/questions', json={
            'question': 'test question',
            'answer': 'test answer',
            'difficulty': 3,
            'category': 1,
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 201)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], 'question created')
        self.assertIsInstance(data['created_id'], int)

    def test_create_question_empty_question(self):
        res = self.client().post('/questions', json={
            'question': '',
            'answer': 'test answer',
            'difficulty': 3,
            'category': 1,
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable entity')

    def test_create_question_empty_answer(self):
        res = self.client().post('/questions', json={
            'question': 'test question',
            'answer': '',
            'difficulty': 3,
            'category': 1,
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable entity')

    def test_create_question_no_args_passed(self):
        res = self.client().post('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
