#include<bits/stdc++.h>
#include<string>
using namespace std;
int main()
{
    int n,p=0;
    string s;
    scanf("%d",&n);
    while(n--)
    {
        cin>>s;
        int i;

        if(s[0]=='+' || s[2]=='+')
            p++;

        if(s[0]=='-' || s[2]=='-')
            p--;
    }
    cout<<p;
    return 0;
}

