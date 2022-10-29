import json
import sys
from branch import Branch
from multiprocessing import Process
from concurrent import futures
import service_pb2_grpc
import grpc

input_file = sys.argv[1]
branch_events = list()

with open(input_file, 'r') as f:
    input_events = json.load(f)    

    for input_event in input_events:
        if('branch' == input_event.get('type')):
            branch_events.append(input_event)


branch_processes = []
port = 50051
branches = []
branch_ids = []



