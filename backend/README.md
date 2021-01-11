# Trivia: Backend

Trivia app’s backend server hosted locally at `http://127.0.0.1:5000/`.

## Getting Started

### Installing Dependendies

The current project repo uses [`poetry`](https://python-poetry.org/docs/) to manage
dependencies among different Python packages, which is essential to reproducibility.
Following are steps for setting up and getting started:

First, ensure you are using the right version of Python (`^3.8`). You may want to
use [`pyenv`](https://github.com/pyenv/pyenv) to effectively manage multiple versions
of Python installation. You can then install `poetry`:
```
$ pip install poetry
```

Once you clone the current repo into your local machine, you can go inside the repo and run:
```
$ poetry install
```
to install the right versions of packages for running scripts in the project repo.

To use the new Python configuration that has been installed, you need to run:
```
$ poetry shell
```
which will activate the virtual environment for the project repo.

You can simply type:
```
$ exit
```
to exit from the virtual environment and return to the global (or system) Python installation.

### Setting up the Database

Once the virtual environment is activated, restore the PostgreSQL database to connect and use:
```
$ createdb trivia
$ psql -d trivia -U [username] -a -f trivia.psql
```
where you need to put your system's valid user in `[username]`.

### Running the Server

Finally, you can launch the backend server:
```
$ export FLASK_APP=flaskr
$ export FLASK_ENV=development
$ flask run
```

For successful launch, make sure that the virtual environment has been activated.

### Testing

You can run tests to ensure the API is working as expected:
```
$ createdb trivia_test
$ psql -d trivia_test -U [username] -a -f trivia.psql
$ python test_flaskr.py
```

## API Reference

### `GET` */categories*

Fetch existing categories.

#### REQUEST

- *Path Parameters:* None

- *Query Parameters:* None

- *Request Body:* None

- *Example:*
```
$ curl "http://127.0.0.1:5000/categories"
```

#### RESPONSE

- `200`: Returns a dictionary of categories where the key and value are category ID and name, respectively.

- *Example:*
```
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "success": true
}
```

---

### `GET` */questions*

Fetch existing questions with pagination. Each page contains 10 questions.
If no page is specified, `page=1` is rendered by default.

#### REQUEST

- *Path Parameters:* None

- *Query Parameters:*
    - `page` (optional): Page to fetch and render. Defaults to 1.

- *Request Body:* None

- *Example:*
```
$ curl "http://127.0.0.1:5000/questions?page=2"
```

#### RESPONSE

- `200`: Returns a collection of questions in the given page.

- *Example:*
```
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "questions": [
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "Escher",
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    },
    {
      "answer": "Mona Lisa",
      "category": 2,
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?"
    },
    {
      "answer": "One",
      "category": 2,
      "difficulty": 4,
      "id": 18,
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    },
    {
      "answer": "Jackson Pollock",
      "category": 2,
      "difficulty": 2,
      "id": 19,
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    },
    {
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
    },
    {
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?"
    },
    {
      "answer": "Blood",
      "category": 1,
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?"
    },
    {
      "answer": "Scarab",
      "category": 4,
      "difficulty": 4,
      "id": 23,
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    }
  ],
  "success": true,
  "total_questions": 19
}
```

---

### `GET` */categories/<category_id>/questions*

Fetch questions under a given category.

#### REQUEST

- *Path Parameters:*
    - `category_id`: ID of the category to fetch questions for.

- *Query Parameters:*
    - `page` (optional): Page to fetch and render. Defaults to 1.

- *Request Body:* None

- *Example:*
```
$ curl "http://127.0.0.1:5000/categories/1/questions"
```

#### RESPONSE

- `200`: Returns a collection of questions under the given category.

- *Example:*
```
{
  "current_category": 1,
  "questions": [
    {
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
    },
    {
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?"
    },
    {
      "answer": "Blood",
      "category": 1,
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?"
    }
  ],
  "success": true,
  "total_questions": 3
}
```

---

### `POST` */questions/search*

Search questions that match the provided string.

#### REQUEST

- *Path Parameters:* None

- *Query Parameters:*
    - `page` (optional): Page to fetch and render. Defaults to 1.

- *Request Body:*
    - `searchTerm`: String to match. Defaults to an empty string, which results in all questions being matched and returned.

- *Example:*
```
$ curl "http://127.0.0.1:5000/questions/search" \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"searchTerm": "medicine"}'
```

#### RESPONSE

- `200`: Returns a collection of questions that match the provided string.

- *Example:*
```
{
  "questions": [
    {
      "answer": "Blood",
      "category": 1,
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?"
    }
  ],
  "success": true,
  "total_questions": 1
}
```

---

### `POST` */questions*

Create a new question.

#### REQUEST

- *Path Parameters:* None

- *Query Parameters:* None

- *Request Body:*
    - `question`: Question string.
    - `answer`: Answer string.
    - `difficulty`: Level of difficulty (integer between 1 and 5).
    - `category`: Category ID.

- *Example:*
```
$ curl "http://127.0.0.1:5000/questions" \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{
        "question": "test question",
        "answer": "test answer",
        "difficulty": 3,
        "category": 1
    }'
```

#### RESPONSE

- `201`: Returns success message and ID of the created question.

- *Example:*
```
{
  "id": 24,
  "message": "question created",
  "success": true
}
```

---

### `DELETE` */questions/<question_id>*

Delete an existing question.

#### REQUEST

- *Path Parameters:* None
    - `question_id`: ID of the question to be deleted.

- *Query Parameters:* None

- *Request Body:* None

- *Example:*
```
$ curl "http://127.0.0.1:5000/questions/24" \
    -X DELETE
```

#### RESPONSE

- `200`: Returns success message and ID of the deleted question.

- *Example:*
```
{
  "id": 24,
  "message": "question deleted",
  "success": true
}
```

---

### `POST` */quizzes*

Draw a new question to play.

#### REQUEST

- *Path Parameters:* None

- *Query Parameters:* None

- *Request Body:*
    - `previous_questions`: Array of question IDs that have been already played. Defaults to an empty array.
    - `quiz_category`: Category ID being played. Defaults to null.

- *Example:*
```
$ curl "http://127.0.0.1:5000/quizzes" \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{
        "previous_questions": [16, 17],
        "quiz_category": 2
    }'
```

#### RESPONSE

- `200`: Returns a new question to play.

- *Example:*
```
{
  "question": {
    "answer": "Jackson Pollock",
    "category": 2,
    "difficulty": 2,
    "id": 19,
    "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
  },
  "success": true
}
```
