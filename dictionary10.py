dict =  {

   'Alex': ['subj1', 'subj2', 'subj3'], 

   'David': ['subj1', 'subj2']}
sum=[]
count=0
for i in dict.values():
    sum=sum+i
# print(sum)
i=0
while i<len(sum):
    # a=sum[i]
    count=count+1
    i=i+1
print(count)


