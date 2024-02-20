matn = "salom DunYo  salom   dunyo, salom"

# print(matn.replace('salom', 'xayr'))
# print(matn.replace('salom', 'xayr',2))


# print(matn.startswith('salom'))
# print(matn.endswith('dunyo'))

m = '123'
n = 'assd'
w = 'qweqr1234'
# print(m.isdigit())
# # # n = int(m)
# # # print(type(n))

# print(n.isalpha())

# print(w.isalnum())

new = 'Salom Dunyo. Salom Hayot'
# n = new.split('o')
# n = new.split()
# n = new.split(' ')
# print(n)

# print(matn.index('s'))
# print(matn[::-1])

# cars  = ['audi', 'bmw', 'nexia', 'malibu']

# mijoz = input("Qaysi mashinani sotib olmoqchisiz: ")
# if mijoz.lower() in cars:
#     print(f"Siz {mijoz} mashinani sotib oldiz")
# else:
#     print(f"Afsuski {mijoz} mashinasi yo'q ")
 

yosh = (input("Yoshingiz nechida?"))

if yosh<=4 or yosh>=60:
    narh = 0
elif yosh < 18:
    narh = 10000
else:
    narh = 20000
    print(f"Chipta {narh} so'm")