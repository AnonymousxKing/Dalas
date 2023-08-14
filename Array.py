array=[12,45,54,65,65,25,89,98,100]
print(array[6])
print("What Do You Want")
print("1-Check Entry By index")
print("2- Make Entry By index")
print("Enter Your Choise:")
e=int(input())
if e==1:
   print("Enter the Index That You Want To Check")
   i=int(input())
   p=len(array)
   print("You Chose "+str(e)+"." )
   if i<=len(array):    
    print("Value of Array at index "+str(i)+" is " +str(array[i])+" .")  
   else:
    print("Range Is Out Of Array")
    print("please Enter The Range From 0 To "+str(p)+".")
elif e==2:
   print("You Chose "+str(e)+".")
   print("===================================Adding A Entry================================")
   print("Enter The Index Where You Want To Put That Number")
   index=str(input())
   print("Enter The Number DO You Want To ADD")
   number=str(input())
   array.insert(int(index),int(number))
   print("The Value "+number+" Has Been Inserted In "+index )

   




