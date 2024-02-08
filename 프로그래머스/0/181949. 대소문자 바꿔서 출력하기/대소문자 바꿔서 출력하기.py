str = input()
result = ""
for i in str :
    if i.isupper() :
        i = i.lower()
    else :
        i = i.upper()
    result += i
    
print(result)

