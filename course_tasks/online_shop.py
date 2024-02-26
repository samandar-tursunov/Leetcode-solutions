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
#   QO'SHISH BO'LIMI UCHUN OMBOR_____________
qoshish = {}
for key, values in Malumotlar_ombori.items():
    turkum = {}
    for k, v in values.items():
        turkum[k] = 0
    qoshish[key] = turkum
sotuv = {}   
while True:
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
            if bolim == 0:
                break
            
                                                #___________ Ko'rish bo'limi _____________
            
            if bolim == 1:
                while True:
                    print("SIZDAGI (Turkumlar)================\n")                 
                    list_turkumlar2 = []
                    a = 0
                    for key, value in Malumotlar_ombori.items():
                        list_turkumlar2.append(key)
                        print((str(a + 1) + " " + key))
                        a += 1
                        
                    turkumdagi = input("Biror turkumni tanlang: ")
                    
                    if turkumdagi.isdigit() and int(turkumdagi) > 0 and int(turkumdagi) < 6:
                        turkumdagi = list_turkumlar2[int(turkumdagi) - 1]
                        for i , j in Malumotlar_ombori[turkumdagi].items():
                            print((f"{i} mahsuloti --> {j} miqdorida ").center(125))
                    else:
                        print(("\nKiritishda xatolik yuz berdi ⚠ \n").center(125))
                    stop = input("Davom etish uchun --> 1\n To'xtatish uchun --> 0\n")
                    if stop.isdigit():
                        if int(stop) == 1:
                            continue
                        elif int(stop) == 0:
                            break
                    else:
                        print(("\n\nKiritishda xatolik yuz berdi ⚠ ").center(125))
            
                                        #____________ Qo'shish bo'limi ____________        
            elif bolim == 2:
                while True:
                    list_turkumlar2 = []
                    a = 0
                    for key, value in Malumotlar_ombori.items():
                        list_turkumlar2.append(key)
                        print((str(a + 1) + " " + key).center(125))
                        a += 1  
                    enter = input("Turkumlardan birini tanla: ")
                    if enter.isdigit() and int(enter) > 0 and int(enter) < 6:
                        enter = int(enter)
                        print(f"\n\nSiz qo'shmoqchi bo'lgan turkum >>> {list_turkumlar2[enter - 1]}\n") 
                        qoshish_k = list_turkumlar2[enter-1]
                        malumot_ombori_k = qoshish_k
                        
                        qoshish_v_k = input("\nNimani qo'shmoqchisiz: ")  
                        if qoshish_k in qoshish:
                            malumot_ombori_v_k = qoshish_v_k
                            qoshish_v = qoshish[qoshish_k]
                            qoshish_v_v = (input("\nMiqdori:"))
                            if qoshish_v_k in qoshish_v:
                                qoshish_v_v = int(qoshish_v_v)
                                malumot_ombori_v_v = qoshish_v_v
                                qoshish[qoshish_k][qoshish_v_k] += qoshish_v_v
                                Malumotlar_ombori[malumot_ombori_k][malumot_ombori_v_k] += malumot_ombori_v_v
                                print(f"{qoshish_v_k.title()} muvaffaqiyatli qo'shildi ✅ ")
                            else:
                                qoshish_v_v = int(qoshish_v_v)
                                qoshish[qoshish_k][qoshish_v_k] = qoshish_v_v
                                malumot_ombori_v_v = qoshish_v_v
                                Malumotlar_ombori[malumot_ombori_k][malumot_ombori_v_k] = malumot_ombori_v_v
                                print(f"{qoshish_v_k.title()} muvaffaqiyatli qo'shildi ✅ ")

                        else:
                            print("Yangi turkum qo'shib bo'lmaydi ❌")
                            break
                        
                    elif int(enter)== 0 :
                        break
                                            #______________ SOTUV BOLIM _______________
            elif bolim == 3:
                for key, values in Malumotlar_ombori.items():
                    turkum = {}
                    for k, v in values.items():
                        turkum[k] = 0
                    sotuv[key] = turkum
                while True:
                    list_turkumlar2 = []
                    a = 0
                    for key, value in Malumotlar_ombori.items():
                        list_turkumlar2.append(key)
                        print((str(a + 1) + " " + key).center(125))
                        a += 1  
                    enter = input("Turkumlardan birini tanlang: ")
                    if int(enter) == 0:
                        break
                    elif enter.isdigit() and int(enter) > 0 and int(enter) < 6:
                        enter = int(enter)
                        print(f" Siz sotmoqchi bo'lgan turkum >>> {list_turkumlar2[enter - 1]}") 
                        enter = int(enter)
                    
                        sotuv_k = list_turkumlar2[int(enter) - 1]
                        malumot_ombori_k = sotuv_k
                        if sotuv_k in Malumotlar_ombori:
                            malumot_ombori_k = sotuv_k
                            sotuv_v_k = input("Sotib yuboradigan mahsulotni kiriting: ")

                            if sotuv_v_k in Malumotlar_ombori[malumot_ombori_k]:
                                malumot_ombori_v_k = sotuv_v_k
                                while True:
                                    sotuv_v_v = input("Miqdori:")
                                    if sotuv_v_v.isdigit() and int(sotuv_v_v) >= 0:
                                    
                                        sotuv_v_v = int(sotuv_v_v)
                                        malumot_ombori_v_v = sotuv_v_v
                                        sotuv[sotuv_k][sotuv_v_k] += sotuv_v_v
                                        Malumotlar_ombori[malumot_ombori_k][malumot_ombori_v_k] -= malumot_ombori_v_v
                                        break
                                    else:
                                        print("Miqdorni Noto'g'ri kiritdingiz ❌ ")
                            else:
                                print("Bizda bunday mahsulot mavjud emas ⚠ ")
                                pass
                        
                        
                        
                        
                        
                    elif int(enter) == 0:
                        break 
            #                              ______________ REPORT BO'LIMI _______________
            elif bolim == 4:
                while True:
                    print(("Bu yerda QO'SHILGAN/SOTILGAN mahsulotlar haqida ma'lumot olishingiz mumkin ").center(125))
                    report = input("'QOSHILGAN' mahsulotlar haqida ma'lumot uchun 1 ni bosing\n'SOTILGAN' mahsulotlar haqida ma'lumot uchun 2 ni bosing\n'ORTGA' 0 ni bosing\n >>> ")
                    if int(report) == 0:
                        break
                    elif report.isdigit() and int(report) == 1:
                        for key,value in qoshish.items():
                            print("\n\n",key.center(100))
                            print(100*"_") 
                            for key_2,value_2 in value.items():
                                print(f"{key_2} :" + str(value_2), end='  ')
                                

                    elif report.isdigit() and int(report) == 2:
                         for key,value in qoshish.items():
                            print("\n\n",key.center(100))
                            print(100*"_")
                            for key_2,value_2 in value.items():
                                print(f"{key_2} : " + str(value_2), end='  ')
    else:
        print("Login yoki passwordda xatolik ♻ \n\n" )
        continue
                            
                         
                                




