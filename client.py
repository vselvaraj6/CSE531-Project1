import json
import sys
from customer import Customer
from multiprocessing import Process

input_file = sys.argv[1]
customer_input_items = list()

with open(input_file, 'r') as f:
    input_items = json.load(f)    

    for input_item in input_items:
        if('customer' == input_item.get('type')):
            customer_input_items.append(input_item)

customers = []
customer_processes = []
for customer_input_item in customer_input_items:
    customer = Customer(customer_input_item.get('id'),customer_input_item.get('events'))
    customers.append(customer)
    customer_process = Process(target=customer.executeUpdateEvents(),)
    customer_processes.append(customer_process)
    customer_process.start()

for customer_process in customer_processes:
    customer_process.join()    

for customer_input_item in customer_input_items:
    customer = Customer(customer_input_item.get('id'),customer_input_item.get('events'))
    customers.append(customer)
    customer_process = Process(target=customer.executeReadEvents(),)
    customer_processes.append(customer_process)
    customer_process.start()

for customer_process in customer_processes:
    customer_process.join()    

for customer in customers:
    print('customer response : ', customer)
