# my_file = open("Day11/example.txt","w")

# my_file.write("Hello world from file \n")
# my_file.write("I love python")

# my_file.close()


# with open("example.txt","a") as file:
#     file.write("\nI am learning file operation ")

# with open("example.txt",'r') as file:
#     content = file.read()
# print(content)

with open("example.txt",'r') as file:
    content = file.readlines()
print(content)






