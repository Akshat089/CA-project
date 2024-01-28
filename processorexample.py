import math
#declare all elements
AC = "0"
MBR = "0"
MAR = "0"
IBR = "0"
IR = "0"
IBR = "0"
PC = "0" 
MQ = "0"
PC_array = []
instruction_array = []
#make dictionary as a dynamic memory
memory = {
    "000000000000" : "0000000000000000000000000000000000000000", #line 0 stores 0
    "000000000001" : "0000000000000000000000000000000000000000", #line1 stores 0 (count value)
    "000000000010" : "0000000000000000000000000000000000001010", #line2 stores 10 (stores 10 which we will use to divide)
    "000000000011" : "0000000000000000000000000000011001100010", #line3 stores 1634 (num)
    "000000000100" : "0000000000000000000000000000011001100010", #line4 stores 1634 (originalnum)
    "000000000101" : "0000000000000000000000000000011001100010", #line5 stores 1634 (finalnum)
    "000000000110" : "0000000000000000000000000000000000000000", #line6 stores 0 (result)
    "000000000111" : "0000000000000000000000000000000000000000", #line7 stores 0 (for comparison)
    "000000001000" : "0000000000000000000000000000000000000001", #line8 stores 1 (to increment count by 1)
    "000000001001" : "0000000000000000000000000000000000011011", #line9 stores 27 (to store remainder to the power of count)
    "000000001010" : "0000000000000000000000000000000000001111", #line10 stores 15 (just here by mistake)
    "000000001011" : "0000000000000000000000000000000000000001", #line11 stores 1 (flag if true)
    "000000001100" : "0000000000000000000000000000000000000000", #line12 stores 0 (flag if false)
}
#define ADD function
def ADD_M(AC,MBR,MAR,M):
    MBR = M[MAR]
    AC = int(AC,2)
    AC = AC + int(MBR,2)
    AC = format(AC, "040b")
    return AC

#define SUB function
def SUB_M(AC,MBR,MAR,M):
    MBR = M[MAR]
    AC = int(AC,2)
    AC = AC - int(MBR,2)
    AC = format(AC, "040b")
    return AC

#define LOAD function
def LOAD_M(AC,MBR,M,MAR):
    MAR = MAR
    MBR = M[MAR]
    AC = MBR
    return AC

#define STORE function
def STORE_M(AC,MBR,M,MAR):
    MBR = AC
    M[MAR] = MBR
    return M[MAR]

#define LOADMQ function
def LOAD_MQ(AC,MQ):
    print(MQ)
    AC = MQ
    return  AC

#define DIVISION function
def DIV_M1(AC,MBR,M,MAR,MQ):
    MAR = MAR
    MBR = M[MAR]
    AC = int(AC,2)
    MQ = AC//int(MBR,2)    
    AC = AC % int(MBR,2)
    AC = format(AC, "040b")
    MQ = format(MQ, "040b")
    return AC,MQ

#define POWER function
def POW_M(AC,MBR,MAR,M):
    MAR = MAR
    MBR = M[MAR]
    AC = int(AC,2)
    AC = pow(AC,int(MBR,2))
    AC = format(AC, "040b")
    return AC

#define COMP function
def COMP_M(AC,MBR,MAR,M):
    MAR = MAR
    MBR = M[MAR]
    AC = int(AC,2)
    X = AC - int(MBR,2)
    AC = format(AC, "040b")
    if X == 0:
        return 1
    else:
        return 0

#define print function
def printfunc(AC,MBR,MAR,IR,IBR,PC):
    print(f"MAR value is: {MAR}")
    print(f"MBR value is: {MBR}")
    print(f"IR value is: {IR}")
    print(f"IBR value is: {IBR}")
    print(f"PC value is: {PC}")
    print(f"AC Value is: {AC}")

#main program starts here
    
with open('output.txt', 'r') as file:
    for line in file: #iterate through machine file
        word = line.strip().split()
        PC_array.append(word[0]) #all pc values here
        instruction_array.append(word[1]) #all instructions here

i = 0  #to start from the first line of file
while(IR != "00000011"):
    #start the fetch cycle
    PC = PC_array[i] 
    MBR = instruction_array[i]
    IR = MBR[0:8]
    MAR = MBR[8:20]
    IBR = MBR[20:40]

    j = 0 #used for lhs and rhs execution

    while(j<2):
        if IR == "01000110":  # jump modification it executes jump if number in AC is greater than 0
            if int(AC, 2) > 0:
                print("jump is RUNNING")
                j = 1          # in assembly there is no other instruction with jump since it acts as a loop
                i = abs(int(PC, 2) - int(MAR, 2) - i) # find the value of i using MAR
                PC = int(MAR, 2)   # Update the PC to the new value
                PC = format(PC, "012b") # convert PC to string again
                printfunc(AC, MBR, MAR, IR, IBR, PC) #calls function
                i = i - 1 #decrements i as it will increment itself at the end of the loop 
                break

        elif IR == "00001001": #for LOAD function we use this opcode
            print("load IS RUNNING")
            AC = LOAD_M(AC,MBR,memory,MAR) #call the LOAD function
            printfunc(AC,MBR,MAR,IR,IBR,PC)

        elif IR == "00100001": #for store function use opcode
            print("store IS RUNNING")
            memory[MAR] = STORE_M(AC,MBR,memory,MAR) #call store function
            printfunc(AC,MBR,MAR,IR,IBR,PC)

        elif IR == "00000101": #for add function we use this opcode
            print("add IS RUNNING")
            AC = ADD_M(AC,MBR,MAR,memory) #call add function
            printfunc(AC,MBR,MAR,IR,IBR,PC)

        elif IR == "00000110": #for sub function use opcode
            print("sub IS RUNNING")
            AC = SUB_M(AC,MBR,MAR,memory) #calls function
            printfunc(AC,MBR,MAR,IR,IBR,PC)

        elif IR == "00010110": #for div function use opcode
            print("div IS RUNNING")
            r = DIV_M1(AC,MBR,memory,MAR,MQ) #calls function
            AC = r[0] #from tuple extracts AC 
            MQ = r[1] #from tuple extract MQ
            printfunc(AC,MBR,MAR,IR,IBR,PC)
            
        elif IR == "00001010": #opcode for load mq
            print("loadmq IS RUNNING") 
            AC = LOAD_MQ(AC,MQ)  #calls loadmq function
            printfunc(AC,MBR,MAR,IR,IBR,PC)

        elif IR == "01001000": #opcode for power function
            print("pow IS RUNNING")
            AC = POW_M(AC,MBR,MAR,memory) #calls pow function
            printfunc(AC,MBR,MAR,IR,IBR,PC)

        elif IR == "00100010": #opcode for compare function
            print("comp IS RUNNING")
            flag = COMP_M(AC,MBR,MAR,memory) #calls comp function
            printfunc(AC,MBR,MAR,IR,IBR,PC)

        elif IR == "00000011": #halt opcode loop breaks,program ends
            print("halt IS RUNNING")
            break

        j+=1 #used to implement lhs and rhs. once it is done PC increments itself
        IR  = IBR[0:8] #for rhs it reassigns value to IR and MAR
        MAR = IBR[8:20]

    PC = int(PC,2) #PC converted to binary
    print(PC)
    PC = format(PC,"012b") #PC converted to 12bit string
    i+=1    #i is incremented thus PC increases
print(flag)

        

            
            
