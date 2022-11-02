import  math
# 两篇待比较的文档的路径

sourcefile = '2.txt'
s2 = '1.txt'
# 关键词统计和词频统计，以列表形式返回
def Count(resfile):
        t = {}
        infile = open(resfile, 'r', encoding='utf-8')
        f = infile.readlines()
        count = len(f)
        # print(count)
        infile.close()

        s = open(resfile, 'r', encoding='utf-8')
        i = 0
        while i < count:
            line = s.readline()
        # 去换行符
            line = line.rstrip('\n')
            # print(line)
            words = line.split(" ")
            #   print(words)

            for word in words:
                    if word != "" and t.__contains__(word):
                        num = t[word]
                        t[word] = num + 1
                    elif word != "":
                        t[word] = 1
                    # elif word != "":
                    #     t[word] = 1
            i = i + 1

        # 字典按键值降序
        dic = sorted(t.items(), key=lambda t: t[1], reverse=True)
        print(dic)
        # print()
        s.close()
        return (dic)



def MergeWord(T1,T2):
        MergeWord = []
        duplicateWord = 0
        for ch in range(len(T1)):
            MergeWord.append(T1[ch][0])
        for ch in range(len(T2)):
            if T2[ch][0] in MergeWord:
                    duplicateWord = duplicateWord + 1
            else:
                    MergeWord.append(T2[ch][0])

        # print('重复次数 = ' + str(duplicateWord))
        # 打印合并关键词
        # print(MergeWord)
        return MergeWord

# 得出文档向量
def CalVector(T1,MergeWord):
    TF1 = [0] * len(MergeWord)

    for ch in range(len(T1)):
            TermFrequence = T1[ch][1]
            word = T1[ch][0]
            i = 0
            while i < len(MergeWord):
                    if word == MergeWord[i]:
                     TF1[i] = TermFrequence
                     break
                    else:
                        i = i + 1
        # print(TF1)
    return TF1

def CalConDis(v1,v2,lengthVector):

        # 计算出两个向量的乘积
        B = 0
        i = 0
        while i < lengthVector:
            B = v1[i] * v2[i] + B
            i = i + 1
        # print('乘积 = ' + str(B))

        # 计算两个向量的模的乘积
        A = 0
        A1 = 0
        A2 = 0
        i = 0
        while i < lengthVector:
            A1 = A1 + v1[i] * v1[i]
            i = i + 1
        # print('A1 = ' + str(A1))

        i = 0
        while i < lengthVector:
            A2 = A2 + v2[i] * v2[i]
            i = i + 1
           # print('A2 = ' + str(A2))

        A = math.sqrt(A1) * math.sqrt(A2)
        # print("ASD")
        # print(A)
        return format(float(B) / A,".3f")
def Count2(text):
    t = {}

    f = text.split("\n")
    count = len(f)
    # print(count)


    i = 0
    while i < count:
        line = text.split("\n")[i]
        # 去换行符
        line = line.rstrip('\n')
        # print(line)
        words = line.split(" ")
        #   print(words)

        for word in words:
            if word != "" and t.__contains__(word):
                num = t[word]
                t[word] = num + 1
            elif word != "":
                t[word] = 1
            # elif word != "":
            #     t[word] = 1
        i = i + 1

    # 字典按键值降序
    dic = sorted(t.items(), key=lambda t: t[1], reverse=True)
    # print(dic)
    # print()
    return (dic)



T1 = Count(sourcefile)
# print("文档1的词频统计如下：")
# print(T1)
# print()
T2 = Count(s2)
# print("文档2的词频统计如下：")
# print(T2)
# print()
# 合并两篇文档的关键词
mergeword = MergeWord(T1,T2)
#  print(mergeword)
# print(len(mergeword))
# 得出文档向量
v1 = CalVector(T1,mergeword)
# print("文档1向量化得到的向量如下：")
# print(v1)
# print()
v2 = CalVector(T2,mergeword)
# print("文档2向量化得到的向量如下：")
# print(v2)
# print()
# 计算余弦距离
print(CalConDis(v1,v2,len(v1)))


f1 = open("1.txt","r",encoding="utf-8").read().split("\n")
f2 = open("2.txt","r",encoding="utf-8").read().split("\n")
sum = 0
for i in f1:
    for j in f2:
        T1 = Count2(i)
        T2 = Count2(j)
        mergeword = MergeWord(T1, T2)
        v1 = CalVector(T1, mergeword)
        v2 = CalVector(T2, mergeword)
        try:
            if float(CalConDis(v1, v2, len(v1))) >= 0.45:
                print("文章1"+i)
                print("文章2"+j)
                print("相似度" +CalConDis(v1, v2, len(v1)) )
                print("\n")
                sum += len(j)
        except:
            pass
print(sum)