#include<bits/stdc++.h>
using namespace std;
int main()
{
    int d,n,b,answer=0,c;
    cin>>d>>n>>b;
    for(int i=1; i<=b; i++)
    {
        c=i*d;
        answer= answer+c;
    }
    {
        if(answer<=n)
            cout<<"0";
        else
            cout<<answer-n;
    }
    return 0;
}


