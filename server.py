import json
import sys
from branch import BranchServicer
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
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), options=(('grpc.so_reuseport',0),))
    service_pb2_grpc.add_BranchServicer_to_server(BranchServicer(id, balance, branches), server)
    server.add_insecure_port(GRPC_BIND_ADDR)
    server.start()
    print("gRPC Bank process started for ID:" , id, "Listening on port:",  GRPC_BIND_ADDR)
    server.wait_for_termination()            

branch_processes = []
port = 50051
branches = []

port_map = {}
#populate ports for no. of bank process
for branch in branch_events:
    key = branch.get('id')
    port_map[key] = port
    port = port + 1

print("port_map", port_map)

for branch_event in branch_events:

    #remove self processes from the branch 
    branch_id = branch_event.get('id')
    processes = []
   
    for key, value in port_map.items():
        if key != branch_id :
            processes.append(value)

    print("processes after self removal", processes)
    branch = BranchServicer(branch_id, branch_event.get('balance'), processes)
    print("invoking branch process ... ", branch.id)
    branch_process = Process(target=start_bank_process, args=(branch.id,branch.balance,branch.branches,port_map.get(branch_id)))
    branch_processes.append(branch_process)
    branches.append(branch)
    branch_process.start()

for branch_process in branch_processes:
    branch_process.join()


