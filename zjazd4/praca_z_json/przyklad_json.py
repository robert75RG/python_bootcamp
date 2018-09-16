import json

ob1 =["AAA", 2,3,["RAfał", "Magda"]]
print(json.dumps(ob1))

# zapis do pliku
with open("example_json","w") as f:
    json.dump(ob1,f)


#otworzenie pliku
with open("example_json") as f:
    data = json.load(f)
    print(data)
    print(type(data))
    data.append("coś tam")
print(data)

with open("example_json", "w") as f:
    json.dump(data,f)