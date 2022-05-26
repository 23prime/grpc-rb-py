# Python gPRC server #

## Install Poetry ##

Use [Poetry](https://python-poetry.org) for package management.

Install Poetry according to this [here](https://python-poetry.org/docs/#installation).

## Install dependencies and create virtual env ##

```console
$ cd python-server/
$ poetry install
```

## Python server ##

- Generate Python sources from `.proto` file

```console
$ poetry run python -m grpc_tools.protoc \
    -I./protos \
    --python_out=./python_server \
    --grpc_python_out=./python_server \
    ./protos/helloworld.proto
```

- Start server

```console
$ poetry run python python_server/main.py
```

- Format code by black

```console
$ poetry run black python_server/ 
```

- Sort import by isort

```console
$ poetry run isort python_server/ 
```
