#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,len;
    char s[102];
    scanf("%d",&n);
    while(n--)
    {
        scanf("%s",&s);
        len= strlen(s);

        if(len<=10)
            printf("%s\n",s);
        else
            printf("%c%d%c\n",s[0],len-2,s[len-1]);
    }
    return 0;
}
