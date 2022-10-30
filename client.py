import json
import sys
from customer import Customer
from multiprocessing import Process

def parse_input_file():
    customer_input_items = list()
    try:
        with open(input_file, 'r') as f:
            input_items = json.load(f)    

            for input_item in input_items:
                if('customer' == input_item.get('type')):
                    customer_input_items.append(input_item)           
    except:
        print("Invalid format. Please check the content of input.json file") 
    return customer_input_items                   


if len(sys.argv) < 2:
    print("Missing input file. Pass input.json file as argument!")
    exit()

input_file = sys.argv[1]
customer_input_items = parse_input_file()

customers = []
customer_processes = []

for customer_input_item in customer_input_items:
    customer = Customer(customer_input_item.get('id'),customer_input_item.get('events'))
    customers.append(customer)

for customer in customers:
    for event in customer.events:
        if event.get('interface') != 'query':
            customer_process = Process(target=customer.executeUpdateEvents(),)
            customer_processes.append(customer_process)
            customer_process.start()

for customer in customers:
    for event in customer.events:
        if event.get('interface') == 'query':
            customer_process = Process(target=customer.executeReadEvents(),)
            customer_processes.append(customer_process)
            customer_process.start()

for customer_process in customer_processes:
    customer_process.join()    

for customer in customers:
    print('------------------Final Response-------------')
    print(customer)
