from main import cookies
import time
import json

with open("data.json", "r") as file:
    data = json.load(file)

cookies = data["cookies"]

while True:
    time.sleep(1)
    cookies += 1
    main_data = {"cookies": cookies, "test_mode": 1}

    main_data_json = json.dumps(main_data)

    with open('data.json', 'w') as json_file:
        json.dump(main_data, json_file)
        print("Saved!")
