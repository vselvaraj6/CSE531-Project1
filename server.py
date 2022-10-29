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

def start_bank_process(id, balance, branches, port):
    GRPC_BIND_ADDR = '[::]:'+str(port)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_BranchServicer_to_server(Branch(id=id,balance=balance,branches=branches), server)
    server.add_insecure_port(GRPC_BIND_ADDR)
    server.start()
    print("gRPC Bank process started for ID" , id, "Listening on port",  GRPC_BIND_ADDR)
    server.wait_for_termination()            

branch_processes = []
port = 50051
branches = []
branch_ids = []
for branch_event in branch_events:
    branch = Branch(branch_event.get('id'),branch_event.get('balance'),{})
    print("invoking branch process ... ", branch.id)
    branch_process = Process(target=start_bank_process, args=(branch.id,branch.balance,branch.branches,port))
    branch_processes.append(branch_process)
    branch_process.start()
    port = port + 1
    branches.append(branch)
    branch_ids.append(branch.id)

for branch in branches:
    branch.set_branches(branch_ids)

for branch in branches:
    print(branch)

for branch_process in branch_processes:
    branch_process.join()


