import grpc
import time
import service_pb2_grpc
import service_pb2
import json
import sys

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
       pass

    # TODO: students are expected to send out the events to the Bank
    def executeEvents(self):
        port = 50050 + self.id
        host = 'localhost:'+str(port)
        print('Creating stub to connect to ', host)
        request = service_pb2.Request(id=self.id, type='customer', events=self.events)
        with grpc.insecure_channel(host) as channel:
            self.stub = service_pb2_grpc.BranchStub(channel)
            response = self.stub.MsgDelivery(request=request)
            print(response)
        channel.close()    

  