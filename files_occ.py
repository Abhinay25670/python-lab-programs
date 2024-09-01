input_file = "hello.txt"
output_file= "hello1.txt"

charto_remove= "h"

with open(input_file,"w") as file:
    file.write("loremipsum sadhsagfgeyfkdfjhsdg jkhjhjhjhjhjhk jhkjhhkkljh;ljh jhkjhkjhkjhhkkhk jhkjhjk ")
with open(input_file,"r") as file:
    content=file.read()

char_count = content.count(charto_remove)
char_replace= content.replace(charto_remove,"")

with open(output_file,"w")as file:
    file.write(char_replace)

with open(output_file,"r")as file:
    con=file.read()

print(con)
print("count of",charto_remove,"=",char_count)