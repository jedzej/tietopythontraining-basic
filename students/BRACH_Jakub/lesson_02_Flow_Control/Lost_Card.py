card_qty = int(input())
checksum = 0
c = 0
for c in range(1, card_qty+1):
    checksum = checksum + c
for c in range(1, card_qty):
    checksum = checksum - int(input())
print(checksum)
