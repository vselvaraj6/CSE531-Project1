
from concurrent import futures
import generated.service.service_pb2_grpc

class Branch(generated.service.service_pb2_grpc.BranchServicer):

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

    def __str__(self) -> str:
       return "id: {0}, balance: {1}, branches: {2}".format(self.id,self.balance,self.branches)     

    def set_branches(self, branches):
        self.branches = branches
        
    # TODO: students are expected to process requests from both Client and Branch
    def MsgDelivery(self,request, context):
        pass



    
  
