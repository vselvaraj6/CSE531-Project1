import grpc
from concurrent import futures
import service_pb2_grpc
import service_pb2


class Branch(service_pb2_grpc.RPCServicer):

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
        return service_pb2.ServerOutput()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_BankingServiceServicer_to_server(Branch(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

serve()
    
  
