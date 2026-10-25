#pop()
StudentInfo={
    "Mahadi":{
        "Name": "Mahadi Hasan Mithu",
        "ID": 11240321822,
        "Location": "Gollamari"
    },
    "Jim":{
        "Name":"Sonom Sultan Jim",
        "ID": 11240321818,
        "Loaction": "HadisPark"
    },
    "Test":"Khulna"
}
StudentInfo["Mahadi"].pop("Location")
print(StudentInfo)

#-------------popitem()--------------
StudentInfo.popitem()
print(StudentInfo)


#-----------del()-----------
print("\n\n------------------")
del StudentInfo["Mahadi"]["ID"]
print(StudentInfo)

#clear()----------------
StudentInfo["Mahadi"].clear()
print(StudentInfo)