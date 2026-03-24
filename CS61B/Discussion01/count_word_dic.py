# 创建一个字典，返回字符列表中单词出现的次数
# 字典的内容用{}包裹
#1. 创建一个单词列表
list_of_words = ["apple","banana","pear","orange","orange","orange","pear","pear","apple","pear","pear","pear"]

def count_word_dic(list_of_words):
    counts = {} # 2. 初始化字典
    for word in list_of_words: # 3. 遍历列表中的单词
        if word not in counts: # 4. 第一次出现的单词还没被收入字典里，计数为1
            counts[word] = 1
        else: # 5. 不是第一次出现的就计数加一
            counts[word] += 1
    return counts
print(count_word_dic(list_of_words))
