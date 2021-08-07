import json

class editJsonFile:
    def __init__(file):
        file.name = file

    def open(file):
        try:
            global json_file
            json_file = json.load(open(file))
            return json.load(open(file))
        except Exception as e:
            print(e)
    
    def save(file):
        try:
            json.dump(json_file, open(f"{file}", "w"))
        except Exception as e:
            print(e)

    def edit(file, value, key, *keys):
        try:
            if not json_file[key].keys():
                json_file[key] = value
            else:
                keyadd = 0
                for keyy in keys:
                    if keyadd == 0:
                        valuee = keyy
                    else: 
                        valuee = valuee[keyy]
                    keyadd = keyadd+1
                json_file[key][valuee] = value
        except Exception as e:
            print(e)

    def get(file, key, *keys):
        try:
            if not json_file[key].keys():
                value = json_file[key]
            else:
                value = json_file[key]
                for keyy in keys:
                    if keyy in json_file[key]:
                        value = value[keyy]
                return value
        except Exception as e:
            print(e)
