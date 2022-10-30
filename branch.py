import grpc
from concurrent import futures
import service_pb2_grpc
import service_pb2
import time

class BranchServicer(service_pb2_grpc.BranchServicer):

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

    def propogate_branch(self):

        for process in self.branches:
            host = 'localhost:'+str(process)
            print('Creating branch stub to connect to ', host)
            with grpc.insecure_channel(host) as channel:
                self.stub = service_pb2_grpc.BranchStub(channel)
                request = service_pb2.PropogateBranchRequest(balance=self.balance)
                response = self.stub.PropogateBranch(request=request)
                print(response)
            channel.close()     

    # TODO: students are expected to process requests from both Client and Branch
    def UpdateTransaction(self,request, context):

        event = request.event
        output = service_pb2.Response()
        if event.interface == 1:
            self.balance = self.balance + event.money
            print("deposit - customer id: ", self.id, "balance: ", self.balance)
            print("executing event..", event)
            self.propogate_branch()
        elif event.interface == 2:
            self.balance = self.balance - event.money
            print("withdraw - customer id: ", self.id, "balance: ", self.balance)
            print("executing event..", event)
            self.propogate_branch()
        output.id = self.id
        output.result = 0
        output.interface = event.interface
        return output

    def ReadTransaction(self,request, context):
        print("executing ReadTransaction for..", request.event)
        output = service_pb2.Response()
        output.money = self.balance  
        print("query - customer id: ", self.id, "balance: ", self.balance)
        output.id = self.id
        output.result = 0
        output.interface = request.event.interface
        return output

    def PropogateBranch(self, request, context):
        self.balance = request.balance 
        print("propogate branch successful!")   
        output = service_pb2.PropogateBranchResponse()
        output.result = 0
        return output   
