#Shift Cypher or Caesar Cypher Algorithm
def shiftCypher(text,shift):
    encrypt_s=""
    i=shift
    for c in text:
        x=ord(c)
        if(x not in range(65,91) and x not in range(97,123)):
            encrypt_s+=c
            continue
        else:
            if x in range (65,91):
                x=x+i
                while(x>90):
                    x=x-26
                
            if x in range(97,123):
                x=x+i
                while(x>122):
                    x=x-26
            encrypt_s+=chr(x)

    return encrypt_s

#Decimal to any Base from 2 t0 36 Change Algorithm
def baseChange(text,Base):
    text=text+" "
    encrypt_s=""
    num=0
    for ind in range(0,len(text)):
        x=ord(text[ind])
        if(x not in range(48,58) ):
            encrypt_s+=text[ind]
            continue
        else:
            if(ord(text[ind+1]) not in range (48,58) ):
                num=(num*10)+(x-48)
                encrypt_s+=str(dec_to_base(num,Base))
                num=0
                
            elif ord(text[ind+1]) in range (48,58):
                num=(num*10)+(x-48)
                continue
            

    return encrypt_s

#Function to convert decimal to any other base from 2 to 36
def dec_to_base(num,base):  #Maximum base - 36
    base_num = ""
    while num>0:
        dig = int(num%base)
        if dig<10:
            base_num += str(dig)
        else:
            base_num += chr(ord('A')+dig-10)  #Using uppercase letters
        num //= base
    base_num = base_num[::-1]  #To reverse the string
    return base_num

#Hill Cipher Character Set of size 73
hc_Char=['0','1','2','3','4','5','6','7','8','9',' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',',','\'','.','!','?','*','\"','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','-',';','\n']

#Function to multiply matrix and get its modulous 
def multiMatrix(chrMatrix,keyMatrix):
    K=keyMatrix
    d=chrMatrix
    res=[0,0,0]
    res[0]=(K[0][0]*d[0])+(K[0][1]*d[1])+(K[0][2]*d[2])
    res[1]=(K[1][0]*d[0])+(K[1][1]*d[1])+(K[1][2]*d[2])
    res[2]=(K[2][0]*d[0])+(K[2][1]*d[1])+(K[2][2]*d[2])
    
    res[0]=(res[0]%73)
    res[1]=(res[1]%73)
    res[2]=(res[2]%73)
    
    return res

#Primary Hill Cipher Function
def HillCipher(string,key):
    if(len(string)%9!=0):
        string=string+"x"*(9-(len(string)%9))
    keyMatrix=[[0,0,0],[0,0,0],[0,0,0]]
    encryptStr=""
    k=0
    for i in range(0,3):
        for j in range(0,3):
            d=hc_Char.index(key[k])
            keyMatrix[i][j]=d
            k=k+1
    if(len(string)%3!=0):
        string=string+("x"*(3-(len(string)%3)))
    chrMatrix=[]
    
    for i in range(0,len(string),3):
        chrMatrix=[]
        for j in range(i,i+3):
            d=hc_Char.index(string[j])  
            chrMatrix.append(d)
           
        res=multiMatrix(chrMatrix,keyMatrix)
        tempStr=hc_Char[res[0]]+""+hc_Char[res[1]]+""+hc_Char[res[2]]
        encryptStr+=tempStr

    return encryptStr

#Playfair Cipher
def matrix(x,y,initial):
    return [[initial for i in range(x)] for j in range(y)]


def locindex(c,my_matrix): #get location of each character
    loc=list()
    if c=='J':
        c='I'
    for i ,j in enumerate(my_matrix):
        for k,l in enumerate(j):
            if c==l:
                loc.append(i)
                loc.append(k)
                return loc

def encrypt(msg):  #Encryption
    key=input("Enter the key :")
    key=key.replace(" ", "")
    key=key.upper()
    result=list()
    for c in key: #storing key
        if c not in result:
            if c=='J':
                result.append('I')
            else:
                result.append(c)
    flag=0
    for i in range(65,91): #storing other character
        if chr(i) not in result:
            if i==73 and chr(74) not in result:
                result.append("I")
                flag=1
            elif flag==0 and i==73 or i==74:
                pass    
            else:
                result.append(chr(i))
    k=0
    my_matrix=matrix(5,5,0) #initialize matrix
    for i in range(0,5): #making matrix
        for j in range(0,5):
            my_matrix[i][j]=result[k]
            k+=1

    msg=msg.upper()
    msg=msg.replace(" ", "")
    msg=msg.replace("\n","")
    i=0
    for s in range(0,len(msg)+1,2):
        if s<len(msg)-1:
            if msg[s]==msg[s+1]:
                msg=msg[:s+1]+'X'+msg[s+1:]
    if len(msg)%2!=0:
        msg=msg[:]+'X'
    out=""
    while i<len(msg):
        loc=list()
        loc=locindex(msg[i],my_matrix)
        loc1=list()
        loc1=locindex(msg[i+1],my_matrix)
        if loc[1]==loc1[1]:
            out+=str(my_matrix[(loc[0]+1)%5][loc[1]])+str(my_matrix[(loc1[0]+1)%5][loc1[1]])+' '
        elif loc[0]==loc1[0]:
            out+=str(my_matrix[loc[0]][(loc[1]+1)%5])+str(my_matrix[loc1[0]][(loc1[1]+1)%5])+ ' '
        else:
            out+=str(my_matrix[loc[0]][loc1[1]])+str(my_matrix[loc1[0]][loc[1]])+' '    
        i=i+2
    return out 



#Main function for Cypher Selection
def main(string):
    print("Enter The Encryption Technique of Your Choice:-")
    print("1. Shift Cypher")
    print("2. Number Base Change")
    print("3. Hill Cypher")
    choice=input()
    out=""
    if(choice=='1'):
        shift=int(input("Enter Number For Shift \n"))
        out=shiftCypher(string,shift) #Applying Shift Cypher
        print(out)
    elif(choice=='2'):
        base=int(input("Enter The New Base \n"))
        out=baseChange(string,base)  #Applying Base Change
    elif(choice=='3'):
        key=input("Enter a key of length 9 \n")
        out=HillCipher(string,key)
    else:
        print("Invalid Input , Enter A Valid Input between 1 and 3 \n")
        out=main(string)
    
    return out
    
    
    
    
    
    
if __name__== "__main__":
    print("____________________________________________________________________________________________________________________________________")
    print("____________________________________________________________________________________________________________________________________")
    print()
    print("                                   WELCOME TO THE CUSTOM TEXT ENCRYPTER                               ")
    print("                 You can apply any Custom Encryption to your text file using this program ")
    print("                 The users inputs the path file, encryption technique and encryption key of their own choice")
    print("         It also supports compound encryption, you can apply encryption to encypted text to multiply the strength of Encryption ")
    print("____________________________________________________________________________________________________________________________________")
    print("____________________________________________________________________________________________________________________________________")
    print()
    print("Enter the path of your File :")
    path=input()
    string = open(path, 'r').read()
    out=main(string)
    print("Your text has been sucessfully encrypted !!!")
    print("To strengthen the Encryption, You can perform compound Encryption by applying another encryption to this encrypted file")
    print("If you want to apply compund encryption, Enter 1")
    print("If you want to save the file, Enter 0")
    flag=input()
    while(flag=='1'):
        out=main(out)
        print("Your text has been sucessfully encrypted !!!")
        print("If you want to apply compund encryption, Enter 1 \n")
        print("If you want to save the file, Enter 0 \n")
        flag=input()
    print("Text has been Encrypted and The Text File is Saved \n")
    print("Enter the file name with which you want to save the file (Example - encrypted.txt) \n")
    filename=input()
    f=open(filename,"w+")
    f=open(filename,"a+")
    f.write(out)
    f.close()
    
