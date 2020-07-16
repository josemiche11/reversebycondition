'''
Input- zoho123
Output- ohoz123

'''
char= input("Enter the string: ")
char2= list(char)
num= "1234567890"
list1= [0]*len(char)
list2=[]
for i in range(len(char)):
    if char2[i] not in num:
        list2.append( char2.index( char2[i]))
        char2[i]= "*"
list2.reverse()
k=0
for j in range( len(char) ):
    if j in list2:
        list1[j]= char[list2[k]]
        k= k+1
    else:
        list1[j]= char[j]
ch=""
for l in range(len(list1)):
    ch= ch+ list1[l]
print(ch)
