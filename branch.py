import grpc
from concurrent import futures
import service_pb2_grpc
import service_pb2
import logging

class Branch(service_pb2_grpc.BranchServicer):

    def __init__(self, id, balance, branches):
        # unique ID of the Branch
        self.id = id
        # replica of the Branch's balance
        self.balance = balance
        # the list of process IDs of the branches
        self.branches = branches
        # the list of Client stubs to communicate with the branches
        self.stubList = list()
        # a list of received messages used for debugging purpose
        self.recvMsg = list()
        # iterate the processID of the branches

    # TODO: students are expected to process requests from both Client and Branch
    def MsgDelivery(self,request, context):
        pass


    def start_bank_process(self, id, balance, branches):
        GRPC_BIND_ADDR = '[::]:50051'
        executor = futures.ThreadPoolExecutor(max_workers=1)
        server = grpc.server(executor, options=[
            ("grpc.so_reuseport",1),
            ("grpc.use_local_subchannel_pool", 1),
        ],)
        service_pb2_grpc.add_BranchServicer_to_server(Branch(id=id,balance=balance,branches=branches), server)
        server.add_insecure_port(GRPC_BIND_ADDR)
        server.start()
        print("gRPC Bank process started for ID" , id)
        server.wait_for_termination()
    
  
