#include<bits/stdc++.h>
using namespace std;
int main()
{
    int a[5][5],i,j,b,c,ans;

    for(i=0; i<5; i++)
    {
        for(j=0; j<5; j++)
            scanf("%d",&a[i][j]);
    }

    for(i=0; i<5; i++)
    {
        for(j=0; j<5; j++)
            if(a[i][j]==1)
            {
                b=i;
                c=j;
            }
    }

    printf("%d\n",(abs(b-2)+abs(c-2)));

    return 0;
}



/*
#include<bits/stdc++.h>
using  namespace std;
int main()
{
    int i,a[30],b;

    for(i=0; i<25; i++)
    {
        scanf("%d",&a[i]);
    }
    for(i=0; i<25; i++)
    {
        if(a[i]==1)
            b=i;
    }
    printf("%d",abs(12-b));

    return 0;
}
*/


