<div align="center">
  <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="Railway Logo" width="200" />
</div>

# FastAPI Template

An example HTTP REST API built on top of [FastAPI](https://fastapi.tiangolo.com/). Easy to deploy, set up, and scale.

Out of the box, this starter includes lightweight implementations of the following features that are easy to extend and customize:

- **REST API endpoints** - A set of REST API endpoints using standard, spec-compliant methods like `GET` & `POST`
- **Rate Limiting** - Rate limiting to prevent abuse of your API, at configurable rates based on customizable identifiers
- **Caching** - Caching of API responses to reduce the load on your API and improve performance
- **Dependency Injection** - Dependency injection to easily inject dependencies into your API endpoints
- **OpenAPI Documentation** - Automatically generated OpenAPI documentation for your API, that can be annotated and deployed alongside your code
- **Type Hints** - Well defined requests and responses with Pydantic models and type hints
- **Environment Variables** - Configuration of your application using environment variables that can be set in a `.env` file

## 🚀 Quickstart

**Deploy on Railway in 1-click**

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/???)

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

## 📦 Deployment

You can deploy this application to [Railway](https://railway.app/) connected to a GitHub repository where every new Pull Request will generate a completely new, isolated preview environment. Merges to the `main` branch are automatically built and deployed with no additional config.

Railway provides a free tier that you can use to deploy this application to "kick the tires".

## 📃 OpenAPI Documentation

By default, FastAPI will generate an OpenAPI schema for your API. This schema is used to generate documentation for your API automatically. You can access the documentation at http://localhost:8000/docs. Your docs are made publicly available by default at `/redoc` and `/docs` when deploying your application.

## 🔑 Environment Variables

To

## 💿 Powered By

Built on a modern stack with the following technologies:

- **FastAPI** - A modern, fast (high-performance), web framework for building APIs based on standard Python type hints.
- **Python 3.10** - Supporting modern versions of Python to get the latest and greatest features.
- **Poetry** - A modern dependency management and packaging tool for Python.
- **Redis** - An open source, in-memory data structure store, used for caching and rate limiting.

## 📝 Additional Resources

- Visit the [FastAPI docs](https://fastapi.tiangolo.com/tutorial/) for more information about building an API .
- Railway's [docs](https://docs.railway.app/) provide more information about managing your application and exposing it to internet traffic.
