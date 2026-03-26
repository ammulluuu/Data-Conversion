def DEC_BIN(n):
    bin=" "   #python takes binary as string values
    while n>0:
        b=n % 2        #to fetch reminder
        bin=str(b) + bin
        n=n//2         #to get quotient
    print("binary",bin)
def DEC_OCT(n):
    octal=" "         #octal,hexa,binary are number systems not default decimal numbers
    while n>0:         #so we assign them as string
        b=n % 8
        octal=str(b) + octal
        n=n//8
    print("Ocatl",octal)

def DEC_HEX(n):
    hexa=" "
    while n>0:
        s=n% 16
        hexa=str(s) + hexa
        n=n//16
    print("Hexadecimal",hexa)
def BIN_DEC(n):
    dec=0
    power=0
    for digit in n[: :-1]:         #it reverse string
        dec=dec + int(digit) * (2 ** power)
        power +=1
    print("DECIMAL",dec)
def BIN_OCT(n):
    while len(n) %3 !=0:   #each octal digit corresponds to 3 binary bits
        n="0" + n            #if not add 0 to last
        octal=" "
    for i in range(0,len(n),3):
        group=n[i:i+3]
        value=int(group,2)
        octal +=str(value)
    print("Octal",octal)
def BIN_HEX(n):
    while len(n) % 4 != 0:   #4 binary digits represents 1 hex value
        n="0" + n
    hexa=""
    for i in range (0,len(n),4):
        group=n[i:i+4]
        value=int(group,2)

        if value<10:
            hexa += str(value)
        else:
            hexa += chr(55 + value)
    print("Hexadecimal",hexa)
def OCT_DEC(n):
    dec=0
    power=0
    for digit in n[::-1]:
        dec=dec + int(digit) * (8 ** power)
        power +=1
    print("Decimal",dec)
def OCT_BIN(n):
    binary=""
    for digit in n:
        if digit == '0':
            binary += "000"
        elif digit == '1':
            binary += "001"
        elif digit == '2':
            binary += "010"
        elif digit == '3':
            binary += "011"
        elif digit == '4':
            binary += "100"
        elif digit == '5':
            binary += "101"
        elif digit == '6':
            binary += "110"
        elif digit == '7':
            binary += "111"
    print("Binary",binary)
def OCT_HEX(n):          
    binary = ""                        # Step 1: Octal → Binary
    octal_to_binary = {
        '0': "000", '1': "001", '2': "010", '3': "011",
        '4': "100", '5': "101", '6': "110", '7': "111"
    }

    for digit in n:
        binary += octal_to_binary[digit]

                                    # Step 2: Binary → Hexadecimal
    while len(binary) % 4 != 0:
        binary = "0" + binary

    hex_num = ""

    for i in range(0, len(binary), 4):
        group = binary[i:i+4]
        value = int(group, 2)

        if value < 10:
            hex_num += str(value)
        else:
            hex_num += chr(55 + value)

    print("Hexadecimal:", hex_num)
def HEX_DEC(hex_num):    
    hex_num=hex_num.upper()      #hex includes uppercase alphabets
    dec=0
    power=0
    for digit in hex_num[::-1]:
        if digit.isdigit():
            value=int(digit)
        else:
            value=ord(digit)-55    #ascii of A is 65 and Hex'A' means 10 so substract with 55
        dec += value * (16 ** power)
        power +=1
    print("Decimal",dec)
def HEX_BIN(hex_num):
    hex_bin = {
        '0':'0000','1':'0001','2':'0010','3':'0011',
        '4':'0100','5':'0101','6':'0110','7':'0111',
        '8':'1000','9':'1001','A':'1010','B':'1011',
        'C':'1100','D':'1101','E':'1110','F':'1111'
    }

    hex_num = hex_num.upper()
    binary = ""

    for digit in hex_num:
        binary += hex_bin[digit]

    print("Binary value:", binary)




def HEX_OCT(hex_num):
    hex_bin = {
        '0':'0000','1':'0001','2':'0010','3':'0011',
        '4':'0100','5':'0101','6':'0110','7':'0111',
        '8':'1000','9':'1001','A':'1010','B':'1011',
        'C':'1100','D':'1101','E':'1110','F':'1111'
        }

    hex_num = hex_num.upper()
    binary = ""

    for digit in hex_num:
        binary += hex_bin[digit]   #converts into binary

    while len(binary) % 3 !=0:    #binary to octal
        binary='0'+binary
    octal=""
    for i in range(0,len(binary),3):
        group = binary[i:i+3]
        octal += str(int(group,2))
    print("Octal value",octal)
DEC_BIN(5)
DEC_OCT(10)
DEC_HEX(20)
BIN_DEC("1010")
BIN_OCT("10101")
BIN_HEX("10101")
OCT_DEC("10")
OCT_BIN("10")
OCT_HEX("10")
HEX_DEC("2A")
HEX_BIN("2A")
HEX_OCT("2A")










































        
        
        















































