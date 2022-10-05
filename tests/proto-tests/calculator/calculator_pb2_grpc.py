# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import calculator_pb2 as calculator__pb2


class CalculatorStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
        """Constructor.

        Args:
          channel: A grpc.Channel.
        """
        self.SquareRoot = channel.unary_unary(
            '/Calculator/SquareRoot',
            request_serializer=calculator__pb2.Number.SerializeToString,
            response_deserializer=calculator__pb2.Number.FromString,
        )


class CalculatorServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def SquareRoot(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CalculatorServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'SquareRoot': grpc.unary_unary_rpc_method_handler(
            servicer.SquareRoot,
            request_deserializer=calculator__pb2.Number.FromString,
            response_serializer=calculator__pb2.Number.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'Calculator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))