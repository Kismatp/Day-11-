import json

# # Writing json file 
# json_data =[ 
#     {
#     "name": "Ram ",
#     "age" : 20 ,
#     "address ": "Bhaktapur "

#     },
#     {
#     "name": "Hari",
#     "age" : 21 ,
#     "address ": "Bharatpur "
#     }
# ]
# # Writing json file 
# json_data= []
# json_data.append(
# {
#     "name": "Ram ",
#     "age" : 20 ,
#     "address ": "Bhaktapur "

#     }

# )

# with open("example.json","w") as file :
#     json.dump(json_data , file)

with open("example.json","r") as file :
    json_content = json.load(file)
    # print(json_content)

# Accessing elements from json content 
    for record in json_content:
        print(record)







