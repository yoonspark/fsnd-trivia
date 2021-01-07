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

### `GET` /categories

Fetch existing categories.

#### Parameters

None.

**Sample: Request Body**

```
```

#### Returns

A dictionary of categories where the key and value are category ID and name, respectively.

**Sample: Response**

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
