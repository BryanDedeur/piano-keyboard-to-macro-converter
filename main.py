import random

def read_input():
    # Read input from the terminal
    user_input = input("Enter your text: ")

    file_content = []
    with open("base.pmc", mode='r') as file:
        for line in file.readlines():
            file_content.append(line)

    line_number = 2
    jump_number = 3
    for token in user_input.split(' '):
        no_delay = False
        for char in token:
            if char == '|':
                continue
            if char == '[' or char == ']':
                # file_content.append(str(line_number)+'|[Pause]||1|0|Sleep|||||'+str(jump_number)+'|\n')
                no_delay = True
                ''
                if file_content[-1].find("KeyWait") == -1:
                    file_content.append(str(line_number)+'|[KeyWait]|Tab|1|0|KeyWait||||||\n')
                line_number += 1
                jump_number += 2
                continue
            if no_delay:
                file_content.append(str(line_number)+'|'+char+'|{'+char+'}|1|'+str(random.randint(0,50))+'|Send|||||'+str(jump_number)+'|\n')
            else:
                file_content.append(str(line_number)+'|'+char+'|{'+char+'}|1|0|Send|||||'+str(jump_number)+'|\n')
                if file_content[-1].find("KeyWait") == -1:
                    line_number += 1
                    file_content.append(str(line_number)+'|[KeyWait]|Tab|1|0|KeyWait||||||\n')

            line_number += 1
            jump_number += 2


    # Open a file to write
    with open("output.pmc", mode='w') as file:
        # Write the input to the file
        for line in file_content:
            file.write(line)
    
    print("Input written to 'output.pmc' successfully!")


if __name__ == '__main__':
    read_input()

