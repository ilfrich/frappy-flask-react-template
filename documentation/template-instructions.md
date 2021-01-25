# Flask + React Project Template

Project template / boilerplate for a micro-service providing endpoints via Flask (Python) and a frontend via React 
(JavaScript).

**Table of Contents**

1. [Requirements](#requirements)
    1. [Tech Stack](#tech-stack)
2. [Installation](#installation)
3. [Running the App](#running-the-app)
    1. [Environment Config](#environment-config)
4. [Customisation](#customisation)

## Requirements

- Python3.6+
- NodeJS / npm
- MongoDB **or** MySQL

### Tech Stack

**Backend**

- **Flask** framework for hosting API endpoints and delivering the frontend
- **pymongo** for MongoDB access
- **mysql-connector-python** for MySQL access

**Frontend**

- **React** basic framework for the frontend
- **Webpack** and **Babel** to transpile the frontend into a single `index.js`, which gets included by the `index.html`
- **Moment.JS** the standard library for date/time handling in JavaScript
- **S Alert** a basic notification library 
- **ESLint** and **Prettier** for linting Javascript code and auto-format

## Installation

You need to create an `.env` file. You can copy the `.env.template` in order to get a base file with a valid 
environment configuration.

First, try to run:

```bash
make install-deps
```

You might have to run it with `sudo`.

That should install the Python (pip) dependencies and Javascript (npm) dependencies.
This assumes, that your Python/Pip binaries are `python3` and `pip3`.

**Manual Installation**

If above doesn't work, install the dependencies separately:

_Javascript:_

```bash
npm install
``` 

_Python:_

```bash
pip install -r requirements.txt
```

## Running the App

If you just want to compile the frontend once and then serve it via the backend (e.g. production mode), simply run:

```bash
npm run build
```

This will produce an index.js containing all the frontend code in the `/static` directory and put the index.html in the 
`/templates` folder. Those 2 directories are used by the Flask app to deliver the frontend components.

The backend's entry point is the script `runner.py` on the root of the project. To run the backend, simply execute:

```bash
make start
```

Again, if your Python binary differs from `python3`, simply run:

```bash
python runner.py
```

(and replace `python` with whatever you use as binary)

- This will serve the Flask app via: http://localhost:5555

**Frontend Development**

The frontend can be continuously re-compiled whenever you change the code.
In a separate bash window, simply run:

```bash
make frontend
```

Or

```bash
npm run hot-client
```

This will run the `webpack` watcher, which will observe the `/frontend/src` folder for changes and re-compile the 
frontend when changes have occurred. 

In case of compilation errors, this bash window will also tell you what is wrong 
with your code. 

_Do not close this window while you're developing, or you quit the watcher._

### Environment Config

As mentioned before, the Flask app is using an `.env` file to load environment variables which specify database access.
Check the `config.py` for all currently supported environment variables.

You can easily extend this and add getters for additional environment configuration and add those to your `.env` file.
Please provide meaningful defaults for all additional config variables (_except 3rd party service credentials_)

## Customisation

The following changes should be performed at the beginning of a project based on this repository:

**Choose a Database**

The boilerplate offers support for 2 different databases: MongoDB and MySQL. The following adaptations are required to 
pick one:

- Update the `requirements.txt` and remove the database driver for the database you don't need.
- Update the `config.py` and remove the environment variables for the database you don't need (they're prefixed with 
`MONGO_` or `MYSQL_`).
- Update the `runner.py` and potentially remove the MySQL related connection stuff, if you decide to use MongoDB.
- Create a copy of the `.env.template` file and call it `.env`. This file will be used to load environment variables 
like the database credentials from this file (which is also on `.gitignore`). Remove the database parameters for the 
database you don't need.

**Create Stores**

After having chosen a database, you can now start to create stores. We recommend having separate `.py` files for each
table / collection in the `storage/` folder.

The stores are initialised in the `runner.py` and references to these stores are stored in the `stores` dictionary, 
which allows to easily pass all database stores into other components such as API handler or data adapter components.
Clean up the `TODO` items in the `runner.py` and remove traces of the database functions you don't need.

**Change Frontend Title**

The template for the index.html is located here: `frontend/index.html`.
Webpack will use that file and inject the script which represents the transpiled frontend. Note: the 
`templates/index.html` is created by Webpack and will be overwritten every time the frontend compiles.

Please also change the name and description in the package.json for completeness.
