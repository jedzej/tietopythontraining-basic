#Statement
#Given an integer. Print its tens digit.
print("Please enter an integer value:")
a = int(input())
print("Ten digit is: " + str((a%100)//10))