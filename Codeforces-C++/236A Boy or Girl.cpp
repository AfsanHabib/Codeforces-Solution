#include<bits/stdc++.h>
using namespace std;
int main()
{
    string s;
    cin>>s;
    int l= s.length();
    int c=0;
    transform(s.begin(), s.end(), s.begin(), :: tolower);
    sort(s.begin(), s.end());
    for(int i =0; i<l; i++)
    {
        if(s[i]!= s[i+1])
            c++;
    }
    if(c%2==0)
    {
        printf("CHAT WITH HER!");
    }
    else
    {
        printf("IGNORE HIM!");
    }
    return 0;
}
