

def print_user( user, password, *data ):
    print("User:", user,
          "Password:", password,
          "Data size:", len(data),
          "Data:", data)
    pass

print("-------------------------")
m1 = [11,22,33, 44]
print(m1)

print_user("Alex", "qwerty", *m1)








