#Asking user the value of m and n.

n=int(input("Enter the value of n:"))
m=int(input("Enter the value of m:"))
text=""

#Reading the content inside the file named raw_text.txt 
#Assigning the content inside the file to variable named file1

with open ("raw_text.txt","r") as file:
  file1=file.read()
  

# Writing syntax  to encrypt the content of the file according to question.

for char in file1:
    ordervalue=ord(char)
    if ord('a') <= ordervalue <= ord('m'):
        ciphervalue = ordervalue+(n*m)
        while ciphervalue > ord('m'):
         ciphervalue = ord('a') + (ciphervalue - ord('m') - 1)

    elif ord('n') <= ordervalue <= ord('z'): 
        ciphervalue = ordervalue-(n+m)
        while ciphervalue<ord('n'):
          ciphervalue=ord('z')-(ord('n')-ciphervalue-1)
          
    elif ord('A') <= ordervalue <= ord('M'):
        ciphervalue = ordervalue-n
        while ciphervalue<ord('A'):
           ciphervalue=ord('M')-(ord('A')-ciphervalue-1)
           
    elif ord('N') <= ordervalue <= ord('Z'):
        ciphervalue=ordervalue+(pow(m,2))
        while ciphervalue > ord('Z'):
         ciphervalue = ord('N') + (ciphervalue - ord('Z') - 1)
         
    else:
        ciphervalue=ordervalue

    text+=chr(ciphervalue)

#Writing the encrypted content to the file named encrypted_text.txt

with open ("encrypted_text.txt", "w") as file:
    file.write(text)
    print("Encrypted text written to the new file named encrypted_text.txt.")
    
# Creating a function to decrypt the encrypted text.

def decrypt_text(n,m):
    text_2=""
    
#reading the content  inside the encrypted_text.txt and doing syntax for decryption

    with open ("encrypted_text.txt","r") as file:
       file2=file.read()
    

    for char in file2:
       ordervalue=ord(char)
       if ord('a') <= ordervalue <= ord('m'):
           ciphervalue = ordervalue-(n*m)
           while ciphervalue < ord('a'):
            ciphervalue = ord('m') - (ord('a')-ciphervalue-1)

       elif ord('n') <= ordervalue <= ord('z'): 
           ciphervalue = ordervalue+(n+m)
           while ciphervalue>ord('z'):
             ciphervalue=ord('n') + (ciphervalue - ord('z') - 1)
          
       elif ord('A') <= ordervalue <= ord('M'):
          ciphervalue = ordervalue+n
          while ciphervalue>ord('M'):
              ciphervalue = ord('A') + (ciphervalue - ord('M') - 1)
           
       elif ord('N') <= ordervalue <= ord('Z'):
           ciphervalue=ordervalue-(pow(m,2))
           while ciphervalue < ord('N'):
            ciphervalue=ord('Z')-(ord('N')-ciphervalue-1)
         
       else:
           ciphervalue=ordervalue
        
       text_2+=chr(ciphervalue)
#writing decrypted content in a file named decrypted_text.txt
    with open ("decrypted_text.txt","w") as file:
       file.write(text_2)
       print("Decrypted text written to new file decrypted_text.txt .")
    return file2
decrypt_text(n,m)

#Checking the correctness of the decrypted content.

def check_correctness():
    with open ("raw_text.txt","r") as file:
         content_1=file.read()
         
    with open ("decrypted_text.txt","r") as file:
        content_2=file.read()
    
    if content_1==content_2:
        print("The decrypted text is correct.")
    
    else:
        print("The decrypted text is incorrect.")
        
check_correctness()
        
        
         
   
     



        
    
    