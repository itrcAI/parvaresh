import json

def save_json(dates, 
              iter : int,
              path_destination : str = "None"):
    if path_destination != "None":
        output_file = path_destination + "/dates.json"
    else:
        output_file = "dates.json"

        
    result = {}
    for temp_day, temp_date in zip(dates, list(range(iter))):
        result.update({temp_day : temp_date})
        
    with open(output_file, "w") as f:
        json.dump(result, f)

