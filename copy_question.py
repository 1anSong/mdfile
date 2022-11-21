import copy
####情况1
a = [1,2,3]
b=a
a=[]
#a.append(1) ## 思考题
print(b)

####情况2
a = [1,2,3]
b=a.copy()
a=[]
#print(b)

####情况3
a = [1,2,3]
b=a
a.append(4)
#print(b)

####情况4
a = [1,2,3]
b=a.copy()
a.append(4)
#print(b)


####情况5
a = [1,2,3]
b=copy.deepcopy(a)
a=[0]
#print(b)

####情况6
a = [1,2,3]
b=copy.deepcopy(a)
a.append(4)
#print(b)

print('------------------')

a = {1:[1,2,3]}
b=a
a={1:[]}
print(b)

a = [1,2,3]
b=a
a[1].append(4)
print(b)
