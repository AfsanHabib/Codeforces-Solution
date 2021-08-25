#include<bits/stdc++.h>
using namespace std;
int main()
{
    int a,n,m;
    scanf("%d%d%d",&n,&m,&a);

    long long row,col,ans;

    if(n%a == 0)
    {
        row= n/a;
    }
    else
    {
        row= n/a+1;
    }

    if(m%a==0)
    {
        col=m/a;
    }
    else
    {
        col=m/a+1;
    }

    ans= row*col;

    printf("%lld",ans);

    return 0;
}
