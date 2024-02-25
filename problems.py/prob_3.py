# "If"  boyicha masalalar
#_______________________________
# a= int(input("a= "))
# b = int(input("b= "))
# c = int(input("c= "))

# if a>=b and a>=c:
#     max = a
# elif b>=a and b>=c:
#     max = b
# else:
#     max = c
    
# if a<=b and a<=c:
#     min = a
# elif b<=a and b<=c:
#     min = b
# else:
#     min = c
    
# orasidagi_son = a + b + c - max - min
# print(f" MAX = {max} \n MIN = {min} \n Orasidagi son = {orasidagi_son}")

#___________________________________

data = {
    'meva':{
        "olma": 100,
        "anor": 100,
        "gilos": 100,
    },
    'sabzavot':{
        "sabzi": 1200,
        "kartoshka": 800,
        "karam": 500,
    },
}

a, b = ('meva', {'olma': 100, 'anor': 100, 'gilos': 100})
# print(a)
# print(b)
for a,b in data.items():
    print(a)

# print(data['meva'].keys())
# print(data.values())

for i,j in data['meva'].items():
    print(i)
    


# print(data['ovqat'])
# print(data.get('ggg', 'topilmadi'))

# data2 = {}

# # print(data.items())
# for key, values in data.items():
#     data2[key] = values.copy()
    




data2 = {}
for key, values in data.items():
    oila = {}
    for k, v in values.items():
        oila[k] = 0
    data2[key] = oila


# print(data)
# print(data2)

# print("---------------")
data2['meva']['olma'] = 600

print(data)
print(data2)



# data = {
#     "olma": {
#         "qizil":12,
#         "oq":3333,
#         },
#     "gilos":500,
# }

# data2 = data.copy()


# print(data)
# print(data2)

# data2['olma'] = 750

# print("------------")
# print(data)
# print(data2)
