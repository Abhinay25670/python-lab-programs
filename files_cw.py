file_name = "hello.txt"

content= "loremipsum hfsdjfhgwufyffjksftwfwtfjedgejgfwjhgfdhs \t djshgvshdg \t hfshdgg"

with open (file_name,"w") as file:
    file.write(content)

with open(file_name,"r") as file:
    file1=file.read()

print(file1)