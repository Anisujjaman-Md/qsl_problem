# QSL Problem_1

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)

## Requirements

- Python 3.12
- Django 5.0
- Postgres 16

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Anisujjaman-Md/qsl_problem.git
    cd problem_1
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - For Windows:

        ```bash
        venv\Scripts\activate
        ```

    - For macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Apply migrations:

    ```bash
    python manage.py migrate
    ```

## Configuration

1. Configure Database

    ```env
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'qsl',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
   }
    ```

2. Update the `config/settings.py` file with your configuration.

## Usage

Run the development server:

```bash
python manage.py runserver
```

## API Endpoints

``` 
    Registration: POST /api/register/
    Login: POST /api/login/
```


# QSL Problem_2

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)

## Requirements

- Python 3.12

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Anisujjaman-Md/qsl_problem.git
    cd problem_2
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - For Windows:

        ```bash
        venv\Scripts\activate
        ```

    - For macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage
Run script:

```bash
python tsp.py
```