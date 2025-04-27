import json

with open("smart_notes/test.json", "r", encoding="utf-8") as json_file:
    data_json = json_file.read()
    print(data_json)
   
data_json2 = None

with open("smart_notes/test.json", "r", encoding="utf-8") as json_file:
    data_json2 = json.load(json_file)
    print("\n\n", data_json2)

with open("smart_notes/test.json", "w", encoding="utf-8") as json_file:
    data_json2["Note 1"]["text"] = "Chenged text for note 1"
    data_json2["Note 3"] = {
        "text": "Нотатка 3",
        "tags": ["tag2"]
    }
    # data_json2["Note 3"] = {
    #     "text": "Нотатка 3",
    #     "tags": ["tag2"]
    # json.dump(data_json2, json_file)