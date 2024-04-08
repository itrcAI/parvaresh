import json

def save_json(path : str,
              data : dict) -> None:
    
    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=4)


