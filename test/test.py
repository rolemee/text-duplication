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