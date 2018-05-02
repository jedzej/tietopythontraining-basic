thelargest = int(input())
thesecond = int(input())
if thesecond > thelargest:
    thelargest, thesecond = thesecond, thelargest
i = int(input())
while i != 0:
    if i > thelargest:
        thesecond, thelargest = thelargest, i
    elif i > thesecond:
        thesecond = i
    i = int(input())
print(thesecond)
