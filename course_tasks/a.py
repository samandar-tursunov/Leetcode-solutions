Malumotlar_ombori = {
    "SABZAVOTLAR" :
        {"bodring":12, "pomidor":4, "kartoshka":6},
    "ICHIMLIKLAR": 
        {"gazli-suv":20, "energetik":31, "sharbat":17},
    "XOJALIK_BUYUMLAR" :
        {"bolg'a": 3, "pichoq":13, "qozon":2, "choynak":4},
    "AKSESUARLAR":
        {"soat":22, "uzuk":3, "tumor":1},
    "KIYIMLAR": 
        {"palto":10, "ko'ylak":2, "tufli":14,"kepka":23, "shim":7}
}
qoshish_malumotlari = {}
for key,value in Malumotlar_ombori.items():
    qoshish_mahsulot_key = key
    qoshish_mahsulot_value = value.copy()
    qoshish_malumotlari[qoshish_mahsulot_key] = qoshish_mahsulot_value
for key,value in qoshish_malumotlari.items():
    for key_2,value_2 in qoshish_malumotlari[key].items():
        qoshish_malumotlari[key][key_2] = 0
# print(Malumotlar_ombori)
# print(qoshish_malumotlari)
while True:
    print("""     BU YERGA ADMIN/MIJOZ KIRA OLADI \n   """)
    login = str(input("Iltimos loginingizni kiriting >>>  "))
    password = int(input("Parolni ham kiriting(FAQAT RAQAMLAR):  "))
    
    if login == "admin" and password == 1111:
        print("""
              ============ BU ADMIN OYNASI ===============
              
              SIZDAGI HUQUQLAR
              
              KO'RISH  >>1
              QO'SHISH >>2
              SOTISH   >>3
              HISOBOT  >>4 
              ORTGA    >>0
              
              """)
        
        while True:
            bolim = int(input("Nima huquqdan foydalanasiz:\n  "))
            
#                                         ___________ Ko'rish bo'limi _____________
            
            if bolim == 1:
                while True:
                    print("SIZDAGI (Turkumlar)================\n")
                    n = 0
                    for a, b in Malumotlar_ombori.items():
                        n += 1
                        print(f"({n}). {a}")
                    turkum_ichida = str(input("Qaysi turkumni ko'rasiz: ")).upper()                          
                    if turkum_ichida in Malumotlar_ombori:
                        for i, j in Malumotlar_ombori[turkum_ichida].items():
                            print(f"{i.title()} mahsuloti --> {j} miqdorida ")
                        
                    else:
                        print("Bu turkum omborda mavjud emas")
                    
                    stop = int(input("""
                                    Davom etish uchun --> 1
                                    To'xtatish uchun --> 0
                                    """))
                    if stop == 1:
                        continue
                    elif stop == 0:
                        break
            
#                                         ____________ Qo'shish bo'limi ____________
            elif bolim == 2:
                while True:
                    list_turkumlar = []
                    index = 0
                    for key,value in Malumotlar_ombori.items():
                        
                        list_turkumlar.append(key)
                        print((str(index+1)+" "+key).center(125))
                        index+=1
                    index = input("Kerakli bo'limni raqam orqali tanlang:")
                    if index.isdigit() and int(index) > 0 and int(index) <6:
                        index = int(index)
                        print(list_turkumlar[index-1])
                        qoshish_mahsulot_key = list_turkumlar[index-1]
                        malumot_ombori_key  = qoshish_mahsulot_key
                        
                        qoshish_mahsulot_value_key = input("Kerakli mahsulot nomini kiriting:") 
                        if qoshish_mahsulot_key in qoshish_malumotlari:
                            malumot_ombori_value_key = qoshish_mahsulot_value_key
                            qoshish_mahsulot_value = qoshish_malumotlari[qoshish_mahsulot_key]
                            qoshish_mahsulot_value_value  = int(input("Miqdori:"))
                            if qoshish_mahsulot_value_key in qoshish_mahsulot_value:
                                malumot_ombori_value_value = qoshish_mahsulot_value_value
                                Malumotlar_ombori[malumot_ombori_key][malumot_ombori_value_key] += malumot_ombori_value_value
                            else:
                                qoshish_malumotlari[qoshish_mahsulot_key][qoshish_mahsulot_value_key] = qoshish_mahsulot_value_value
                                malumot_ombori_value_value = qoshish_mahsulot_value_value
                                Malumotlar_ombori[malumot_ombori_key][malumot_ombori_value_key] = malumot_ombori_value_value
                        else:
                            print("Yangi turkum qo'shib bo'lmaydi")
                            break
                    elif int(index) == 0:
                        break
                    
#                                       ________________________ SOTISH BOLIMI __________________________
            elif bolim == 3:
                while True:
                    list_turkumlar = []
                    index = 0
                    for key,value in Malumotlar_ombori.items():
                        
                        list_turkumlar.append(key)
                        print((str(index+1)+" "+key).center(125))
                        index+=1
                    index = input("Kerakli bo'limni raqam orqali tanlang:")
                    if index.isdigit() and int(index) > 0 and int(index) <6:
                        index = int(index)
                        print(list_turkumlar[index-1])
                    sotuv_ombori = {}
                    sotuv_ombori_key = ''
                    sotuv_ombori_value = {}
                    sotuv_ombori_value_key = ''
                    sotuv_ombori_key = list_turkumlar[index-1]
                    sotuv_ombori[sotuv_ombori_key][sotuv_ombori_value_key] =0
                    malumot_ombori_key = sotuv_ombori_key
                    if sotuv_ombori_key in Malumotlar_ombori:
                        sotuv_ombori_value_key = input("Sotub yuboradigan mahsulotni kiriting: ")
                        if sotuv_ombori_value_key in Malumotlar_ombori[malumot_ombori_key]:
                            while True:
                                sotuv_ombori_value_value = input("Miqdori:")
                                if sotuv_ombori_value_value.isdigit() and int(sotuv_ombori_value_value) >= 0:
                                    # print("eferf")
                                    sotuv_ombori_value_value = int(sotuv_ombori_value_value)
                                    # print(type(sotuv_ombori_value_value))
                                    sotuv_ombori[sotuv_ombori_key][sotuv_ombori_value_key] += sotuv_ombori_value_value

                                    Malumotlar_ombori[malumot_ombori_key][malumot_ombori_value_key] -= sotuv_ombori_value_value
                                    break
                                else:
                                    print("Miqdorni musbat yoki to'g'ri kiritmadingiz.Iltimos boshqatdan kiriting!")
                        else:
                            print("Bizda bunday mahsulot mavjud emas!Mavjud mahsulotlar:")
                            pass
                    
                    else:
                        print("Bizda bunday Turkumlar mavjud emas!Iltimos mavjud turkumni kiriting!Turkumlar")   
                                
                            
                            
                    
                    
                    
                    

            elif bolim == 0:
                break            
                    
                    
                    
                
# print(Malumotlar_ombori)                  
                    
                    
                        
                        
                # qoshish_mahsulot_key = input()
                # while True:
                #     print("""   TURKUMGA MAHSULOT QO'SHISH >>> 1
                #                 YANGI TURKUM YARATISH      >>> 2
                #           """)
                #     turkum = int(input(">>>> "))
                #     if turkum == 1:
                #         m = 0
                #         for a, b in Malumotlar_ombori.items():
                #             m += 1 
                #             print(f"{a} >>> {m}")
                #         s = input("...")
                #         if s == m:
                #             for i,j in Malumotlar_ombori[a].items():
                #                 yangi_mahsulot = str(input("MAHSULOT nomini kiriting: "))
                #                 soni = int(input("MAHSULOT sonini kiriting: "))
                            
                            
                #                 Malumotlar_ombori[j][yangi_mahsulot] = soni
                #                 print("Yangi mahsulot qo'shildi ☑ ")
                #                 print(Malumotlar_ombori[a])

