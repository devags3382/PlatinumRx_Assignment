string = "platinumrx"
seen = ""
for char in string:
    if char not in seen:
        seen += char
print(seen)