def convert(number):
    out=''
    if number%3==0:
        out+='Pling'
    if number%5==0:
        out+='Plang'
    if number%7==0:
        out+='Plong'
    if (number%3!=0) and (number%5!=0) and (number%7!=0):
        out=str(number)
    return out
