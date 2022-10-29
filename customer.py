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

    def __str__(self) -> str:
        return "id: {0}, events:{1}".format(self.id,self.events)   

    # TODO: students are expected to create the Customer stub
    def createStub(self):
        port = 50050 + self.id
        with grpc.insecure_channel('localhost:'+str(port)) as channel:
            self.stub = service_pb2_grpc.BranchStub(channel)

    # TODO: students are expected to send out the events to the Bank
    def executeEvents(self):
        for event in self.events:
            interface = event.get('interface')
            print(interface)
            

        
     