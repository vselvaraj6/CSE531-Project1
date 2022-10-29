import json
import sys
from customer import Customer
from multiprocessing import Process

input_file = sys.argv[1]
customer_events = list()

with open(input_file, 'r') as f:
    input_events = json.load(f)    

    for input_event in input_events:
        if('customer' == input_event.get('type')):
            customer_events.append(input_event)

customers = []
for customer_event in customer_events:
    customer = Customer(customer_event.get('id'),customer_event.get('events'))
    customer.executeEvents()
    customers.append(customer)
  