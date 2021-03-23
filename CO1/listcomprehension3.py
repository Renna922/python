#a)
list=[1,-2,9,-3,0,-6,8,4,7]
newlist=[x for x in list if x>0]
print(newlist)
#b)
num=int(input("enter number of nos:"))
list=[]
for x in range(num):
    x=int(input("enter the number:"))
    list.append(x)
print(list)
squarelist=[x**2 for x in list]
print(squarelist)
#c)
word="mango"
vowels="aeiou"
list=[x for x in word if x in vowels]
print(list)
#d)
word="fruits"
list=[ord(x) for x in word]
print(list)
