# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import helloworld_pb2 as helloworld__pb2


class dataProviderStub(object):
    """HW 8
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.serverConnection = channel.unary_unary(
                '/helloworld.dataProvider/serverConnection',
                request_serializer=helloworld__pb2.ExperimentDetails.SerializeToString,
                response_deserializer=helloworld__pb2.Data.FromString,
                )


class dataProviderServicer(object):
    """HW 8
    """

    def serverConnection(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_dataProviderServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'serverConnection': grpc.unary_unary_rpc_method_handler(
                    servicer.serverConnection,
                    request_deserializer=helloworld__pb2.ExperimentDetails.FromString,
                    response_serializer=helloworld__pb2.Data.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'helloworld.dataProvider', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class dataProvider(object):
    """HW 8
    """

    @staticmethod
    def serverConnection(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/helloworld.dataProvider/serverConnection',
            helloworld__pb2.ExperimentDetails.SerializeToString,
            helloworld__pb2.Data.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
