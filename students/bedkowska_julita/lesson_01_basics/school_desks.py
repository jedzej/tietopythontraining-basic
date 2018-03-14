a = int(input("Class a: "))
b = int(input("Class b: "))
c = int(input("Class c: "))


def calc(num):
    return (num // 2) + num % 2


print(calc(a) + calc(b) + calc(c))
