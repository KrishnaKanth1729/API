<img align="right" width=200px height=200px src="https://cdn.discordapp.com/attachments/776153365452554301/786297555415859220/Tech-With-Tim.png" alt="Project logo">

<h1>Tech With Tim - API</h1>

<div>

[![Status](https://img.shields.io/website?url=https%3A%2F%2Fapi.dev.twtcodejam.net)](https://api.dev.twtcodejam.net) <!-- TODO: Switch to main API link. -->
[![GitHub Issues](https://img.shields.io/github/issues/Tech-With-Tim/API.svg)](https://github.com/Tech-With-Tim/API/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/Tech-With-Tim/API.svg)](https://github.com/Tech-With-Tim/API/pulls)
[![Licence](https://img.shields.io/badge/licence-MIT-blue.svg)](/LICENCE)
[![Discord](https://discord.com/api/guilds/501090983539245061/widget.png?style=shield)](https://discord.gg/twt)
[![Test and deploy](https://github.com/Tech-With-Tim/API/workflows/Release%20-%20Test%2C%20Build%20%26%20Redeploy/badge.svg)](https://github.com/Tech-With-Tim/API/actions?query=workflow%3A%22Release+-+Test%2C+Build+%26+Redeploy%22)

<!-- TODO: Lint & Test status -->

</div>

API for the Tech With Tim website using [FastAPI](https://fastapi.tiangolo.com/).

## 📝 Table of Contents

<!-- - [🧐 About](#-about) -->

- [🏁 Getting Started](#-getting-started)
  - [Discord application](#discord-application)
  - [Prerequisites](#prerequisites)
  - [Environment variables](#environment-variables)
  - [Running](#running)
- [🐳 Running with Docker](#-running-with-docker)
- [✅ Linting](#-linting)
- [🚨 Tests](#-tests)
- [📚 Docs](/docs/README.md)
- [📜 Licence](/LICENCE)
- [⛏️ Built Using](#️-built-using)
- [✍️ Authors](#️-authors)

<!-- ## 🧐 About

TODO: Write about 1-2 paragraphs describing the purpose of your project. -->

## 🏁 Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [Running with Docker](#-running-with-docker) if you want to setup the API faster with Docker.

### Discord application

Create a new Discord application [here](https://discord.com/developers/applications) by clicking the `New application` button and name it whatever you want.

![New application](https://cdn.discordapp.com/attachments/721750194797936823/794646477505822730/unknown.png)

Now that you have an application, go to the OAuth2 tab.

![OAuth2 tab](https://cdn.discordapp.com/attachments/721750194797936823/794648158272487435/unknown.png)

And add `http://127.0.0.1:5000/auth/discord/callback` to the redirects.

![Redirects](https://cdn.discordapp.com/attachments/721750194797936823/798276213776318494/unknown.png)

### Prerequisites

Install Pipenv:

```sh
pip install pipenv
```

Install the required packages and the packages for development with Pipenv:

```sh
pipenv install --dev
```

### Environment variables

#### Required

Start by writing this in a file named `.env`:

```prolog
REDIS_URI=
SECRET_KEY=
POSTGRES_URI=
DISCORD_CLIENT_ID=
DISCORD_CLIENT_SECRET=
```

And fill in the variables with the values below:

- `REDIS_URI` is the Redis server URI.
- `SECRET_KEY` is the key used for JWT token encoding.
- `POSTGRES_URI` is the PostgreSQL database URI.
- `DISCORD_CLIENT_ID` is the Discord application ID. Copy it from your Discord application page (see below).
- `DISCORD_CLIENT_SECRET` is the Discord application secret. Copy it from your Discord application page (see below).

![Client ID and secret](https://cdn.discordapp.com/attachments/721750194797936823/794646777840140298/unknown.png)

#### Optional

For testing you need to add these environment variables:

- `TEST_REDIS_URI` is the Connection URI for Redis testing server.
- `TEST_POSTGRES_URI` is the PostgreSQL database URI for tests.

If you are self hosting the Piston API, you need to set the `PISTON_URL` environment variable.

### Running

Run the API and initialise the database:

#### Make sure submodules are up to date.
> If you have not initialized submodules use this command:\
> `git submodule update --init`
>
> To update submodules:\
> `git submodule foreach git pull`

```sh
pipenv run python launch.py runserver --initdb
```

The API should run at [http://127.0.0.1:5000](http://127.0.0.1:5000). For more information about the CLI, check the docs [here](/docs/cli.md).

## 🐳 Running with Docker

Both the API and the [frontend](https://github.com/Tech-With-Tim/Frontend) can be started using Docker. Using Docker is generally recommended (but not strictly required) because it abstracts away some additional set up work.

- Setup the discord app like done [here](#discord-application).

- Make a file named `.env` like done [here](#environment-variables). You don't need the DB_URI environment variable though.

- Then make sure you have `docker` and `docker-compose` installed, if not read [this for docker](https://docs.docker.com/engine/install/) and [this for docker compose](https://docs.docker.com/compose/install/).

- Deploy the API:

  ```sh
  docker-compose up --build api
  ```

## ✅ Linting

We use a pre-commit hook for linting the code before each commit. Set up the pre-commit hook:

```sh
pipenv run pre-commit install
```

If you want to run the pre-commit checks before trying to commit, you can do it with:

```sh
pipenv run lint
```

## 🚨 Tests

To test the API, we use the [pytest](https://docs.pytest.org/en/stable/) framework to make sure that the code we write works.

Run the tests:

```sh
pipenv run test
```

**When you contribute, you need to add tests on the features you add.**

## ⛏️ Built Using

- [Python](https://www.python.org/) - Language
- [FastAPI](https://fastapi.tiangolo.com/) - Backend framework
- [PostDB](https://github.com/SylteA/postDB) - Database module
- [pytest](https://docs.pytest.org/en/stable/) - Testing framework
- [pytest-asyncio](https://github.com/pytest-dev/pytest-asyncio) - Testing plugin for [pytest](https://docs.pytest.org/en/stable/)

## ✍️ Authors

- [@SylteA](https://github.com/SylteA) - Most of the backend
- [@Shubhaankar-sharma](https://github.com/Shubhaankar-sharma) - Docker deployment
- [@takos22](https://github.com/takos22) - Some endpoints and markdown files

See also the list of [contributors](https://github.com/Tech-With-Tim/API/contributors) who participated in this project.
