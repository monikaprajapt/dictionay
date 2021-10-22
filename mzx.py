# my_dict = {'data1':100,'data2':-54,'data3':247}
# v=1
# for i in my_dict:    
#     v=v * my_dict[i]
# print(v)


# myDict = {'a':1,'b':2,'c':3,'d':4}
# # print(myDict)
# if 'b' in myDict: 
#     del myDict['b']
# print(myDict)



# color_dict = {'red':'#FF0000',
#           'green':'#008000',
#           'black':'#000000',
#           'white':'#FFFFFF'}

# for key in sorted(color_dict):
#     print("%s: %s" % (key, color_dict[key]))






# my_dict = {'x':500, 'y':5874, 'z': 560,'a':123}

# key_max = max(my_dict.keys(), key=(lambda key: my_dict[key]))
# # # key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

# print('Maximum Value: ',my_dict[key_max])
# # # print('Minimum Value: ',my_dict[key_min])


# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d =  Counter(d1) + Counter(d2)
# print(d)

# from collections import Counter
# 

# L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# # print("Original List: ",L)
# value = set( val for dic in L for val in dic.values())
# print("Unique Values: ",value)



     




# # from collections import defaultdict, Counter
# str1 = 'w4monika'
# str1=input("enter the name")
# my_dict = {}
# for i in str1:
#     my_dict[i] = my_dict.get(i,5)
# print(my_dict)




# user=input("enter the key")
# user1=(input("enter the key"))
# dict={'age':23,'age1':24,'age2':26,'age3':23}
# sum=0
# for i in dict.keys():
#     if user==i:
#         key1=i
# for i in dict.keys():
#     if user1==i:
#         key2=i
# sum=dict[key1]+dict[key2]

# print(sum)



# from heapq import nlargest
# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}  
# three_largest = nlargest(3, my_dict, key=my_dict.get)/
# # print(three_largest) 


# # 

      






# a=[1,2,3,[4,5,6,],23,[7,8,9]]
# i=0
# sum=0
# while i<len(a):
#     b=a[i]
#     if type(b) is list:
#         j=0
#         while j<len(b):
#             sum=sum+b[j]
#             j=j+1
#     else:
#         sum=sum+a[i]
#     i=i+1
# print(sum)

a={1:"monika",2:"sonu",3:"rani",4:"sita"}
# for i in a:
#     a[2]= "monu"
# print(a)
a[1]='aman'
print(a)