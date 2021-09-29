#include<bits/stdc++.h>
using namespace std;


void answer()
{
	string s;
	cin>>s;

	int a=0,b=0,c=0,i,d;

	for (i=0;i<s.size();i++){
		if(s[i]=='A')
			a++;
		else if(s[i]=='B')
			b++;
		else
			c++;
	}
	d=a+c;
	
	if(d==b){
		cout<<"YES"<<"\n";
	}
	else
		cout<<"NO"<<"\n";
	return ;
}

int main(){
	int tc;
	cin>>tc;
	while(tc--)
	{
		answer();
	}
	return 0;
}