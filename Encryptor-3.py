
print("Write the secret message You want to Hide >>")
text= input()
encoding='utf-8'
errors='surrogatepass'
bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
sequence = bits.zfill(8 * ((len(bits) + 7) // 8))
sh = len(sequence)
print("The bit stream needs to encode: " + sequence)
print("Total number of bits: {}".format(sh)) 
print("The stego-text is saved to stegofile.txt")



comp = ['10000', '10001', '10010', '10011','10100','10101','10110','10111', '11000', '11001', '11010', '11011','11100','11101','11110','11111','1']
words = []
res =""
dicti = {'00000':" ᠎",'10000':" ᠎",'00001':" ᠎",'10001':" ᠎", '00010':" ᠎", '10010':" ᠎",'00011':" ᠎", '10011':" ᠎", '00100':" ⁠", '10100':" ⁠",'00101':" ⁠",'10101':" ⁠",'00110':" ⁠",'10110':" ⁠",'00111':" ⁠",'10111':" ⁠",'01000':" ᠎⁠",'11000':" ᠎⁠",'01001':" ᠎⁠",'11001':" ᠎⁠",'01010':" ᠎⁠",'11010':" ᠎⁠",'01011':" ᠎⁠",'11011':" ᠎⁠",'01100':" ⁠᠎",'11100':" ⁠᠎",'01101':" ⁠᠎",'11101':" ⁠᠎",'01110':" ⁠᠎",'11110':" ⁠᠎", '01111':" ⁠᠎",'11111': " ⁠᠎",'0':" ",'1':" "}

#Read the plain text file
f = open("Newtext.txt", "r", encoding="utf-8-sig")
if f.mode =="r":
    text = f.read()


words = text.split()
#print(words)

c1 = ['A','C','D','E','F','H','I','K','M','N','O','P','S','T','Y','a','c','d','e','g','h','i','j','p','s']
c2 = ['Α','С','Ⅾ','Е','Ϝ','Н','Ι','Κ','Μ','Ν','О','Р','Ѕ','Т','Ү','а','с','ԁ','е','𝗀','հ','і','ϳ','р','ѕ']

kc = 0

for i in range(len(words)):
    
    for j in range(len(c1)):
        flag =0
        
        if words[i].find(c1[j])>=0 and sequence[kc: kc+5] in comp and len(sequence) - kc >=5:
            #print("kcc: {}".format(sequence[kc: kc+5]))
            katara =words[i].replace(c1[j], c2[j])
            res = res + katara+dicti.get(sequence[kc:kc+5])
            #print("res: {}".format(res))
            kc = kc+5
            flag=1
            #print("rc1: {}".format(res))
            break
        elif words[i].find(c1[j])>=0 and sequence[kc: kc+5] not in comp and len(sequence) - kc >=5:
            #print("kc: {}".format(sequence[kc: kc+3]))
            res = res + words[i]+dicti.get(sequence[kc:kc+5])
            #print("res: {}".format(res))
            kc = kc+5
            flag=1
            #print("rc2: {}".format(res))
            break;
        elif words[i].find(c1[j])>=0 and sequence[kc: kc+1] in comp and len(sequence) - kc <5 and len(sequence) - kc >0:
            #print("ko",sequence[kc: kc+1])
            katara =words[i].replace(c1[j], c2[j])
            res = res + katara+dicti.get(sequence[kc:kc+1])
            kc = kc+1
            flag=1
            #print("rc2: {}".format(res))
            break;
            
        elif words[i].find(c1[j])>=0 and sequence[kc: kc+1] not in comp and len(sequence) - kc <5 and len(sequence) - kc >0:
            
            res = res + words[i]+dicti.get(sequence[kc:kc+1])
            #print(res)
            kc = kc+1
            flag=1
            #print("rc2: {}".format(res))
            break;    
            
        
    if flag == 0:       
        res = res + words[i]+" "
            
    if kc >= len(sequence):
        break
    
if kc < len(sequence):
    print("Whole sequence is not been updated in result!")
print(res)

#Write data in the text file
text_file = open("specialtext.txt", "w", encoding="utf-8-sig")
n = text_file.write(res)
text_file.close()


        
            
    

    
