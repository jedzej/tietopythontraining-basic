n = int(input('n: '))

k = 2
fcn = 1
adding = 1
while k <= n:
    fcn = fcn * k
    k += 1
    adding = adding + fcn

print(adding)
