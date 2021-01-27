
with open("file/SacramentocrimeJanuary2006.csv") as csv_file:
    for line in csv_file:
        temp_line = line.split(",")
        place_counter = 0
        while place_counter < len(temp_line):
            temp_line[place_counter] = temp_line[place_counter][1:-1]
            if place_counter == 0:
                print(temp_line[place_counter])
            if place_counter == 1:
                print(temp_line[place_counter])
            if place_counter == 5:
                print(temp_line[place_counter] + "\n\n")
            place_counter = place_counter + 1
         

import os.path
import shutil
import time
temp_output = ""
with open("file/pet.py") as python_file:
    for line in python_file:
        temp_line = line.strip()
        if temp_line.startswith("#") or temp_line.startswith('"""'):
            pass
        else:
            temp_output = temp_output + line

if os.path.isfile("file/cleaned_output.py"):
    shutil.copy2("file/cleaned_output.py", "file/cleaned_output.py.backup" + str(time.time()))
else:
    with open("file/cleaned_output.py", "w") as file_output:
        file_output.write(temp_output)