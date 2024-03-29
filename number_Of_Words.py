str=input("Enter any string/statement:- ")
split=str.split()
dictionary={}
for i in split:
    if i in dictionary:
        dictionary[i]+=1
    else:
        dictionary[i]=1
print(dictionary)