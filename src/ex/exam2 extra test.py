import json

def main():

    data = {
        "item": "notebook",
        "quantity": 3,
        "price": 2.50,
        "tags": ["stationery", "school", "paper"]
    }


    with open("sample.json", "w") as f:
        json.dump(data, f, indent=4)

    print("JSON file saved as sample.json")


    with open("sample.json", "r") as f:
        loaded = json.load(f)

    print("Loaded JSON content:")
    print(loaded)

if __name__ == "__main__":
    main()
