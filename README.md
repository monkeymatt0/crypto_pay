# CryptoPay Gateway

This project is meant to be a gateway to perform transaction on the blockchain of ethereum.
It is for testing basic web3 functionality, the blockchain which we will with interact have 2 configuration:

- DEVELOPMENT_BLOCKCHAIN -> Use Ganache to simulate it
- PRODUCTION_BLOCKCHAIN -> With this one we can go on the mainnet or on a testnet like Sepolia

The entire application is made of BE and FE (not started yet).

The architecture will be REST

## BE

The backend is written in Python3.12.3, it uses djangorestframework with other packages.

To not install all the packages on your global python we will need to create a virtual environment.
We can achieve this by using this command on terminal:

```
python3 -m venv <your_env_name>
```

So for example if I run:

```
python3 -m venv env
```

This will create a virtual environment called **env**.

After we have created the virtual environment we need to activate it, to do that
we can use this from command line:

```
source <your_env_name>/bin/activate
```

Of course you need to stay in the root folder of the project where the **env** folder is.
For env folder I mean the name that has been given to the environment.

### Upgrade pip

A thing that I always do before install the requirements is to upgrade pip by following these steps:

1. Activate the environment

```
source env/bin/activate
```

2. Running the command to upgrade pip:

```
python -m pip install --upgrade pip
```

This will upgrade the pip version.

### Intalling packages

If everything went well then the only thing remained is to call from command line:

```
pip install -r requirements.txt
```

This will automatically install all the dependency needed for the project to work properly

### BE - Purpose

The purpose of the backend is really simple, store the transactions' details:

- transaction hash
- sender address
- receiver address
- amount
- status
- timestamp

Of course it will handle also more basic feature like Login, Register and other.

## BE - Celery, Django Celery Beat

When we will create a transaction on the blockchain we will store a record inside the database.
This transaction will not be received instantly but instead will require a bit of time.

So we need a worker that periodically check the status of the transaction the are still pending.
This worker is then divided in 3 phases:

1. Fetch all pending transaction from DB
2. Contact the blockchain to check what is the status
3. Update the status of the transaction on the DB

### Settings

Once you have installed celery and django celery beat you have to run the migration to make celery works properly:

```
python manage.py migrate django_celery_beat
```

Of course the DB needs to be started before run this command.

Celery works with redis or also rabbitMQ in this case we will use redis.
For this reason we need to also start redis and set a couple of env variable (example of env var will be given after for now look at env.example file)

To properly set the worker we have to make a couple of steps:

1. call:

```
python manage.py <name of your task creator>
```

At this point you have created the task a written in your DB all the data needed to make worker works properly
Example:
my task creator name is "task_creator" => Is setted to run every 5 minutes
then the command will look like this:

```
python manage.py task_creator
```

2. Start celery and django celery beat:

```
celery -A <your_project_name> worker --beat --loglevel=info
```

TODO: Exmplain how to run a blockchain with ganache on local container or machine.
