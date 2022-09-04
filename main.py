a = 2
b = 4
# print(a+b)

def myFunc(name, *all, id, **abc):
    print(name, "\n", id)
    if(len(all) != 0):
        print(all)

# myFunc("alqama", 23, "BS", "Teacher", id=345)

def employeeDetails(**data):
    for key, value in data.items():
        # print(key, " = ", value)
        print(f"{key} = {value}")


# employeeDetails(name = "Alqama", age = 23, id="Pak-9802")

abc = {
    "name": "Alqama",
    # "myDictFunc": (lambda s: s.upper())
}
abc["age"] = 23
# for key, value in abc.items():
#     print(f"{key} = {value}")

# print(abc["myDictFunc"]("alq"))

xyz = abc.copy()
xyz["id"] = 12345

print(abc)
print(xyz)

class Employee:
    pass


emp1 = Employee();
emp1.name = "Alqama"

print(emp1.name)










