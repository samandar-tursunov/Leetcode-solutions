# Check the sentence: "All digits of this number must be different"

# input: 1221
# output: Wrong!

# input: 37526
# output: Correct!

# num = int(input("Please, Enter the numbers: "))

# if len(str(num)) == len(set(str(num))):
#     print("It is different!")
# else:
#     print("It is not different!!!")

from itertools import permutations

# Harf-rakam eşleştirmesi
letter_to_digit = {'I': '1', 'D': '4', 'C': '9', 'M': '9', 'O': '6'}

# IDC ve IMO kelimelerinin sayısal değerlerini oluşturma
idc_digits = ''.join(letter_to_digit[letter] for letter in 'IDC')
imo_digits = ''.join(letter_to_digit[letter] for letter in 'IMO')

# Tüm permütasyonları kontrol etme
count = 0
for perm_idc in permutations(idc_digits):
    for perm_imo in permutations(imo_digits):
        if int(''.join(perm_idc)) > int(''.join(perm_imo)):
            count += 1

print("Tengsizliğin çözüm sayısı:", count)