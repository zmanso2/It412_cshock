import json

with open("files/config.json") as json_obj:
    config_data = json.load(json_obj)

#print(config_data["memory"])
config_data["memory"] = "100 MB"

with open("files/config.json", "w") as json_obj:
    json.dump(config_data,json_obj)
