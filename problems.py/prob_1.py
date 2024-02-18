# Check the sentence: "All digits of this number must be different"

# input: 1221
# output: Wrong!

# input: 37526
# output: Correct!

num = int(input("Please, Enter the numbers: "))

if len(str(num)) == len(set(str(num))):
    print("It is different!")
else:
    print("It is not different!!!")
