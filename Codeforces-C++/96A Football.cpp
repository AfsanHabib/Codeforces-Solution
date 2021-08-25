#include<bits/stdc++.h>
using namespace std;
int main()
{
    char ch[105];
    int i,a=0,b=0;
    cin>>ch;
    int l=strlen(ch);
    for(i=0; i<l; i++)
    {
        if(ch[i]=='0')
        {
            if(ch[i+1]=='0' && ch[i+2]=='0' && ch[i+3]=='0' && ch[i+4]=='0' && ch[i+5]=='0' && ch[i+6]=='0' )
                a=7;
        }
        else if(ch[i]=='1')
        {
            if(ch[i+1]=='1' && ch[i+2]=='1' && ch[i+3]=='1' && ch[i+4]=='1' && ch[i+5]=='1' && ch[i+6]=='1' )
                b=7;
        }
    }
    {
        if(a==7 || b==7)
            printf("YES\n");
        else
            printf("NO\n");
    }

    return 0;
}
