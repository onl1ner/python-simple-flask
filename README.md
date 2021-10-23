# Simple flask application

A Flask application with the ability to log in and register a user, create and receive articles written by one or another user.

## Installation

To get started with the application you need to complete following steps:

- Install dependencies:

```shell
$ pip install -r requirements.txt
```

- Create `.env` file in root directory of the project and add there `SECRET_KEY` and `DB_URI` variables:

```
SECRET_KEY=your-secret-key
DB_URI=your-database-uri
```

- Create tables in your database:

```sql
CREATE TABLE USERS(
	id SERIAL PRIMARY KEY,
	login VARCHAR,
	first_name VARCHAR,
	last_name VARCHAR,
	password VARCHAR
);

CREATE TABLE ARTICLES(
	id SERIAL PRIMARY KEY,
	author_id INT REFERENCES USERS(id),
	created_at BIGINT,
	text VARCHAR
)
```

- Run application:

```shell
$ python3 src/app.py
```

## Usage

The application consists of two modules:

- Auth - authorization module, which responsible for user registration and token generation.
- Article - article module, which responsible for creating new articles for user and retreiving them.

So in total we have following routes:

- `[POST] /auth/register`
    <details>
    <summary>Body</summary>

    ```js
    {
        login: String,
        first_name: String,
        last_name: String,
        password: String
    }
    ```
    </details>

    <details>
    <summary>Response body</summary>

    ```js
    {
        id: String,
        login: String,
        first_name: String,
        last_name: String
    }
    ```
    </details>

- `[POST] /auth/login`
    <details>
    <summary>Request body</summary>

    ```js
    {
        login: String,
        password: String
    }
    ```
    </details>

    <details>
    <summary>Response body</summary>

    ```js
    {
        access: String
    }
    ```
    </details>

- `[GET] /articles/`
    <details>
    <summary>Query parameters</summary>

    `[OPTIONAL] author_id: String` - parameters used to retrieve articles written by specific author.
    
    </details>

    <details>
    <summary>Response body</summary>

    ```js
    [
        {
            id: Integer,
            author_id: Integer,
            created_at: Integer,
            text: String
        }
    ]
    ```
    </details>

- `[POST] /articles/create`
    <details>
    <summary>Query parameters</summary>

    `[REQUIRED] token: String` - token that is used to create article for specific user.
    
    </details>

    <details>
    <summary>Response body</summary>

    ```js
    {
        id: Integer,
        author_id: Integer,
        created_at: Integer,
        text: String
    }
    ```
    </details>

## Examples

Here is the example of usage:

```shell
$ curl -XGET 'http://localhost:5000/articles/'

[
  {
    "author_id": 1, 
    "created_at": 1634918180, 
    "id": 1, 
    "text": "Lorem ipsum"
  }, 
  {
    "author_id": 1, 
    "created_at": 1634918194, 
    "id": 2, 
    "text": "Lorem ipsum dolor sit amet"
  }, 
  {
    "author_id": 1, 
    "created_at": 1634918209, 
    "id": 3, 
    "text": "Lorem ipsum dolor sit amet"
  }, 
  {
    "author_id": 1, 
    "created_at": 1634918517, 
    "id": 4, 
    "text": "Lorem ipsum dolor sit amet"
  }
]
```
