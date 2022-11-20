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
        # print(dic)
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

import pickle
import zlib

a = '''   srand(GetTickCount());                     // 初始化随机数队列的"种子"
	ProcNumber=((float) rand() / 32767) * 5 + 5;  // 随机产生进程数量5~10
	FinishedProc=0;

	for(i=0;i<ProcNumber;i++)   // 生成进程的CPU--I/O时间数据序列
	{  
		proc[i].p_pid=((float) rand() / 32767) * 1000;
		proc[i].p_state='B';   // 初始都为后备状态
		s=((float) rand() / 32767) *6 + 6; // 产生的进程数据序列长度在6~12间
		proc[i].p_rserial[0]=s; // 第一项用于记录序列的长度
		for(j=1;j<=s;j++)  // 生成时间数据序列，数值在10~30间
			proc[i].p_rserial[j]=((float) rand() / 32767) *10 + 5;
		// 赋其他字段的值
		proc[i].p_pos=1;
		proc[i].p_starttime=((float) rand() / 32767) *49+1;
		proc[i].p_endtime=0;   
		proc[i].p_cputime=proc[i].p_rserial[1];  
		proc[i].p_iotime=proc[i].p_rserial[2];  
		proc[i].p_next=-1; 
	}
	printf("\n---------------------------\n    建立了%d个进程数据序列\n\n", ProcNumber);
	DisData();
	printf("\nPress Any Key To Continue.......");
	_getch() ; 
	return ;
}


//   从磁盘读取最后一次生成的进程信息的文件，执行调度，以重现调度情况。


void Read_Process_Info()
{
	ifstream inFile;     // 定义打开文件的文件流
	char ch; 
	int i,j,k,tmp;		
	inFile.open("Process_Info.txt") ; // 打开上次写的txt进行信息文件流
	i=0;
	while(inFile)
	{ 
		inFile.get(ch);

		for(j=0;j<3;j++) inFile.get(ch);//扔掉3个字符，	    
		inFile>>proc[i].p_pid;
		for(j=0;j<5;j++) inFile.get(ch);//继续读，扔掉5个字符
		inFile>>proc[i].p_rserial[0];
		for(j=0;j<7;j++) inFile.get(ch);//继续读，扔掉7个字符
		inFile>>proc[i].p_starttime;
		for(j=0;j<2;j++) inFile.get(ch);//继续读，扔掉2个字符
		for(k=1;k<=proc[i].p_rserial[0];k++)
		{
			inFile>>tmp;  
			proc[i].p_rserial[k]=tmp;
		}		
		proc[i].p_state='B';
		proc[i].p_pos=1;
		proc[i].p_endtime=0; 
		proc[i].p_next=-1; 
		proc[i].p_cputime=proc[i].p_rserial[1];  
		proc[i].p_iotime=proc[i].p_rserial[2];     
		i++; //本行结束，一个进程信息读完，序号+1, 准备 next process 
	}
	ProcNumber=i-1;  //给ProcNumber赋值，i最后有++，回位下
	inFile.close();//完工后，记得归位，关灯。
}





//            检查是否有新进程到达，有则放入就绪队列


void NewReadyProc(void)
{ 	int n;

	for(int i=0; i<ProcNumber; i++) 
	{	
		if (proc[i].p_starttime == ClockNumber) // 进程进入时间达到系统时间，ClockNumber是当前的系统时间
		{   
          proc[i].p_state='R';	 //	进程状态修改为就绪	  	  
		  proc[i].p_next=-1; // 该进行即将要挂在队列末尾，它肯定是尾巴，后面没人的，所以先设置next=-1

          if (ReadyPoint==-1) // 如果当前就绪队列无进程
		  	  ReadyPoint=i;
		  else      // 如果就绪队列有进程，放入队列尾
'''

str1 = zlib.compress(a.encode(), zlib.Z_BEST_COMPRESSION)
str2 = zlib.decompress(str1)
print(len(a))
print(len(str1))
print(len(str2))
print(len(pickle.dumps(a)))

print(zlib.decompress(str1).decode())