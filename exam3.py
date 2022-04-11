

# массивы
m1 = list([1,2,3,4,5])

print(m1)

print(m1[0])

print(len(m1))

m1.append(123)
m1.remove(1)


for item in m1:
    print(" : ", item)

# dict()

h1 = {"a1": 123, "d1": "test", 33: "test2", 33: "test3", (1,2): "qqq"}

print("----------")

h1[(123,55,77,886)] = 99988999898

for k, item in h1.items():
    print(" : ", k, item)

po, reg, county, hs = (123,55,77,886)

print(po, reg, county, hs)
print(h1["d1"])

user1 = {"name": "Alex", "lastname": "Cheremisin", "age": 49, 
"skils": ["java", "python", "clojyre", "brainfuck"]}
user2 = {"name": "Dmitry", "lastname": "Danilov", "age": 30, 
"skils": [ "python"]}

users = [user1, user2]

def print_user(a1):
    print(a1["age"])
    print(a1["lastname"])

def print_user1(age, lastname, name, skils, **kv):
    print(age, name, lastname, skils)
    

for u in users:
    print_user1(**u)

