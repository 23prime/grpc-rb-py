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

## Benchmarking ##

Use [ghz](https://ghz.sh).

### Installing ###

Download from [here](https://github.com/bojand/ghz/releases).

e.g.) `ghz-linux-x86_64.tar.gz` to `/tmp`

```console
$ ls /tmp/ghz-linux-x86_64.tar.gz
$ mkdir /opt/ghz/
$ tar -zxvf /tmp/ghz-linux-x86_64.tar.gz -C /opt/ghz/
$ ls -l /opt/ghz/
-rw-r--r-- 1 root root    11357  4月 10 09:23 LICENSE
-rwxr-xr-x 1 root root 21364736  4月 10 09:22 ghz
-rwxr-xr-x 1 root root 23810360  4月 10 09:23 ghz-web
```

And add `/opt/ghz/` to `$PATH`.

```console
$ ghz -v
v0.108.0 
```

### Usage example ###

See more: <https://ghz.sh/docs/usage>

```console
$ ghz \
    --call helloworld.Greeter/SayHello \
    -d '{ "name": "miku", "age": 17 }' \
    -c 100 \
    -n 1000 \
    --insecure \
    localhost:50051
```
