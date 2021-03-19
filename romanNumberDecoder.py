roman = {
        "I":1,
        "IV":4,
        "V":5,
        "IX":9,
        "X":10,
        "XL":40,
        "L":50,
        "XC":90,
        "C":100,
        "CD":400,
        "D":500,
        "CM":900,
        "M":1000
    }
l = [key for key in roman]
def decoder(stringr):
    global roman
    global l
    num1= 0
    listofpositions = []
    k = ""
    sr = ""
    for i in range(len(stringr)-1):
        sr += stringr[i]+stringr[i+1]
        if sr in l:
            num1 += roman[sr]
            listofpositions.append(i)
            listofpositions.append(i+1)
        sr = k
    for i in range(len(stringr)):
        if i in listofpositions:
            continue
        else:
            num1 += roman[stringr[i]]
    print(listofpositions)
    return num1
