dic1={1:10,2:40}
dic2={3:13,2:20}
dict3={4:20,5:30}
for key in dic2:
    if key in dic1:
        dic1[key]=dic1[key]+dic2[key]
        dic1.update(dict3)
    else:
        dic1[key]=dic2[key]
print(dic1)

