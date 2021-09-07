
import itertools
# =============================================================================
# Read The data from the file
# =============================================================================
f = open("specialtext.txt", "r", encoding="utf-8")
if f.mode =="r":
    data = f.read()

# Special Character Dataset
# =============================================================================
# Output Result Array Defination
# =============================================================================
c1 = ['A','C','D','E','F','H','I','K','M','N','O','P','S','T','Y','a','c','d','e','g','h','i','j','p','s']
c2 = ['Α','С','Ⅾ','Е','Ϝ','Н','Ι','Κ','Μ','Ν','О','Р','Ѕ','Т','Ү','а','с','ԁ','е','𝗀','հ','і','ϳ','р','ѕ']
result = []

# =============================================================================
# Data traversing Loop
# =============================================================================
for i in range(len(data)):
    spn = '0'
    if ord(data[i]) == 6158 or ord(data[i]) == 8288 or ord(data[i]) == 8239:
        
        if ord(data[i]) == 6158 and ord(data[i-1]) == 8196 and ord(data[i+1]) != 8288 :
            spn = '1'
        if ord(data[i]) == 6158 and ord(data[i-1])==8201 and ord(data[i+1]) != 8288:
            spn = '2'
        if ord(data[i]) == 6158 and ord(data[i-1])==8200 and ord(data[i+1]) != 8288:
            spn = '3'
        if ord(data[i]) == 6158 and ord(data[i-1])==8287 and ord(data[i+1]) != 8288:
            spn = '4'
        if ord(data[i]) == 8288 and ord(data[i-1])==8196 and ord(data[i+1]) != 6158:
            spn = '5'
        if ord(data[i]) == 8288 and ord(data[i-1])==8201 and ord(data[i+1]) != 6158:
            spn = '6'
        if ord(data[i]) == 8288 and ord(data[i-1])==8200 and ord(data[i+1]) != 6158:
            spn = '7'
        if ord(data[i]) == 8288 and ord(data[i-1])== 8287 and ord(data[i+1]) != 6158:
            spn = '8'
        if ord(data[i]) == 6158 and ord(data[i-1]) == 8196 and ord(data[i+1]) == 8288:
            spn = '9'
        
        
        if ord(data[i]) == 6158 and ord(data[i-1])==8201 and ord(data[i+1]) == 8288:
            spn = '10'
        
        
        if ord(data[i]) == 6158 and ord(data[i-1])==8200 and ord(data[i+1]) == 8288:
            spn = '11'
        
        if ord(data[i]) == 6158 and ord(data[i-1])==8287 and ord(data[i+1]) == 8288:
            spn = '12'
        
        if ord(data[i]) == 8288 and ord(data[i-1])==8196 and ord(data[i+1]) == 6158:
            spn = '13'
        
        if ord(data[i]) == 8288 and ord(data[i-1])==8201 and ord(data[i+1]) == 6158:
            spn = '14'
        
        if ord(data[i]) == 8288 and ord(data[i-1]) == 8200 and ord(data[i+1]) == 6158:
            spn = '15'
        
        
        if ord(data[i]) == 8288 and ord(data[i-1]) == 8287 and ord(data[i+1]) == 6158:
            spn = '16'
        
        if ord(data[i]) == 8239:
            spn = '17'
       
        backind = data[0 : i]
        extract=backind.split()[-1]
        #print(extract)
        fl=0
        for item in range(len(c2)):
            #print(spn)
            if extract.find(c2[item])>=0:
                #print(c2[item])
                
                fl = 1
                if spn == '1':
                    result.append('10000')
                if spn == '2':
                    result.append('10001')
                if spn == '3':
                    result.append('10010')
                if spn == '4':
                    result.append('10011')
                if spn == '5':
                    result.append('10100')
                if spn == '6':
                    result.append('10101')
                if spn == '7':
                    result.append('10110')
                if spn == '8':
                    result.append('10111')
                if spn == '9':
                    result.append('11000')
                if spn == '10':
                    result.append('11001')
                if spn == '11':
                    result.append('11010')
                if spn == '12':
                    result.append('11011')
                if spn == '13':
                    result.append('11100')
                if spn == '14':
                    result.append('11101')
                if spn == '15':
                    result.append('11110')
                if spn == '16':
                    result.append('11111')
                if spn == '17':
                    result.append('1')    
                
                break
        if fl == 0:
            for item in range(len(c1)):
                #print(spn)
                #print(c1[item])
                if extract.find(c1[item]) >= 0:
                    if spn == '1':
                        result.append('00000')
                    if spn == '2':
                        result.append('00001')
                    if spn == '3':
                        result.append('00010')
                    if spn == '4':
                        result.append('00011')
                    if spn == '5':
                        result.append('00100')
                    if spn == '6':
                         result.append('00101')
                    if spn == '7':
                        result.append('00110')
                    if spn == '8':
                         result.append('00111')
                    if spn == '9':
                        result.append('01000')
                    if spn == '10':
                        result.append('01001')
                    if spn == '11':
                        result.append('01010')
                    if spn == '12':
                        result.append('01011')
                    if spn == '13':
                        result.append('01100')
                    if spn == '14':
                        result.append('01101')
                    if spn == '15':
                        result.append('01110')
                    if spn == '16':
                        result.append('01111')
                    if spn == '17':
                        result.append('0') 
                        
                    break
        
    
# =============================================================================
# Result Representation Part:
# =============================================================================
print("Result in List Form : ")
print(result)
str1 = ''.join(str(e) for e in result)

#Result length:
print("Result Length: ")
print(len(str1))
# =============================================================================
#print every 8 bits:
#print("Every 8 bits: ")
chopper =0
for item in range(len(str1)):
    chopper = chopper+1
    #print(str1[item], end=" ")
    if chopper == 8:
       # print('\n')
        chopper =0

#==============================================================================

## New Block of Code

#def text_from_bits(str1, encoding='utf-8', errors='surrogatepass'):
#    n = int(str1, 2)
#    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

##New Block of Code

n = int(str1, 2)
tres =n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
print("Result in decoded form: ")

print(tres)
    
    
