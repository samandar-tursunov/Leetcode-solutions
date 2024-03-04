import datetime
shop = {
    "mevalar" : {
        'olma' : {
            'miqdor' : 10,
            'price' : 14000,
            'date' : '12.12.2012',
            'term' : '12.12.2013',
            'country' : 'uzbekistan'
        },
          'anor' : {
            'miqdor' : 80,
            'price' : 17000,
            'date' : '1.10.2022',
            'term' : '1.9.2023',
            'country' : 'uzbekistan'
        },
          'uzum' : {
            'miqdor' : 12,
            'price' : 4000,
            'date' : '9.8.2024',
            'term' : '30.8.2024',
            'country' : 'russian'
        },
    },
    
    "ichimliklar" : {
        'kola' : {
            'miqdor' : 30,
            'price' : 16000,
            'date' : '13.02.2024',
            'term' : '12.12.2024',
            'country' : 'america'
        },
          'fanta' : {
            'miqdor' : 43,
            'price' : 15000,
            'date' : '14.04.2024',
            'term' : '15.10.2024',
            'country' : 'uzbekistan'
        },
          'choy' : {
            'miqdor' : 98,
            'price' : 1000,
            'date' : '28.02.2024',
            'term' : '22.07.2026',
            'country' : 'china'
        },
    }
        
}


add = {}
for key, value in shop.items():
    add[key] = {}
    for k, v in value.items():
        add[key][k] = {}
        for k1 , k2 in v.items():
            add[key][k][k1] = 0
        
 
while True:
    bolim = input("QO'SHISH UCHUN 1 NI BOSING:\nSOTISH UCHUN 2 NI BOSING:\nHISOBOTNI KO'RISH 3 NI BOSING\nDASTURNI YAKUNLASH 0\n\n>>>> ")
    if int(bolim) == 0:
        break
                                   # ================ QO'SHISH BOLIMI =================
    if int(bolim) == 1:
        print((f"**************** MAHSULOT KIRIB KELISH BOLIMI ****************\n").center(160))
        turkumlist = []
        n = 0
        for i, j in shop.items():
            turkumlist.append(i)
            print(f"{n+1}. {i}")
            n += 1
        while True:
                turkum = input(f"Qaysi turkumga qo'shmoqchisiz (1 dan {n} gacha): ")
                if turkum.isdigit() and int(turkum) == 0:
                    break
                if turkum.isdigit() and int(turkum) >0 and int(turkum) <= n:
                    turkum = int(turkum)
                    add_key = turkumlist[int(turkum)-1]
                    shop_key = add_key
                

                    while True:
                        add_key_v = input(f"Ortga--> 0 \n\n{add_key}ga nima mahsulot qo'shmoqchisiz: ") 
                        if add_key_v.isdigit():
                            if int(add_key_v) == 0:
                                break
                        if add_key_v in shop[shop_key].keys():
                            miqdorini = input("Miqdori: ")
                            if miqdorini.isdigit():
                                miqdorini = int(miqdorini)
                                kirgan_vaqt = datetime.datetime.now() 
                                shop[shop_key][add_key_v]['miqdor'] += miqdorini 
                                add[add_key][add_key_v]['miqdor'] += miqdorini
                                
                                print(f"{add_key_v} bazaga muvaffaqiyatli qo'shildi ✅\n Kelgan vaqt {kirgan_vaqt} ")
                            else:
                                print("MIQDORINI XATO KIRITDINGIZ❌\n")
                        else:
                            miqdori = input("miqdor: ")
                            while True:
                                if miqdori.isdigit() and int(miqdori)>0:
                                    miqdori=int(miqdori)
                                    break
                                else:
                                    miqdori=input("XATO KIRITDINGIZ QAYTADAN KIRITING❌ : ")
                            narxi = input("Narxi: ")
                            while True:
                                if narxi.isdigit() and int(narxi)>0:
                                    narxi=int(narxi)
                                    break
                                else:
                                    narxi=input("XATO KIRITDINGIZ QAYTADAN KIRITING❌ : ")
                            sroki = input("Muddati: ") 
                            while True:
                                if sroki.isdigit() and int(sroki)>0:
                                    sroki=int(sroki)
                                    break
                                else:
                                    sroki=input("XATO KIRITDINGIZ QAYTADAN KIRITING❌ : ")
                            country = input("Country: ")
                            
                            miqdori = int(miqdori)
                            kirgan_vaqt = datetime.datetime.now() 
                            add[add_key][add_key_v] = {
                                "miqdor": miqdori,
                                'price': narxi,
                                'date': kirgan_vaqt,
                                'sroki': sroki,
                                'country': country
                            } 
                            shop[shop_key][add_key_v] = {
                                "miqdor": miqdori ,
                                'price': narxi,
                                'date': kirgan_vaqt,
                            }                           
                            print(f"{add_key_v} bazaga muvaffaqiyatli qo'shildi ✅\n Kelgan vaqt: {(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))}")
                            
                            #     print("MIQDORINI XATO KIRITDINGIZ\n")
                else:
                    print("Noto'g'ri buyruq kiritildi ❌ \n")          
                                 # =============== SOTISH BOLIMI =================
    if int(bolim) == 2 :
# <Sotish uchun databasa------ >
        sell = {}
        for key, value in shop.items():
            sell[key] = {}
            for k, v in value.items():
                sell[key][k] = {}
                for k1 , k2 in v.items():
                    sell[key][k][k1] = 0
# </Sotish uchun databasa------ >
        turkumlist = []
        n = 0
        for i, j in shop.items():
            turkumlist.append(i)
            print(f"{n+1}. {i}")
            n += 1
        print((f"**************** MAHSULOTNI SOTIB YUBORISH BOLIMI ****************\n").center(160))
        while True:
            turkum_s = input(f"Qaysi turkumdan sotasiz (0 dan {n} gacha): ")
            if turkum_s.isdigit() and int(turkum_s) == 0:
                    break
            if turkum_s.isdigit() and int(turkum_s) >0 and int(turkum_s) <= n:
                turkum_s = int(turkum_s)
                sell_key = turkumlist[int(turkum_s)-1]
                shop_key = sell_key

                while True:
                    sell_key_v = input(f"Ortga--> 0\n\n{sell_key}dan nimani sotib yubormoqchisiz: ") 
                    if sell_key_v.isdigit():
                        if int(sell_key_v) == 0:
                            break
                    if sell_key_v in shop[shop_key]:
                        soni = int(input(f"{sell_key_v} dan nechta sotib yuborasiz: "))
                        if soni <= shop[shop_key][sell_key_v]['miqdor']:
                            print(f"{sell_key_v} mahsuloti {soni}ta sotildi ✅  ")
                            sell[sell_key][sell_key_v]['date'] = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                            sell[sell_key][sell_key_v]['miqdor'] += soni
                            shop[shop_key][sell_key_v]['miqdor'] -= soni 
                          

                            
                        else:
                            print(f"Sotib bo'lmadi ❌! Bizning mahsulotimiz  {str(soni - shop[shop_key][sell_key_v]['miqdor'])} ta yetmadi " )
                    else:
                        print("Noto'g'ri buyruq berildi ❌ ")
    if int(bolim) == 3:
        print(f"**************** MAHSULOTLARNING REPORT BOLIMI ****************\n")
        tanla = input("Qo'shilganlarni ko'rish>> 1\nSotilganlarni ko'rish>> 2\nJoriy Databasani ko'rish>> 3\nOrqaga>> 0\n")
        
        # while True:
        if tanla.isdigit() and int(tanla) == 0:
            break
        if tanla.isdigit() and int(tanla) == 1:
            total_add = 0
            for turkum, mahsulotlar in add.items():
                for mahsulot, info in mahsulotlar.items():
                    if info['miqdor'] > 0:  
                        total_add += info['miqdor'] 

                        print(f"{mahsulot} -----------> {info['miqdor']} dona kirib kelgan vaqti -----------> {info['date']}")
            
            
        elif tanla.isdigit() and int(tanla) == 2:
            total_price = 0
            for turkum, mahsulotlar in sell.items():
                for mahsulot, info in mahsulotlar.items():
                    if info['miqdor'] > 0:  
                        total_price += info['miqdor'] * shop[turkum][mahsulot]['price']

                        print(f"{mahsulot} -----------> {info['miqdor']} dona -----------> {info['miqdor'] * shop[turkum][mahsulot]['price']} so'm  sotilgan vaqti -----------> {info['date']}")
                    continue    
                                
            print(f"Jami: {total_price} so'm")
        else:
            print("Iltimos yuqoridagi buyruqlarni kiriting ❌ ")    
    


