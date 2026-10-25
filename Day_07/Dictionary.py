StudentInfo={
    "Mahadi":{
        "Name": "Mahadi Hasan Mithu",
        "ID": 11240321822,
        "Location": "Gollamari"
    },
    "Jim":{
        "Name": "Sonom Sultan Jim",
        "ID": 11240321818,
        "Location": "HadisPark"
    }
}

print(StudentInfo["Jim"])
print(StudentInfo["Jim"]["ID"])

#using get()

print("using get()----------------------")
print(StudentInfo.get("Mahadi"))

#show key--------
print("\n-------------finding keys-----------------")
print(StudentInfo.keys())

#Finding value using values()
print("\n--------------finding value-----------------")
print(StudentInfo.values())
