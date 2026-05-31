## Writing into the file
with open("File_Handling//youtube.txt",'w') as file:
    file.write("Here youtube's videos info will be stored.")

## reading the file
with open("File_Handling//youtube.txt",'r') as file:
    txt = file.read()
    print(txt)

## Deleting the file
import os
if os.path.exists("File_Handling//youtube.txt"):
  os.remove("File_Handling//youtube.txt")
else:
  print("The file does not exist")