#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,sum=0,ans=0,a[6],i;
    scanf("%d",&n);
    while(n--)
    {
        for(i=0; i<3; i++)
        {
            scanf("%d",&a[i]);
        }
        sum=0;
        for(i=0; i<3; i++)
        {
            if(a[i]==1)
                sum++;
        }
        if(sum>=2)
            ans++;
    }
    printf("%d\n",ans);

    return 0;
}
