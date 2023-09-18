import random
import os

def read_input():
    for filename in os.listdir('sheet-music/'):
        filepath = os.path.join('sheet-music/', filename)
        if os.path.isfile(filepath):
            file_content = []
            with open("base.pmc", mode='r') as file:
                for line in file.readlines():
                    file_content.append(line)

            song_string = ''
            with open(filepath, mode='r') as file:
                song_string = file.read()

            line_number = 2
            jump_number = 3
            no_delay = False
            for char in song_string:
                if char == '\n':
                    if file_content[-1].find("Pause") == -1:
                        file_content.append(str(line_number)+'|[Pause]||1|'+str(random.randint(200,300))+'|Sleep|||||'+str(jump_number)+'|\n')
                        line_number += 1
                        jump_number += 2
                    continue
                elif char == '[':
                    no_delay = True
                    continue
                elif char == ']':
                    no_delay = False
                    continue
                elif char == ' ':
                    # add pause
                    file_content.append(str(line_number)+'|[Pause]||1|'+str(random.randint(200,300))+'|Sleep|||||'+str(jump_number)+'|\n')
                elif char == '|':
                    # add long pause
                    file_content.append(str(line_number)+'|[Pause]||1|'+str(random.randint(450,550))+'|Sleep|||||'+str(jump_number)+'|\n')
                else:
                    if no_delay:
                        file_content.append(str(line_number)+'|'+char+'|{'+char+'}|1|'+str(random.randint(0,10))+'|Send|||||'+str(jump_number)+'|\n')
                    else:
                        file_content.append(str(line_number)+'|'+char+'|{'+char+'}|1|'+str(random.randint(100,200))+'|Send|||||'+str(jump_number)+'|\n')
                line_number += 1
                jump_number += 2

            # Open a file to write
            with open('complete-songs/auto-'+os.path.splitext(filename)[0]+".pmc", mode='w') as file:
                # Write the input to the file
                for line in file_content:
                    file.write(line)
            
            print('Written to complete-songs/auto-'+os.path.splitext(filename)[0]+'.pmc successfully!')


if __name__ == '__main__':
    read_input()

