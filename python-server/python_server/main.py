"""The Python implementation of the GRPC helloworld.Greeter server."""

import logging
from asyncio.log import logger
from concurrent import futures

import grpc
from grpc_reflection.v1alpha import reflection

import helloworld_pb2
import helloworld_pb2_grpc


class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        logger.info("[SayHello] request.name: {}".format(request.name))
        logger.info("[SayHello] request.age: {}".format(request.age))
        return helloworld_pb2.HelloReply(
            message="Hello, {} ({})!".format(request.name, request.age)
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    SERVICE_NAMES = (
        helloworld_pb2.DESCRIPTOR.services_by_name["Greeter"].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    serve()
