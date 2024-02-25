"""
If we enter one of the three parameters, this program outputs information about it.

"""


ismlar = ["Jonibek", "Shohruh", "Jonibek", "Shohjahon"]
familyalar = ["Yorqulov", "Xasanov", "Aliyev", "Xasanov"]
manzillar = ["Samarqand", "Buxoro", "Navoi", "Toshkent"]

search = input("Qidiruv: ").title()

#_________________________________________ METHOD 1 ______________________________________________________ 

result = []
for ism, familya, manzil in zip(ismlar, familyalar, manzillar):
    if search in [ism, familya, manzil]:
        result.append((ism, familya, manzil))
if result:
    for i in result:
        print(f"Siz qidirgan so'rovlar>>> Ismi: {i[0]}, Familyasi: {i[1]}, Manzili: {i[2]} \n ")
        
else:
    print("Ma'lumot topilmadi.")


# _________________________________________ METHOD 2 ______________________________________________________

if search in (ismlar + familyalar + manzillar):
    for ism, familya, manzil in zip(ismlar, familyalar, manzillar): 
            if search in [ism,familya, manzil]:
                print(f"Siz qidirgan so'rovlar>>> Ismi: {ism}, Familyasi: {familya}, Manzili: {manzil} \n ") 
else:
    print("Ma'lumot mavjud emas") 
# __________________________________________ METHOD 3 ___________________________________________________

for i,n in enumerate(ismlar):
    if search in [ismlar[i], familyalar[i], manzillar[i]]:
        print(f" {ismlar[i]} {familyalar[i]} {manzillar[i]} dan ")
