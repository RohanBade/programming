roman = {
        1:"I",
        4: "IV",
        5:"V",
        9:"IX",
        10:"X",
        40:"XL",
        50:"L",
        90:"XC",
        100:"C",
        400:"CD",
        500:"D",
        900: "CM",
        1000:"M",
        
    }
l = [1,4,5,9,10,40,50,90,100,400,500,900,1000,4000]
def solution(n):
    st = ""
    k = n
    while k >0:
        i = -1
        p = 0
        
        while l[p] <= k:
	        p += 1 
	        i += 1
        st += roman[l[i]]
        k -= l[i]
    return st

print(solution(3058))
