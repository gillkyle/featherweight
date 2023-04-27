<div align="center">
  <img src="https://raw.githubusercontent.com/gillkyle/images/master/featherweight-header.png" width="100%" alt="Featherweight logo" />
</div>

# Featherweight (FastAPI Starter Template)

A straightforward, starter HTTP REST API built on top of [FastAPI](https://fastapi.tiangolo.com/). Quick to deploy, set up, and scale.

Out of the box, this starter includes lightweight implementations of the following features that are easy to extend and customize:

- **REST API endpoints** - a set of REST API endpoints using standard, spec-compliant methods like `GET` & `POST`
- **Rate Limiting** - automatic prevention of abuse of your API, at configurable rates based on customizable identifiers
- **Caching** - tiny persistence of API responses to reduce the load on your API and improve performance
- **Dependency Injection** - invert control and share common functionality across your API
- **OpenAPI Documentation** - automatically generated OpenAPI documentation for your API, that can be annotated and deployed alongside your code
- **Type Hints** - well-defined requests and responses with Pydantic models and type hints
- **Environment Variables** - configuration of your application using environment variables that can be set in a `.env` file

You can extend this template to include additional functionality like:

- **Popular AI Libraries** - add support for popular AI libraries like OpenAI with `poetry add openai`, with the dependency included in your `pyproject.toml` file new builds will automatically include it in your production environment
- **Database Support** - add support for a database like PostgreSQL or MySQL, you can even spin one up alongside the rest of your Railway services
- **Authentication** - drop in whatever authentication/authorization scheme you please

## 🚀 Quickstart

The fastest way to get started is deploying to Railway which will spin up a new instance of this template connected to a GitHub repository. It will manage the networking of server code and the key-value Redis store for you, sharing connections between without any additional configuration.

**Deploy on Railway in 1-click**

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/l2yE91?referralCode=1Apk1r)

### 🛠️ Setup & Installation

Prerequisites:

- [Python 3.10](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/#installation)
- [Redis](https://redis.io/download)

1. Clone the repository

```bash
git clone
```

2. Create a Poetry virtual environment

```bash
poetry env use 3.10
```

Start a shell within the virtual environment

```bash
poetry shell
```

3. Install dependencies

```bash
poetry install
```

4. Run the application

First make sure to start a redis server with

```bash
redis-server
```

Then run the application with:

```bash
poetry run dev
```

You should now be able to access the API at http://localhost:8000 on your machine.

### 📦 Deployment

You can deploy this application to [Railway](https://railway.app/) connected to a GitHub repository where every new Pull Request will generate a completely new, isolated preview environment. Merges to the `main` branch are automatically built and deployed with no additional config.

Railway provides a free tier that you can use to deploy this application to "kick the tires".

## 📃 OpenAPI Documentation

By default, FastAPI will generate an OpenAPI schema for your API. That schema is used to generate documentation for your API automatically. You can access the documentation at http://localhost:8000/docs. Your docs are made publicly available by default at `/redoc` and `/docs` when deploying your application as well.

## 🔑 Environment Variables

To manage a local environment from your product environment, you can use the `.env` file included in this repo as an example for how to share configurations. Railway can also help you manage these variables and will provide some for the services they manage and some of their configurations.

## 💿 Powered By

Built on a modern stack with the following technologies:

- **FastAPI** - A modern, fast (high-performance), web framework for building APIs based on standard Python type hints.
- **Python 3.10** - Supporting modern versions of Python to get the latest and greatest features.
- **Poetry** - A modern dependency management and packaging tool for Python.
- **Redis** - An open source, in-memory data structure store, used for caching and rate limiting.

## 📝 Additional Resources

- Visit the [FastAPI docs](https://fastapi.tiangolo.com/tutorial/) for more information about building API's in general and structuring larger projects.
- Railway's [docs](https://docs.railway.app/) provide more information about managing your application and exposing it to internet traffic.
