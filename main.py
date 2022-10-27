import json
import sys

input_file = sys.argv[1]

with open(input_file, 'r') as f:
    data = json.load(f)

    json_formatted_str = json.dumps(data, indent=2)
    print(json_formatted_str)