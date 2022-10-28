import grpc
import time
import service_pb2_grpc
import service_pb2

class Customer:
    def __init__(self, id, events):
        # unique ID of the Customer
        self.id = id
        # events from the input
        self.events = events
        # a list of received messages used for debugging purpose
        self.recvMsg = list()
        # pointer for the stub
        self.stub = None

    # TODO: students are expected to create the Customer stub
    def createStub(self):
        pass

    # TODO: students are expected to send out the events to the Bank
    def executeEvents(self):
        pass

    def call_deposit(self, money):
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = service_pb2_grpc.BranchStub(channel)
            response = stub.Deposit(service_pb2.DepositInput(id=self.id, money=money))
        print("Money deposited to branch: " + response.message)   
    