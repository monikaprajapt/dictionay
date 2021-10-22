# from heapq import nlargest
# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}  
# three_largest = nlargest(3, my_dict, key=my_dict.get)
# print(three_largest) 


str=input("enter the string:")
# print(str)
count={}
for i in str:
    if i in count.keys():
        count[i]+=1
    else:
        count[i]=1
print(count)




# my_dict = {
#     'a':50,
#     'b':58,
#     'c':56,
#     'd':40,
#     'e':100,
#     'f':20
#     }
# for i in my_dict:
    










