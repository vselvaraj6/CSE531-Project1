
from concurrent import futures
import service_pb2_grpc
import service_pb2
import sys
import json
import grpc

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
        
    # TODO: students are expected to process requests from both Client and Branch
    def MsgDelivery(self,request, context):
        pass

    def Query(self, request, context):
        print("message recieved")
        print(request)
        op = service_pb2.QueryOutput()
        op.money = 400
        return op

def serve(id, balance, branches):
    GRPC_BIND_ADDR = "localhost:50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), options=(('grpc.so_reuseport',0),))
    service_pb2_grpc.add_BranchServicer_to_server(BranchServicer(id, balance, branches), server)
    server.add_insecure_port(GRPC_BIND_ADDR)
    server.start()
    print("gRPC Bank process started for ID" , id, "Listening on port",  GRPC_BIND_ADDR)
    server.wait_for_termination()         

    
input_file = sys.argv[1]
branch_events = list()

with open(input_file, 'r') as f:
    input_events = json.load(f)    

    for input_event in input_events:
        if('branch' == input_event.get('type')):
            branch_events.append(input_event)

if __name__ == "__main__":
    serve(1, 100, list())  
