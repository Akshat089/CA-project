result1 = ""
arr = []
def generator(opcode):
    #function made for all opcodes
    value = ""
    if opcode == "LOAD_M":
        value = "00001001"
    elif opcode == "ADD_M":
        value = "00000101"
    elif opcode == "STORE_M":
        value = "00100001"
    elif opcode == "LOAD_MQ":
        value = "00001010"
    elif opcode == "SUB_M":
        value = "00000110"
    elif opcode == "DIV_M":
        value = "00010110"
    elif opcode == "JUMP_+_M":
        value = "01000110"
    elif opcode == "POW_M":
        value = "01001000"
    elif opcode == "COMP_M":
        value = "00100010"
    elif opcode == "HALT_M":
        value = "00000011"
    elif opcode == "MUL_M":
        value = "00001011"
    elif opcode == "ADD_|M|":
        value = "00000111"
    elif opcode == "SUB_|M|":
        value = "00001000"
    elif opcode == "LSH":
        value = "10001000"
    elif opcode == "RSH":
        value = "11001100"
    elif opcode == "LOAD_MQ_M":
        value = "10101010"
    elif opcode == "LOAD_-M":
        value = "10010010"
    elif opcode == "LOAD_|M|":
        value = "11101110"
    elif opcode == "LOAD_-|M|":
        value = "10111010"
    elif opcode == "JUMP_M(0:19)":
        value = "11010011"
    elif opcode == "JUMP_M(20:39)":
        value = "00001111"
    elif opcode == "JUMP+_M(0:19)":
        value = "10000000"
    elif opcode == "JUMP+_M(20:39)":
        value = "10000001"
    elif opcode == "STOR_M(0:19)":
        value = "00111110"
    elif opcode == "STOR_M(20:39)":
        value = "00111111"
    return value
def convert_to_12bit_binary(num):
    # Use format to convert integer to 12-bit binary representation
    binary_str = format(num, '012b')

    return binary_str   

def convert_to_40bit_binary(num):
    # Use format to convert integer to 40-bit binary representation
    binary_str = format(num, '040b')

    return binary_str      
with open('assembly4.txt', 'r') as file:  #open the assembly code file
    file_content = file.readlines()   #convert file into an array
    line_count = len(file_content)   #length of array
    for i in range(1,line_count):    #iterate through the file
        str1 = convert_to_12bit_binary(i) #convert to 12-bit binary
        result1 += str1                  #incrementing string
    #since string is in 1X60 matrix and we need to convert into 5X12(5 can written as n = no of lines)
    num_col = 12 #this is fixed since we need 12 bit address of each line in file
    num_rows = len(result1) // num_col #find no of rows
    result = [result1[i:i+num_col] for i in range(0, len(result1), num_col)] #converts it into list of n elements
    # print(result)
    for i in range(len(file_content)):
        line_elements = file_content[i].strip().split()
        #iterate through the file we have using same indexing to make the matrix above
        if len(line_elements) == 1:
            first = line_elements[0]
            if first.isdigit():
                # Handle cases where the first element is a digit
                fourty_bit_str = convert_to_40bit_binary(int(first))
                result[i] = result[i] + " " + fourty_bit_str
                arr.append(result[i])
            # Handle lines with only one element (e.g., "7")
            else:
                #handles it for cases such as halt etc
                lhs = generator(first)
                result[i] = result[i] + " " + lhs + "00000000000000000000000000000000"
                arr.append(result[i])
        elif len(line_elements) == 2:
        # Handle lines with two elements (eg: JUMP_+_M 18)
            first = line_elements[0]
            lh = generator(first)
            second = line_elements[1]
            mem = convert_to_12bit_binary(int(second))
            result[i] = result[i] + " " + lh + mem + "00000000000000000000"
            arr.append(result[i])

        elif len(line_elements) >= 4:
            first = line_elements[0]
            
            if first.isdigit():
                # Handle cases where the first element is a digit
                fourty_bit_str = convert_to_40bit_binary(int(first))
                result[i] = result[i] + " " + fourty_bit_str
                arr.append(result[i])
            else:
                # Handle cases where the first element is an opcode
                lhs = generator(first)
                second = line_elements[2]
                mem1 = convert_to_12bit_binary(int(line_elements[1]))
                mem2 = convert_to_12bit_binary(int(line_elements[3]))
                rhs = generator(second)
                result[i] = result[i] + " " + lhs + mem1 + rhs + mem2
                arr.append(result[i])
for i in arr:
    print(i)
