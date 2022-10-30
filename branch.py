import grpc
from concurrent import futures
import service_pb2_grpc
import service_pb2

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

    def set_branches(self, branches):
        self.branches = branches
        
    def propogate_branch(self):
        for branch in self.branches:
            if(branch.id != self.id):
                port = 50050 + self.id
                host = 'localhost:'+str(port)
                print('Creating stub to connect to ', host)
                with grpc.insecure_channel(host) as channel:
                    self.stub = service_pb2_grpc.BranchStub(channel)
                    request = service_pb2.PropogateBranchRequest(id=branch.id, balance=self.balance)
                    response = self.stub.PropogateBranch(request=request)
                    print(response)
                channel.close()     

    # TODO: students are expected to process requests from both Client and Branch
    def MsgDelivery(self,request, context):
        for event in request.events:
            if event.interface == 0:
                output = service_pb2.Response()
                output.money = self.balance  
                print("query - customer id: ", self.id, "balance: ", self.balance)
            elif event.interface == 1:
                output = service_pb2.Response()
                self.balance = self.balance + event.money
                print("deposit - customer id: ", self.id, "balance: ", self.balance)
                self.propogate_branch()
            elif event.interface == 2:
                output = service_pb2.Response()
                self.balance = self.balance - event.money
                print("withdraw - customer id: ", self.id, "balance: ", self.balance)
                self.propogate_branch()
            output.id = self.id
            output.result = 0
            output.interface = event.interface
        return output

    def PropogateBranch(self, request, context):
        branches = []
        for branch in self.branches:
            print("branch.balance", branch.balance, "request.balance",request.balance)
            branch.balance = request.balance
            branches.append(branch)
        self.set_branches(branches)
        for bra in self.branches:
            print("bra.balance", bra.balance, "bra.id", bra.id)    
        print("propogate branch successful!")   
        output = service_pb2.PropogateBranchResponse()
        output.result = 0
        output.id = request.id
        return output   
