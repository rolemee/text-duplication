#include <stdio.h>
#include <windows.h>
#include <fstream>
#include <iostream>
#include <conio.h>

using namespace std;
int   RunPoint;   // ���н���ָ�룬-1ʱΪû�����н���
int   WaitPoint;  // ��������ָ�룬-1ʱΪû����������
int   ReadyPoint; // ��������ָ�룬-1ʱΪû�о�������
long  ClockNumber;   // ϵͳʱ��
int   ProcNumber;    // ϵͳ��ģ������Ľ�������
int   FinishedProc;    // ϵͳ��Ŀǰ��ִ����ϵĽ�������

struct ProcStruct
{
    int  p_pid;         // ���̵ı�ʶ��
    char p_state;       // ���̵�״̬��C--����  R--����  W--����  B--��  F--���
    int  p_rserial[10]; // ģ��Ľ���ִ�е�CPU��I/Oʱ���������У�����洢����0��洢������еĳ��ȣ����������Ա�֪��ɶʱ�ý���ִ�н���
    int  p_pos;   // ��ǰ�������е���λ�ã���������ִ�е������е�����
    int  p_starttime;   // ���̽���ʱ��
    int  p_endtime;     // �������н���ʱ��
    int  p_cputime;     // ��ǰ����ʱ��ν���ʣ�����Ҫ����ʱ��
    int  p_iotime;      // ��ǰI/Oʱ��ν���ʣ���I/Oʱ��
    int  p_next;        // ���̿��ƿ������ָ��
} proc[10];

void DisData() {
    ofstream outFile; //ͬʱ������Ϣд����̵�ĳtxt�ļ��� ���ú���Ҫ#include <fstream.h>

    outFile.open("Process_Info.txt"); //��txt �ļ������Լ���������1��openʱ���� ��û�и��ļ���ϵͳ�ᴴ��һ���հ׵ġ�
    for (int i = 0; i < ProcNumber; i++) {
        cout << "ID=" << proc[i].p_pid << "(len=" << proc[i].p_rserial[0] << ",start=" << proc[i].p_starttime << "):";
        outFile << "ID=" << proc[i].p_pid << "(len=" << proc[i].p_rserial[0] << ",start=" << proc[i].p_starttime << "):";
        for (int j = 1; j <= proc[i].p_rserial[0]; j++) {
            cout << " " << proc[i].p_rserial[j];
            outFile << " " << proc[i].p_rserial[j];
        }
        cout << endl;
        outFile << endl;
    }
    outFile.close(); // д��txt�ļ���������ˢ�����浽������
}

void Create_ProcInfo(void ) {
    int s,i,j;
    srand(GetTickCount());                     // ��ʼ����������е�"����"
    ProcNumber=((float) rand() / 32767) * 5 + 5;  // ���������������5~10
    FinishedProc=0;

    for(i=0;i<ProcNumber;i++)   // ���ɽ��̵�CPU--I/Oʱ����������
    {
        proc[i].p_pid=((float) rand() / 32767) * 1000;
        proc[i].p_state='B';   // ��ʼ��Ϊ��״̬
        s=((float) rand() / 32767) *6 + 6; // �����Ľ����������г�����6~12��
        proc[i].p_rserial[0]=s; // ��һ�����ڼ�¼���еĳ���
        for(j=1;j<=s;j++)  // ����ʱ���������У���ֵ��10~30��
            proc[i].p_rserial[j]=((float) rand() / 32767) *10 + 5;
        // �������ֶε�ֵ
        proc[i].p_pos=1;
        proc[i].p_starttime=((float) rand() / 32767) *49+1;
        proc[i].p_endtime=0;
        proc[i].p_cputime=proc[i].p_rserial[1];
        proc[i].p_iotime=proc[i].p_rserial[2];
        proc[i].p_next=-1;
    }
    printf("\n---------------------------\n    ������%d��������������\n\n", ProcNumber);
    DisData();
    printf("\nPress Any Key To Continue.......");
    _getch() ;
    return ;
}
void NewReadyProc(void) {
    for (int i = 0; i < ProcNumber; i++) {
        if (proc[i].p_starttime == ClockNumber) // ���̽���ʱ��ﵽϵͳʱ�䣬ClockNumber�ǵ�ǰ��ϵͳʱ��
        {
            proc[i].p_state = 'R';     //	����״̬�޸�Ϊ����
            proc[i].p_next = -1; // �ý��м���Ҫ���ڶ���ĩβ�����϶���β�ͣ�����û�˵ģ�����������next=-1

            if (ReadyPoint == -1) // �����ǰ���������޽���
                ReadyPoint = i;
            else      // ������������н��̣��������β
            {
                int n = ReadyPoint;
                while (proc[n].p_next != -1) n = proc[n].p_next;  //�ҵ�ԭ�������е�β��
                proc[n].p_next = i;   //�������β�ͺ���
            }
        }
    }

}
void NextRunProcess() {
    RunPoint = ReadyPoint;
    if(ReadyPoint != -1){
        ReadyPoint = proc[RunPoint].p_next;
        proc[RunPoint].p_next = -1;
    }
}


void Cpu_Sched(void)
{
    int n;

    if (RunPoint == -1)    // û�н�����CPU��ִ��
    { 		NextRunProcess(); 	return; 	}

    proc[RunPoint].p_cputime--;      // ����CPUִ��ʱ�����1��ʱ�ӵ�λ

    if (proc[RunPoint].p_cputime > 0) return; // ����ҪCPUʱ�䣬�´μ�������ξͷ�����

    //�������������>0������������ζ��=0���Ͳ����Զ����أ��������������顣
// ������ɱ���CPU��Ĵ���
    if (proc[RunPoint].p_rserial[0]==proc[RunPoint].p_pos) //����ȫ������ִ�����
    {
        FinishedProc++;
        proc[RunPoint].p_state ='F';
        proc[RunPoint].p_endtime = ClockNumber;
        RunPoint=-1;  //�޽���ִ��
        NextRunProcess(); //�ҷ��ɳ���ȥ����������һ��
    }
    else //����IO������������������
    {
        proc[RunPoint].p_pos++;
        proc[RunPoint].p_state ='W';
        proc[RunPoint].p_iotime =proc[RunPoint].p_rserial[proc[RunPoint].p_pos];

        proc[n].p_next == -1; //����£����Լ�һ�����̣�û��β��һ����������,��p_next��Ϊ-1ʱ���������һ�����Ǳ�������
        n=WaitPoint;
        if(n == -1) //���������е�һ��I/O����
            WaitPoint=RunPoint;
        else
        {	do //�����������е�β
            {
                if(proc[n].p_next == -1)
                { proc[n].p_next = RunPoint;
                    break;
                }
                n=proc[n].p_next;
            } while(n!=-1) ;
        }
        RunPoint=-1;
        NextRunProcess();
    }
    return;
}

void IO_Sched(void) {
    if (WaitPoint == -1)
        return; // û�еȴ�I/O�Ľ��̣�ֱ�ӷ���

    proc[WaitPoint].p_iotime--; // ����1��ʱ�ӵ�I/Oʱ��

    if (proc[WaitPoint].p_iotime > 0)
        return; // ��û����ɱ���I/O

    int target = WaitPoint;
    WaitPoint = proc[target].p_next;
    proc[target].p_next = -1;
    if (proc[target].p_rserial[0] == proc[target].p_pos) {
        FinishedProc++;
        proc[target].p_state = 'F';
        proc[target].p_endtime = ClockNumber;
    } else {
        proc[target].p_pos++;
        proc[target].p_state = 'R';
        proc[target].p_cputime = proc[RunPoint].p_rserial[proc[RunPoint].p_pos];
        int n = ReadyPoint;
        if (n == -1)
            ReadyPoint = target;
        else {
            do {
                if (proc[n].p_next == -1) {
                    proc[n].p_next = target;
                    break;
                }
                n = proc[n].p_next;
            } while (n != -1);
        }
    }
}
void  Display_ProcInfo()
{
    int n;
    system("cls");
    printf("\n       ��ǰϵͳģ��%2d�����̵�����ʱ�ӣ�%ld\n\n", ProcNumber, ClockNumber);

    printf("       ����ָ��=%d, ����ָ��=%d, ����ָ��=%d\n\n", ReadyPoint, RunPoint, WaitPoint);

    if (RunPoint != -1)
    {
        //Print ��ǰ���еĽ��̵���Ϣ��
        printf(" .............Running Process .............\n ");
        printf("��ǰ���еĽ���  No.%d ID��%d(%2d,%2d)", RunPoint, proc[RunPoint].p_pid, proc[RunPoint].p_rserial[0], proc[RunPoint].p_starttime);
        printf(" ��CPUʱ��=%d, ʣ��CPUʱ��=%d\n", proc[RunPoint].p_rserial[proc[RunPoint].p_pos], proc[RunPoint].p_cputime);
    }
    else
        printf("No Process Running !\n");

    n = ReadyPoint;
    printf("\n Ready Process ...... \n");
    while (n != -1) // ��ʾ����������Ϣ
    {
        printf("    [No.%2d ID:%4d],%d,%d,%d\n", n, proc[n].p_pid, proc[n].p_starttime, proc[n].p_rserial[proc[n].p_pos], proc[n].p_cputime);
        n = proc[n].p_next;
    }

    n = WaitPoint;
    printf("\n Waiting Process ...... \n");
    while (n != -1) // ��ʾ����������Ϣ
    {
        printf("    [No.%2d ID:%4d],%d,%d,%d\n", n, proc[n].p_pid, proc[n].p_starttime, proc[n].p_rserial[proc[n].p_pos], proc[n].p_iotime);
        n = proc[n].p_next;
    }


    printf("\n=================== �󱸽��� ====================\n");
    for (int i = 0; i < ProcNumber; i++)
        if (proc[i].p_state == 'B')
            printf("    [No.%2d ID:%4d],%d\n", i, proc[i].p_pid, proc[i].p_starttime);

    printf("\n================ �Ѿ���ɵĽ��� =================\n");
    for (int i = 0; i < ProcNumber; i++)
        if (proc[i].p_state == 'F')
            printf("    [No.%2d ID:%4d],%d,%d\n", i, proc[i].p_pid, proc[i].p_starttime, proc[i].p_endtime);

}
void Read_Process_Info(  )
{
    ifstream inFile;     // ������ļ����ļ���
    char ch;
    int i,j,k,tmp;

    inFile.open("Process_Info.txt") ; // ���ϴ�д��txt������Ϣ�ļ���

    i=0;
    while(inFile)
    {
        inFile.get(ch);

        for(j=0;j<3;j++) inFile.get(ch);//�ӵ�3���ַ���
        inFile>>proc[i].p_pid;

        for(j=0;j<5;j++) inFile.get(ch);//���������ӵ�5���ַ�

        inFile>>proc[i].p_rserial[0];

        for(j=0;j<7;j++) inFile.get(ch);//���������ӵ�7���ַ�

        inFile>>proc[i].p_starttime;

        for(j=0;j<2;j++) inFile.get(ch);//���������ӵ�2���ַ�


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

        i++; //���н�����һ��������Ϣ���꣬���+1, ׼�� next process

    }

    ProcNumber=i-1;  //��ProcNumber��ֵ��i�����++����λ��

    inFile.close();//�깤�󣬼ǵù�λ���صơ�

}

void Scheduler_FF(void)  //����ģ���㷨
{
    if(ProcNumber==0) //��ֵ��Ȼ��0�� ֻ��˵�û�û��������
    {
        Read_Process_Info();//��ô���Ӵ��̶�ȡ�ϴδ����Ľ�����Ϣ����ֵ����Ӧ����

    }
    ClockNumber=0;// ʱ�ӿ�ʼ��ʱ, ��ʼ����ģ��

    while(FinishedProc < ProcNumber) // ִ���㷨
    {
        ClockNumber++;  // ʱ��ǰ��1����λ
        NewReadyProc(); // �б��½����Ƿ񵽴�
        Cpu_Sched();    // CPU����
        IO_Sched();     // IO����
        Display_ProcInfo(); //��ʾ��ǰ״̬
//        Sleep(40);
    }
//    DisResult();
    getch();
}

////////////////////////////////////////////////////////////////////////

void DisResult() {
    int i;
    printf("\n---------------------------------\n");
    printf("��ʶ��-ʱ������-����ʱ��-����ʱ��-��תʱ��-��Ȩ��תʱ��\n");
    for (i = 0; i < ProcNumber; i++)
    {
        printf("ID=%d -> %d\t", proc[i].p_pid, proc[i].p_rserial[0]);
        printf("%d\t%d\t", proc[i].p_starttime, proc[i].p_endtime);
        printf("%d\t", proc[i].p_endtime - proc[i].p_starttime);
        int sumtime = 0;
        for (int j = 1; j <= proc[i].p_rserial[0]; j++)
            sumtime += proc[i].p_rserial[j];
        printf("%.2f", (proc[i].p_endtime - proc[i].p_starttime) * 1.0 / sumtime);
        printf("\n");
    }
}

int main( )
{
    char ch;
    RunPoint=-1;   // ���н���ָ�룬-1ʱΪû�����н���
    WaitPoint=-1;  // ��������ָ�룬-1ʱΪû����������
    ReadyPoint=-1; // ��������ָ�룬-1ʱΪû�о�������
    ClockNumber=0;   // ϵͳʱ��
    ProcNumber=0;    // ��ǰϵͳ�еĽ�������
    system("cls") ;
    while ( true )                           {
        printf("***********************************\n");
        printf("     1: �������̵����������� \n") ;
        printf("     2: ��������Ϣ��ִ�е����㷨\n") ;
        printf("     3: ��ʾ���Ƚ�� \n") ;
        printf("     4: �˳�\n") ;
        printf("***********************************\n");
        printf( "Enter your choice (1 ~ 4): ");
        do
            ch = (char)_getch() ; //���������Ϣ����ȷ����������
        while(ch != '1' && ch != '2' && ch != '3'&& ch != '4');
        if(ch == '4') { printf( "\n");return 0; }   // ѡ��4���˳�
        else if(ch == '3') DisResult();       // ѡ��3
        else if(ch == '2')  Scheduler_FF();     // ѡ��2
        else if(ch == '1') Create_ProcInfo();  // ѡ��1
        _getch() ;
        system("cls") ;
    }
    //����
    printf("\nPress Any Key To Continue:");
    _getch() ;
    return 0;
}
