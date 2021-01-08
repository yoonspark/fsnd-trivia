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

*Path Parameters:* None

*Query Parameters:* None

*Request Body:* None

*Example:*
```
$ curl -X GET "http://127.0.0.1:5000/categories"
```

#### RESPONSE

`200`: Returns a dictionary of categories where the key and value are category ID and name, respectively.

*Example:*
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

*Path Parameters:*
- `page` (optional): Page to fetch and render. Defaults to 1.

*Query Parameters:* None

*Request Body:* None

*Example:*
```
$ curl -X GET "http://127.0.0.1:5000/questions?page=2"
```

#### RESPONSE

`200`: Returns a collection of questions in the given page.

*Example:*
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
