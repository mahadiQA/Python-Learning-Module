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


#Access on key----------------------

for i in StudentInfo:
    print(i)

#using keys()
for j in StudentInfo.keys():
    print(j)

#Access only value------------------

for x in StudentInfo.values():
    print(x)

#Using items()

for y in StudentInfo.items():
    print(y)