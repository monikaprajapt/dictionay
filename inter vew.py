# c={}
# for i in range(1,5):
#     user=input("enter the key")
#     user1=int(input("enter the value"))
#     c[user]=user1
# print(c)


d={'a':20,'b':40,'c':{'1':11,'2':12,'4':15,'5':{'d':5,'e':10}}}
sum=0
for i in d.values():
    if type(i)==dict:
        for j in i.values():
            if type(j)==dict:
                for k in j.values():
                    sum+=k
            else:
                sum+=j
    else:
        sum+=i
print(sum)





# a=[1,2,4,2,1,3,3,2,4,5,2]
# x = {} 
# for i in a:
#     y = a.count(i)
#     x.update({i:y//2})
# print(x)

























