keys1 = "qwertyuiop"
keys2 = "asdfghjkl"
keys3 = "zxcvbnm"

for n, i in enumerate(keys1):
    print(f"{ord(i)} {n};")

for n, i in enumerate(keys2, 12):
    print(f"{ord(i)} {n};")

for n, i in enumerate(keys3, 24):
    print(f"{ord(i)} {n};")