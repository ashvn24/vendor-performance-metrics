
# Vendor Management

The Vendor Management System is a Django-based web application that aims to streamline the vendor management process within an organization. It provides a centralized platform for managing vendor profiles, tracking purchase orders, and evaluating vendor performance through various metrics. 

## Documentation

[Post-man API documentaion](https://documenter.getpostman.com/view/31561157/2sA3JGeNyy) - This contains the whole documentaion of the api endpoints.


## Features

- Tracking vendor performance metrics like on-time delivery rate, quality rating, response time, and fulfillment rate.
- JWT authentication for securing API endpoints.
- Celery for storing historical vendor performance data.
- Docker containerization for consistent deployment.


## Installation

Run vendor-project with docker

```bash
  docker-compose up --build
```


## Run Locally

Clone the project

```bash
  git clone https://github.com/ashvn24/vendor-performance-metrics.git
```


Install dependencies

```bash
  pip install requirements.txt
```

Start the server

```bash
  python manage.py runserver
```

Start Celery worker

```bash
    celery -A vendor.celery worker --pool=solo -l info
```

if running locally make sure to replace the HOST of postgreSQL Database in settings.py to the below mentioned

```bash
"HOST": "localhost",
```
## Run Test
To run the test cases added at test.py follow the bellow command
```bash
  python manage.py test
```
## Tech Stack

**Client:** PostMan

**Server:** Django REST, Celery, JWT, Docker

