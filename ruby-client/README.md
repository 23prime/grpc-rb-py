# Ruby gPRC client #

## Install Ruby and Bundler ##

// skip

## Install dependencies and create virtual env ##

```console
$ cd ruby-client/
$ bundle install
```

## Ruby client ##

- Generate Ruby sources from `.proto` file

```console
$ bundle exec grpc_tools_ruby_protoc \
    -I./protos \
    --ruby_out=./app/lib \
    --grpc_out=./app/lib \
    ./protos/helloworld.proto
```

## Run ##

```console
$ bundle exec ruby app/main.rb Miku
```
