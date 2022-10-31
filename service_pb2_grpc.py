# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import service_pb2 as service__pb2


class BranchStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UpdateTransaction = channel.unary_unary(
                '/Branch/UpdateTransaction',
                request_serializer=service__pb2.Request.SerializeToString,
                response_deserializer=service__pb2.UpdateTransactionResponse.FromString,
                )
        self.ReadTransaction = channel.unary_unary(
                '/Branch/ReadTransaction',
                request_serializer=service__pb2.Request.SerializeToString,
                response_deserializer=service__pb2.ReadTransactionResponse.FromString,
                )
        self.PropogateBranch = channel.unary_unary(
                '/Branch/PropogateBranch',
                request_serializer=service__pb2.PropogateBranchRequest.SerializeToString,
                response_deserializer=service__pb2.PropogateBranchResponse.FromString,
                )


class BranchServicer(object):
    """Missing associated documentation comment in .proto file."""

    def UpdateTransaction(self, request, context):
        """MsgDelivery Service 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadTransaction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PropogateBranch(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BranchServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UpdateTransaction': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateTransaction,
                    request_deserializer=service__pb2.Request.FromString,
                    response_serializer=service__pb2.UpdateTransactionResponse.SerializeToString,
            ),
            'ReadTransaction': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadTransaction,
                    request_deserializer=service__pb2.Request.FromString,
                    response_serializer=service__pb2.ReadTransactionResponse.SerializeToString,
            ),
            'PropogateBranch': grpc.unary_unary_rpc_method_handler(
                    servicer.PropogateBranch,
                    request_deserializer=service__pb2.PropogateBranchRequest.FromString,
                    response_serializer=service__pb2.PropogateBranchResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Branch', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Branch(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def UpdateTransaction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Branch/UpdateTransaction',
            service__pb2.Request.SerializeToString,
            service__pb2.UpdateTransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadTransaction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Branch/ReadTransaction',
            service__pb2.Request.SerializeToString,
            service__pb2.ReadTransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PropogateBranch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Branch/PropogateBranch',
            service__pb2.PropogateBranchRequest.SerializeToString,
            service__pb2.PropogateBranchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
