# EcoCity
## _Information-analytical system for assessing the state of atmospheric air_

This software has:
- Collection of data from open platforms(KMDA)
- Construction of analytical graphs
- Response system in case of critical conditions

## Installation

EcoCity requires [Python](https://www.python.org/)v3.10+, [Postgres](https://www.postgresql.org/), [Redis](https://redis.io/) to run.
Install the dependencies. Prepare .env file and start the server.

```sh
pip install -r requirements.txt
python manage.py runserver
```

.env for example...
```sh
DEBUG=True

DB_HOST=localhost
DB_PORT=5432
DB_USER=user
DB_PASSWORD=user_pass
DB_NAME=db_name

REDIS_DB=0
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_USER=redis_user
REDIS_PASSWORD=pedis_pass
REDIS_PROTOCOL=redis

CORS_ALLOW_ALL_ORIGINS=False
ALLOWED_ORIGIN_WEB=http://localhost:8000
TRUSTED_ORIGIN_WEB=http://localhost:8000
```



## Docker for rapid deployment

Dillinger is very easy to install and deploy in a Docker container.

To launch the project

```sh
docker-compose -d up --build
```

Stop the entire project
```sh
docker-compose down
```

## License

MIT

**Free Software, Hell Yeah!**