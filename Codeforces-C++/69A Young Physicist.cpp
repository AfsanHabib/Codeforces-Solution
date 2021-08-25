#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,x,y,z;
    int a=0, b=0, c=0;
    cin>>n;
    while(n--)
    {
        cin>>x>>y>>z;
        a= a+x;
        b=b+y;
        c=c+z;
    }
    {
        if(a==0 && b==0 && c==0)
            printf("YES\n");
        else
            printf("NO\n");
    }
    return 0;
}
