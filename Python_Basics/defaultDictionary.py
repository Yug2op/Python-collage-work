from collections import defaultdict

d = defaultdict(list)
# print(d['nitin']) # get the default value of dict


contact = defaultdict(list)

contact["nitin"].append("1234")
contact["nitin"].append("56789")

# print(contact)
contact["hitesh"].append("5255121")
# print(contact)

for key in contact:
    print(key)
for val in contact.values():
    print(val)
for key,val in contact.items():
    print(key,val)

