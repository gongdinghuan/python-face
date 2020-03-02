



print("yyyyy")

print("中国，hello python")
print("中国，")
print("he1lo python")

num=3
if num == 3:
    print('num = 3')
else:
    print('end ')

li1=[7,9,1,4,5]
li2=[]
li3=[]
for i in li1:
    if i==5:
        break
    elif i<5:
        li2.append(i)
    else:
        li3.append(i)
else:
    print(li2)

print("li2=");print(li2)
print("li3");print(li3)

x=1
while x<10:
    print(x)
    x+=1