"""
If we enter one of the three parameters, this program outputs information about it.

"""


ismlar = ["Jonibek", "Shohruh", "Jonibek", "Shohjahon"]
familyalar = ["Yorqulov", "Xasanov", "Aliyev", "Xasanov"]
manzillar = ["Samarqand", "Buxoro", "Navoi", "Toshkent"]

search = input("Qidiruv: ").title()

result = []
for ism, familya, manzil in zip(ismlar, familyalar, manzillar):
    if search in [ism, familya, manzil]:
        result.append((ism, familya, manzil))
if result:
    for i in result:
        print(f"Siz qidirgan so'rovlar>>> Ismi: {i[0]}, Familyasi: {i[1]}, Manzili: {i[2]} \n ")
        
else:
    print("Ma'lumot topilmadi.")


