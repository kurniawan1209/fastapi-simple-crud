# FastAPI Simple CRUD

The code in this repository is an example of how to create CRUD operations using FastAPI, Alembic, and PostgreSQL as its database.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.


### Prerequisites

First, install python on your machine. In this code I use python 3.8.5 (https://www.python.org/downloads/). After python installed, then create a environment inside the project folder. You can run this command on your terminal to create it.

``` bash
python -m venv venv
```

Afterwards, you need to activate the environment first before installing the required packages to run this application. You can activate the environment by entering this command to your terminal.

``` bash
venv\Scripts\activate.bat
```

And then install the packages are used. There is so many package are used such like fastapi for sure, alembic as a database migration management, and the psycopg2 to become the driver to postgresql database.

``` bash
pip install -r requirements.txt
```

the next step is to be continued :)