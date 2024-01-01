# def read_file(file_name ):
#     with open(file_name,'r') as file:
#         content = file.read()
#         return content

# data = read_file("sample.txt")
# print(data)   

def write_file():
    with open("sample.txt", 'w') as file: 
         file.write("See uhh again") 
write_file()