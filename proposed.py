import random
import timeit

start = timeit.default_timer()
mynewchar=['wQ','hW','kK','tT','Mi','rP','sG','Bb','kC','89',
           '567','53','LQQ','Hj','CF','GhS','K0q','16','lBB','Jp',
           'hM','hG','Jh','tNN','SKs','rTa','jSc','wKa','jGA','Hxz',
           'kZ2','33s','99T','McB','KVSD','CD3','gq)','jGa','ee3','FA<',
           '<F>','K;','*ES^','kG','hg2','mxZ','KCb','hjs','67w','113d',
           'uws','fhd4','670','l<','hZ!','al)','lxZ','%C','%F','%S',
           'V^','&F&','*D','0)','<,','>>','||','=!',';',':',
           '*','-','(',')','09','88','77','76','73','=','x%',
           '~~','g#','ds!','@!','^^','0&','33','22','z.','c%',
           'µ','¶','·','¸','¹','º','»','¼','½','¾',
           '¡','¢','£','¤','¥','¦','§','¨','©','ª',
           'a$','nm','--','[','+','.,','%^','b','K','v',
           'x','{','-','2','2x','+c','95','au','bL','w',
           '@f','-_',']','5','u','q','an','n,','l','z',
           'J','53','8','21','L','z.','ze','r','g','vx',
           '%a','43','ar','vk','mc','00','dk','fk','ak','sm',
           '«','32','hm','bc','m','ry','aa','k.','r1','y0'
           ':)',':(','fl','sk','sy','::','h^','(.)','st','mx',
           'nl','sz','ps','ma','{}','__','n$','pi','rd','az',
           'kl','br','sM','()','@$','=+','-=','1.','jd','jv',
           'cv','0A','i7','aa','§a',';;','v©','sc','bm','*%',
           'rm','1v','ad','¶¶','º3','}}','w§','!!','($','~f',
           'te','4E','es','kr','¨¨','[¤','07','f©','2¾','11',
           'xx','-1','sb','aw','67','¤]','150','44','1(','#4',
           'nu','-5.5','mr','jn','º2','d©','i7','3¾','9Z','Lq',
           'yy','C3','in','&^','¤;','pH','s©','bL','cK','dW',
           'rr','C#','nz','dg','¤:','º1','csk','mI','4¾','gL',
           'vr','p4','hz','§i','f@','mk','*5#','ry','hi','1¾',
           'cr','q9','sr',"''",'{{','ºy','§l','l2','ol','zx','ii',
           'LKA','FO0','56S','6DA','78CA','9Sa','89S','78&','&$0','0&d']

text=input("Enter a word:")
l=list(text)
list1=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
p=random.choice(list1)
q=random.choice(list1)
print(p,q)
n=(p*q)
pin=(p-1)*(q-1)


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def coprime(a, b):
    return gcd(a, b) == 1
for i in range(0,1000):
    e=random.randint(2,pin)
    if coprime(e,pin):
        print("yes",e,pin)
        break
print("success")

for j in range(0,100000):
        if ((e*j)%pin)==1:
            d=j
            break
print("d=",d)
l2=[]
l3=[]
l4=[]
#for g in range(len(l)):
#    print(ord(l[g]),end=" ")
#print()

##encryption
for k in range(len(l)):
    temp1=(ord(l[k]))
    temp2=((temp1**e)%n)%300
    temp3=((temp1**e)%n)//300
    #print("values:",temp2)
    l2.append(mynewchar[temp2])
    l4.append(temp3)

print("ENCRYPTION:")
for g in range(len(l2)):
    print(l2[g],end="")
print()

#print("q:")
#print(l4)
##decryption           
for c in range(len(l2)):
    temp1=(mynewchar.index(l2[c]))
    #print("index:",temp1)
    temp3=((300*(l4[c]))+temp1)
    temp2=(temp3**d)%n
    l3.append(chr(temp2))
print("DECRYPTION:")    
for g in range(len(l)):
    print(l3[g],end=" ")
print()

stop = timeit.default_timer()

print (stop - start )
