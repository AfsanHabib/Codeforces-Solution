
#include<bits/stdc++.h>
using namespace std;

int main(){


int tc;
cin>>tc;

while(tc--)
{
	int n;
	cin>>n;
	deque<int>De;
	for(int i =0; i<n;i++)
		{
			int x;
			cin>>x;
			De.push_back(x);
		}

	deque<int>asnwer;
	int data=De.front();
	De.pop_front();
	asnwer.push_back(data);

	for(int i=1;i<n;i++){
		int check=asnwer.front();
		data=De.front();
		De.pop_front();
		if(data<check){
			asnwer.push_front(data);
		}
		else{
			asnwer.push_back(data);
		}

	}
	for (int i=0;i<n;i++){
		cout<<asnwer.at(i)<<" ";
	}
		cout<<"\n";


}
	return 0;
}