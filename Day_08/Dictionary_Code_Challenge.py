# Challenge: Dictionaries Basics
# Test your understanding of creating, accessing, changing, adding, and removing dictionary items.
#
# Instructions
# Inside the editor, complete the following steps:
# 1. Create a dictionary called car with the keys "brand", "model", "year" and values "Ford", "Mustang", 2024
# 2. Print the value of the "model" key
# 3. Add a new key "color" with the value "red"
# 4. Remove the "brand" key using pop()
# 5. Print the dictionary

car={"brand":"Ford","model":"Mustang","year":"2024"}

print(car["model"])
car["color"]="red"
car.pop("brand")
print(car)