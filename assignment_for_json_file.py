import json
fm=0
with open ("students.json","r") as file:
    json_content = json.load(file)
    for record in json_content:
        for k,v in record.items():
            if k=="marks":
                fm=v[0]+v[1]+v[2]+v[3]
                per=fm/400*100
                my_file = open("percentage.json","a")
                my_file.write(f"{str(per) }%\n")
                # with open("percentage.json","w") as file:
                #         json.dump(json_data , file)
                print(f"percentage is: {per}%")

my_file.close()

        
        

