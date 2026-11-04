class baba:
    Home="10 floor"
    car="BMW"
    Cash="10cr"

class Son1(baba):
    Phone="iPhone"
    Laptop="Macbook"

class Son2(Son1):
    Business="Shop"

class Son3(Son2):
    BrokenPhone=""
    BrokenHome=""

s=Son3()

print(s.Laptop)


