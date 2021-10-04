l=[]
j=[]
paths ="E:\Programming Source Codes\Python\sample.py"
for i in paths:
    l.append(i)
y=len(l) 
n=0 
for i in range(0,len(l)):
    if(l[i]=="\\"):
        j.append(i)
x=j[len(j)-1]
for i in range (x+1,y):
    print(l[i], end=" ")
    
  
        


    

             
             
  
