import csv

# Writing a csv file 
csv_content = [
    {"name","age","address"},
    {"ram",21,"BHaktapur"},
    {"Hari",22,"CHitwan"}


]

# with open("example.csv","w") as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerow(csv_content)

# Reading a csv file 
with open ("example.csv","r") as file:
    csv_reader=csv.reader(file)
    csv_content = list(csv_reader)
    # print(csv_reader)
    for row in csv_content:
        print(row)

# for row in csv_content[1:]:
#     print(row)





