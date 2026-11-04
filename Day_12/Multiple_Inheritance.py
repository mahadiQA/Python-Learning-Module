class baba:
     car = "BMW"
     tk = "100cr"
     Home = "10 floor"

class kaka:
    SmartPhone="iPhone"
    Ac="Walton"

class kaka2:
    Security= "Web-Camera"
    Laptop = "Macbook"
    Camera="Canon"

class kaka3(baba,kaka,kaka2):
    BrokenHome=""
    BrokenPhone=""

k=kaka3()
print(k.Laptop)

