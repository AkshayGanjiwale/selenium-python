itemsIncart = 0

if itemsIncart != 2:
    # raise Exception("Condition not matched")
    pass
assert(itemsIncart == 0 )


#try catch block
try:
    with open('filelog.txt','r') as reader:
        reader.read()
except Exception as e:
    print(e)

finally:
    print("clearing the records")