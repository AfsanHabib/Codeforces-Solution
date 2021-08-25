#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,k,a[50];
    scanf("%d%d",&n,&k);

    for(int i=0; i<n; i++)
    {
        scanf("%d",&a[i]);
    }
    int ans=0;

    for(int i=0; i<n; i++)
    {
        if(a[i]>=a[k-1] && a[i]>0)
            ans++;
    }

    {
        printf("%d\n",ans);
    }

    return 0;
}
