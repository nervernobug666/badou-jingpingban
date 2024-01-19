# week4作业

# 词典；每个词后方存储的是其词频，词频仅为示例，不会用到，也可自行修改
Dict = {
    "经常": 0.1,
    "经": 0.05,
    "有": 0.1,
    "常": 0.001,
    "有意见": 0.1,
    "歧": 0.001,
    "意见": 0.2,
    "分歧": 0.2,
    "见": 0.05,
    "意": 0.05,
    "见分歧": 0.05,
    "分": 0.1,
}

# 待切分文本
sentence = "经常有意见分歧"

target=[]
# 实现全切分函数，输出根据字典能够切分出的所有的切分方式
def all_cut(Dict, left, result):
    # 获取句子长度
    length = len(sentence)
    #当左切分的索引等于句子长度时输出一个切分结果
    if left == length:
        target.append(result[:])
        return
    #循环每次右切分的索引
    for right in range(left + 1, length + 1):
        #获取句子的切片
        temp = sentence[left:right]
        #如果切片在词表中出现则继续切分
        if temp in Dict.keys():
            all_cut(Dict, right, result + [temp])
    return target


print(all_cut(Dict, 0,[]))
