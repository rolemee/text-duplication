#include <bits/stdc++.h>
using namespace std;

int main() {
   int t;
   cin>>t;
   while(t--){
     int n,q;
     cin>>n>>q;
     int arr[n];
     long long evenSum=0;
     long long oddSum=0;
     int countEvenNumber = 0;
     int countOddNumber = 0;
     for(int i=0;i<n;i++){
        int item;cin>>item;
        arr[i]=item;
        if(arr[i]%2 ==0){
        	evenSum+=arr[i];
        	countEvenNumber+=1;
        }
        else {
        	oddSum+=arr[i];
        	countOddNumber+=1;
        }
     }
     while(q--){
     	int type,x;
     	cin>>type>>x;
     	long long ansEven = evenSum;
     	long long ansOdd = oddSum;
     	if(type == 0){
     		if(x%2 == 1){
     			oddSum = oddSum + x*countEvenNumber + evenSum;
     			evenSum=0;
     			countOddNumber+=countEvenNumber;
     			countEvenNumber=0;
     			
     		}
     		else {
     			evenSum = evenSum + x*countEvenNumber;
     		}
     	}
     	else {
     		if(x%2 == 1){
     			evenSum = evenSum + x*countOddNumber + oddSum;
     			oddSum=0;
     			countEvenNumber+=countOddNumber;
     			countOddNumber=0;
     		}
     		else oddSum = oddSum + x*countOddNumber;

     	}
     	cout<<evenSum + oddSum <<'\n';
     }
   }
}