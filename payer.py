a=["monika"]
l =[]
dic = {}
for i in a: 
    for j in i:
        l.append(j)
# print(l)
i = 0
for x in l:
    dic.update({x:i})
    i+=1
print(dic)