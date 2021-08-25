#include<bits/stdc++.h>
using namespace std;
int main()
{
    string s;
    cin>>s;
    for(int i=0; i<s.size(); i++)
    {
        if(s[0]>= 97)
            s[0]=s[0]-32;

    }
    cout<<s;

    return 0;
}




