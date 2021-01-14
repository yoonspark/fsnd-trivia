import os
import sys
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category


QUESTIONS_PER_PAGE = 10


def paginate_questions(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [q.format() for q in selection]
    current_questions = questions[start:end]

    return current_questions


def create_app(test_config=None):
    # Create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)


    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type,Authorization,true'
        )
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET,PUT,POST,DELETE,OPTIONS'
        )

        return response


    @app.route('/categories')
    def retrieve_categories():
        categories = Category.query.order_by(Category.type).all()

        if len(categories) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'categories': {c.id: c.type for c in categories}
        })


    @app.route('/questions')
    def retrieve_questions():
        categories = Category.query.order_by(Category.type).all()
        questions = Question.query.order_by(Question.id).all()
        current_questions = paginate_questions(request, questions)

        if len(categories) == 0 or len(current_questions) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'categories': {c.id: c.type for c in categories},
            'questions': current_questions,
            'total_questions': len(questions),
        })


    @app.route('/categories/<int:category_id>/questions')
    def retrieve_questions_by_category(category_id):
        questions = Question.query.filter(
            Question.category == category_id
        ).all()
        current_questions = paginate_questions(request, questions)

        if len(current_questions) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'current_category': category_id,
            'questions': current_questions,
            'total_questions': len(questions),
        })


    @app.route('/questions/search', methods=['POST'])
    def search_questions():
        body = request.get_json()
        if body:
            search_term = body.get('searchTerm', '')
        else:
            abort(400)

        questions = Question.query.filter(
            Question.question.ilike("%{}%".format(search_term))
        ).all()

        current_questions = paginate_questions(request, questions)

        return jsonify({
            'success': True,
            'questions': current_questions,
            'total_questions': len(questions),
        })


    @app.route('/questions', methods=['POST'])
    def create_questions():
        body = request.get_json()
        if body:
            q = Question(
                question = body.get('question', ''),
                answer = body.get('answer', ''),
                difficulty = body.get('difficulty', 1),
                category = body.get('category', 1)
            )
        else:
            abort(400)
        if q.question == '' or q.answer == '':
            abort(422)

        try:
            q.insert()
            qid = q.id
        except:
            print(sys.exc_info())
            abort(422)

        return jsonify({
            'success': True,
            'message': 'question created',
            'id': qid,
        }), 201


    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        q = Question.query.get(question_id)
        if not q:
            abort(404)
        qid = q.id

        try:
            q.delete()
        except:
            print(sys.exc_info())
            abort(422)

        return jsonify({
            'success': True,
            'message': 'question deleted',
            'id': qid,
        })


    @app.route('/quizzes', methods=['POST'])
    def draw_next_question():
        body = request.get_json()
        if body:
            previous_questions = body.get('previous_questions', [])
            quiz_category = body.get('quiz_category', {})
        else:
            abort(400)

        if quiz_category:
            category_id = quiz_category.get('id')
        else:
            abort(400)

        # Randomly draw an unplayed question
        candidate_questions = Question.query.filter(
            Question.category == category_id,
            ~Question.id.in_(previous_questions),
        ).all()
        if not candidate_questions:
            abort(404)
        next_question = random.choice(candidate_questions)

        return jsonify({
            'success': True,
            'question': next_question.format(), # Serialize
        })


    @app.errorhandler(400)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request",
        }), 400


    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found",
        }), 404


    @app.errorhandler(422)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'unprocessable entity',
        }), 422


    return app
