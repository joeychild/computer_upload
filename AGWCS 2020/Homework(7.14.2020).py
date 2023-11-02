a = {}
key = "default"
while True:
    b = {}
    key1 = key
    key = input("Enter key: ")
    if key == '':
        key = key1
    else:
        pass
    value = input("Enter value: ")
    try:
        value = int(value)
    except ValueError:
        try:
            value = float(value)
        except ValueError:
            value = str(value)
    val = []
    val.append(value)
    b[key] = val
    a = {**a,**b}
    c = input("Are you finished? ")
    if c == "No":
        continue
    else:
        break
print(a)