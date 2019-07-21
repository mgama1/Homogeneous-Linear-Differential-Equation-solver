import numpy as np
import cmath
coeff=[]
sol=[]
distReal="C.e^{r}X"
distcomplx="e^{a}X(C.COS({b}X)+C.SIN({b}X))"
n=input("Enter the differential equation's degree: ")

while n>=0:
    coeff.append(input("enter the coefficients: "))
    n=n-1

print "coefficients are : " , coeff    

roots=np.roots(coeff)
roots=np.around(roots,decimals=2)
              
#roots= np.sort(roots)


def isDIst(roots):
    if len(roots)==len(np.unique(roots)):
        return True
    else:
        return False
       

            
def isReal(roots):
    return roots.imag==0

def isComplex(roots):
    return roots.imag!=0


    
Dist=isDIst(roots)
Real=isReal(roots)
complx=isComplex(roots)

if Real.any():
    
    i=0
    while i<len(roots):
        if roots[i].imag==0:
            
        
            sol.append(distReal.format(k=i, r=roots[i]))
        i=i+1

    
    


if complx.any():
    
    i=0
    while i<len(roots):
        
        if roots[i].imag!=0:
            sol
            sol.append(distcomplx.format(a=roots[i].real,b=abs(roots[i].imag)))
    
        i=i+1
    
    
    
    

if not Dist :
    i=0
    k=0
    reap=len(roots)-len(np.unique(roots))
    if roots[i].imag==0:
        while k<reap:
            s=sol[0]
            s=s.replace("C.","C.x^"+str(k+1))
            sol=np.append(sol,s)
            sol[k+1]=s
            k=k+1
    else:
        k=0
        reap=len(roots)-len(np.unique(roots))-1
        while k<reap:
            
            s=sol[0]
            s="X"+s
            sol=np.append(sol,s)
            sol[k+1]=s
            k=k+1
    
sol=np.unique(sol)    
sol =" + ".join(sol)
sol=sol.replace("1.0X","X")
sol=sol.replace("e^0.0X","")
sol=sol.replace("+0j","")
print "roots are" , roots

print "Distinct? " , isDIst(roots)
print "Real?" , isReal(roots)
print "sol is : " , sol


#input("")
