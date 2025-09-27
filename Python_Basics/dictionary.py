capital = { "India" : "new delhi",
           "russia" : "moscow",
           "china" : "bijing",
           "japan" : "tokya",
           "france" : "paris"

}

# print(len(capital))
# print(capital.keys())
# print(capital.values())
# print(capital.items())

# creating dictionary using tuples by dict class
keyValue = [("india","new delhi"),("russia","moscow")]
capital2 = dict(keyValue)
# print(type(capital2))

d = {} # to create empty dictionary
d = dict() # to create empty dictionary
# print(capital["India"])

capital['italy'] = 'rome' # inserrt if not present

# print(capital["italy"])

capital['India'] = 'delhi' # update if exsist

# print(capital["India"]) 

del capital["france"] # delete the key-value if present

# print(capital)

# itration on dict

# for key in capital:
    # print(key)
    
for country,capitall in capital.items():
    print(country,capitall)