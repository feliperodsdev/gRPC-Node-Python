# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from protobufs import product_pb2 as protobufs_dot_product__pb2


class ProductServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_unary(
                '/ProductService/List',
                request_serializer=protobufs_dot_product__pb2.Empty.SerializeToString,
                response_deserializer=protobufs_dot_product__pb2.ProductList.FromString,
                )
        self.Insert = channel.unary_unary(
                '/ProductService/Insert',
                request_serializer=protobufs_dot_product__pb2.NewItem.SerializeToString,
                response_deserializer=protobufs_dot_product__pb2.ProductItem.FromString,
                )
        self.Find = channel.unary_unary(
                '/ProductService/Find',
                request_serializer=protobufs_dot_product__pb2.ProductItemId.SerializeToString,
                response_deserializer=protobufs_dot_product__pb2.ProductItem.FromString,
                )
        self.Delete = channel.unary_unary(
                '/ProductService/Delete',
                request_serializer=protobufs_dot_product__pb2.ProductItemId.SerializeToString,
                response_deserializer=protobufs_dot_product__pb2.ProductItem.FromString,
                )


class ProductServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Insert(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Find(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProductServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=protobufs_dot_product__pb2.Empty.FromString,
                    response_serializer=protobufs_dot_product__pb2.ProductList.SerializeToString,
            ),
            'Insert': grpc.unary_unary_rpc_method_handler(
                    servicer.Insert,
                    request_deserializer=protobufs_dot_product__pb2.NewItem.FromString,
                    response_serializer=protobufs_dot_product__pb2.ProductItem.SerializeToString,
            ),
            'Find': grpc.unary_unary_rpc_method_handler(
                    servicer.Find,
                    request_deserializer=protobufs_dot_product__pb2.ProductItemId.FromString,
                    response_serializer=protobufs_dot_product__pb2.ProductItem.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=protobufs_dot_product__pb2.ProductItemId.FromString,
                    response_serializer=protobufs_dot_product__pb2.ProductItem.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ProductService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ProductService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ProductService/List',
            protobufs_dot_product__pb2.Empty.SerializeToString,
            protobufs_dot_product__pb2.ProductList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Insert(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ProductService/Insert',
            protobufs_dot_product__pb2.NewItem.SerializeToString,
            protobufs_dot_product__pb2.ProductItem.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Find(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ProductService/Find',
            protobufs_dot_product__pb2.ProductItemId.SerializeToString,
            protobufs_dot_product__pb2.ProductItem.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ProductService/Delete',
            protobufs_dot_product__pb2.ProductItemId.SerializeToString,
            protobufs_dot_product__pb2.ProductItem.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)