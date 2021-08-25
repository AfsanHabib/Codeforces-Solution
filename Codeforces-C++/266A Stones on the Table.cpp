#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin>>n;
    char a[n];
    int i,ans=0;

    for(i=0; i<n; i++)
    {
        cin>>a[i];
    }
    for(i=0; i<n; i++)
    {
        if(a[i]==a[i+1])
            ans++;
    }
    cout<< ans;

    return 0;
}

/*
#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,i,r=0,b=0,g=0;
    scanf("%d",&n);
    char s[n];
    for(i=0; i<n; i++)
    {
        cin>>s[i];
    }
    for(i=0; i<n; i++)
    {
        if(s[i]== 'R')
            while(s[i+1]=='R')
            {
                r++;
                i++;
            }

        if(s[i]== 'B')
            while(s[i+1]=='B')
            {
                b++;
                i++;
            }

        if(s[i]== 'G')
            while(s[i+1]=='G')
            {
                g++;
                i++;
            }
    }
    cout<<r+b+g;

    return 0;
}

*/
