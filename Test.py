#Test with local Json

from jsonsearch import JsonSearch
import json

#Function Test with loacal JSON

def read_json(file):
    try:
        print('Reading from input')
        with open(file, 'r') as f:
            return json.load(f)
    finally:
        print('Done reading')

return_dict = read_json('sample.json')

def parse(return_dict):
    decoded_json = JsonSearch(object=return_dict, mode='j')
    user_id = "reference"
    id_path = decoded_json.search_all_path(key="category")
    title = decoded_json.search_all_value(key='title')
    print(id_path)
    print(title)
    
print(return_dict)
parse(return_dict)