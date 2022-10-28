import json
import sys
from customer import Customer
from branch import Branch
from multiprocessing import Process

input_file = sys.argv[1]
customer_events = list()
branch_events = list()

with open(input_file, 'r') as f:
    input_events = json.load(f)    

    for input_event in input_events:
        if('customer' == input_event.get('type')):
            customer_events.append(input_event)
        elif('branch' == input_event.get('type')):
            branch_events.append(input_event)

    # print(customer_events)
    # print('------------------')
    # print(branch_events)

branch_processes = []
for branch_event in branch_events:
    branch = Branch(branch_event.get('id'),branch_event.get('balance'),{})
    print("invoking branch process ... ", branch.id)
         
    branch_process = Process(target=branch.start_bank_process, args=(branch.id,branch.balance,branch.branches,))
    branch_processes.append(branch_process)
    branch_process.start()

for branch_process in branch_processes:
    branch_process.join()


for customer_event in customer_events:
    cust = Customer(id=customer_event.get('id'),events=customer_event)
    cust.call_deposit(100)


# branch_processes = []
# for branch_event in branch_events:
#     branch = branch.Branch(id=branch_event.get('id'), balance=branch_event.get('balance'), branches=[])
#     print("invoking branch process ... ", branch.id)
    
#     branch_process = multiprocessing.Process(target=branch.start_bank_process, args=(branch.id,branch.balance,branch.branches))
#     branch_process.start()
#     branch_processes.append(branch_process)    