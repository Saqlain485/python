# def divide_by(a,b):
#     return a/b


# try:
#     ans =divide_by(40,0) 
# except Exception as e:
#     print("something went wrong",e)
#     print(e.__class__)
# file=open('test1.txt',mode='r')
# data=file.readline()
# print(data)
# file.close()
menu=["espresso","macha","latto","capputline","cortade","amercane"]
def find_coffee(coffee):
    if coffee[0]== 'c':
        return coffee
    map_coffee=map(find_coffee,menu)
    print(map_coffee)
    for x in map_coffee:
        print(x)
        