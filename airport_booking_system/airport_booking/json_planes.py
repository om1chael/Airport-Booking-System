import json
from config.definitions import json_path


# import Class that will be used by Flask and in JSON file

def create_json_planes_file(plane_id, plane_cap):
    # read the contents of the JSON planes file and add the created plane to the list of planes
    # values come from Plane class
    planes_dict = {
        "id": plane_id,
        "max capacity": plane_cap
    }
    with open(json_path + "planes.json", "r") as file:
        data = json.load(file)
    data.append(planes_dict)

    with open(json_path + "planes.json", "w") as file:
        json.dump(data, file)
        # overwrites the JSON file with the new data added to old
    return
