cmpl1=3
cmpl2=6

print(cmpl1+cmpl2)
#output=9

print(cmpl1-cmpl2)
#output=-3

print(cmpl1*cmpl2)
#output=18

print(cmpl1**cmpl2)
#output=729

print(cmpl1//cmpl2)
#output=0




#Boolean -true/false

print(2>3)
 # output=False

print(2>=3)
#output=False

print(2<=3)
#output=True

bool1=True
print(type(bool1))
#output=<class'bool'>

print(type(False))
#output=class'bool'

print(int(True))
#output=1

print(int(False))
#output=0

#sequences-list,tuple,string,range
# list = collection of hetrogenous elements Which are indexable and mutable    changesss avuthundhi possible

list1= [1,2,3,4,'sum',67,89,78,[3,4,89,]]

print(type(list))
#output=<class'type'>

print(list1)
#output=[1,2,3,4,'sum',67,89,78,[3,4,89,]]

print(list1[4])
#output=sum

print(list1[5])
#output=67

print(list1[1:7:2])
#output=[2,4,67]

print(list1[1:7:3])
#output=[2,sum,]

#tuple-() Immutable not changes

tupl=(1,2,True,"strl",0.9)

print(tupl[1])
#output=2

print(tupl[4])
#output=0.9

print(tupl[3])
#output=strl


#Tuple is faster than list


# range 
# range is used to print numbers
# useing for loop

for i in range(0,100):
    print(i)
    #output=1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40