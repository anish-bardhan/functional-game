import warmup

b_hash = warmup.binary_hash

for key, value in b_hash.items():
    print(key, "=", value)


for key, value in b_hash.items():
    if key == "x":
        print(value)



def decrypt(message):
    message = message.split("-")
    message = list(message)
    for x in message:
        for key, value in b_hash.items():
            if x == value:
                x = key
    print(x)
decrypt("1100101")
