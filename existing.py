import timeit

start = timeit.default_timer()

A=[9,12,33,47,53,67,78,92]
B=[48,81]
C=[13,41,62]
D=[1,3,45,79]
E=[14,16,24,44,46,55,57,64,74,82,87,98]
F=[10,31]
G=[6,25]
H=[23,39,50,56,65,68]
I=[32,70,73,83,88,93]
J=[15]
K=[4]
L=[26,37,51,84]
M=[22,27]
N=[18,58,59,66,71,91]
O=[0,5,7,54,72,90,99]
P=[38,95]
Q=[94]
R=[29,35,40,42,77,80]
S=[11,19,36,76,86,96]
T=[17,20,30,43,49,69,75,85,97]
U=[8,61,63]
V=[34]
W=[60,89]
X=[28]
Y=[21,52]
Z=[2]

arrsp=['#']
count2=0
count1=0
count3=0
count4=0
count5=0
count6=0
count7=0
count8=0
count9=0
count10=0
count11=0
count12=0
count13=0
count14=0
count15=0
count16=0
count17=0
count18=0
count19=0
count20=0
count21=0
count22=0
count23=0
count24=0
count25=0
count26=0
count27=0


n=input("Enter a text:")
n=n.upper()
l=list(n)
l1=[]

#encryption

for i in range(len(l)):
    if l[i]== 'A':
        temp1=A[count1]
        l1.append(temp1)
        count1=count1+1
        if count1>=8:
            count1=0
    elif l[i]== "B":
        temp1=B[count2]
        l1.append(temp1)
        count2=count2+1
        if count2>=2:
            count2=0
    elif l[i]== "C":
        temp1=C[count3]
        l1.append(temp1)
        count3=count3+1
        if count3>=3:
            count3=0
    elif l[i]== "D":
        temp1=D[count4]
        l1.append(temp1)
        count4=count4+1
        if count4>=4:
            count4=0
    elif l[i]== "E":
        temp1=E[count5]
        l1.append(temp1)
        count5=count5+1
        if count5>=12:
            count5=0
    elif l[i]== "F":
        temp1=F[count6]
        l1.append(temp1)
        count6=count6+1
        if count6>=2:
            count6=0
    elif l[i]== "G":
        temp1=G[count7]
        l1.append(temp1)
        count7=count7+1
        if count7>=2:
            count7=0
    elif l[i]== "H":
        temp1=H[count8]
        l1.append(temp1)
        count8=count8+1
        if count8>=6:
            count8=0
    elif l[i]== "I":
        temp1=I[count9]
        l1.append(temp1)
        count9=count9+1
        if count9>=6:
            count9=0
    elif l[i]== "J":
        temp1=J[count10]
        l1.append(temp1)
        count10=count10+1
        if count10>=1:
            count10=0
    elif l[i]== "K":
        temp1=K[count11]
        l1.append(temp1)
        count11=count11+1
        if count11>=1:
            count11=0
    elif l[i]== "L":
        temp1=L[count12]
        l1.append(temp1)
        count12=count12+1
        if count12>=4:
            count12=0
    elif l[i]== "M":
        temp1=M[count13]
        l1.append(temp1)
        count13=count13+1
        if count13>=2:
            count13=0
    elif l[i]== "N":
        temp1=N[count14]
        l1.append(temp1)
        count14=count14+1
        if count14>=6:
            count14=0
    elif l[i]== "O":
        temp1=O[count15]
        l1.append(temp1)
        count15=count15+1
        if count15>=7:
            count15=0
    elif l[i]== "P":
        temp1=P[count16]
        l1.append(temp1)
        count16=count16+1
        if count16>=2:
            count16=0
    elif l[i]== "Q":
        temp1=Q[count17]
        l1.append(temp1)
        count17=count17+1
        if count17>=1:
            count17=0
    elif l[i]== "R":
        temp1=R[count18]
        l1.append(temp1)
        count18=count18+1
        if count18>=6:
            count18=0
    elif l[i]== "S":
        temp1=S[count19]
        l1.append(temp1)
        count19=count19+1
        if count19>=6:
            count19=0
    elif l[i]== "T":
        temp1=T[count20]
        l1.append(temp1)
        count20=count20+1
        if count20>=9:
            count20=0
    elif l[i]== "U":
        temp1=U[count21]
        l1.append(temp1)
        count21=count21+1
        if count21>=3:
            count21=0
    elif l[i]== "V":
        temp1=V[count22]
        l1.append(temp1)
        count22=count22+1
        if count22>=1:
            count22=0
    elif l[i]== "W":
        temp1=W[count23]
        l1.append(temp1)
        count23=count23+1
        if count23>=2:
            count23=0
    elif l[i]== "X":
        temp1=X[count24]
        l1.append(temp1)
        count24=count24+1
        if count24>=1:
            count24=0
    elif l[i]== "Y":
        temp1=Y[count25]
        l1.append(temp1)
        count25=count25+1
        if count25>=2:
            count25=0
    elif l[i]== "Z":
        temp1=Z[count26]
        l1.append(temp1)
        count26=count26+1
        if count26>=1:
            count26=0
    elif l[i]== " ":
        temp1=arrsp[count27]
        l1.append(temp1)
        count27=count27+1
        if count27>=1:
            count27=0
print("ENCRYPTION:")
print(l1)

j=[]
for i in range(len(l1)):
    if (l1[i] in A):   
          j.append('a')
    elif (l1[i] in B):
          j.append('b')
    elif (l1[i] in C):
          j.append('c')
    elif (l1[i] in D):
          j.append('d')
    elif (l1[i] in E):
          j.append('e')
    elif (l1[i] in F):
          j.append('f')
    elif (l1[i] in G):
          j.append('g')
    elif (l1[i] in H):
          j.append('h')
    elif (l1[i] in I):
          j.append('i')
    elif (l1[i] in J):
          j.append('j')
    elif (l1[i] in K):
          j.append('k')
    elif (l1[i] in L):
          j.append('l')
    elif (l1[i] in M):
          j.append('m')
    elif (l1[i] in N):
          j.append('n')
    elif (l1[i] in O):
          j.append('o')
    elif (l1[i] in P):
          j.append('p')
    elif (l1[i] in Q):
          j.append('q')
    elif (l1[i] in R):
          j.append('r')
    elif (l1[i] in S):
          j.append('s')
    elif (l1[i] in T):
          j.append('t')
    elif (l1[i] in U):
          j.append('u')
    elif (l1[i] in V):
          j.append('v')
    elif (l1[i] in W):
          j.append('w')
    elif (l1[i] in X):
          j.append('x')
    elif (l1[i] in Y):
          j.append('y')
    elif (l1[i] in Z):
          j.append('z')
    elif (l1[i] in arrsp):
          j.append(' ')



     
      
      
print("DECRYPTION:")
print(j)
      

stop = timeit.default_timer()
print (stop - start )

