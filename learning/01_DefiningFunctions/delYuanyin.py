my_string = input("请输入字符串：")
my_string_list = list(my_string)

def delYuanyin(string_list):
    Yuanyin = ['a','e','i','o','u']
    for char in string_list:
        if char not in Yuanyin:
            print(char,end = "")

delYuanyin(my_string_list)