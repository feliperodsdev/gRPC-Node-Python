from asyncio.log import logger
import time
from concurrent import futures
import grpc
from protobufs.product_pb2 import ProductList, ProductItem
import protobufs.product_pb2_grpc
from data import fakeData

class GrpcService(protobufs.product_pb2_grpc.ProductServiceServicer): 
    def Find(self, request, context):
        product = [x for x in fakeData if x.id == request.id]
        return product[0]

def server_start():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    protobufs.product_pb2_grpc.add_ProductServiceServicer_to_server(GrpcService(), server)
    server.add_insecure_port('0.0.0.0:50051')
    server.start()
    server.wait_for_termination()


server_start()