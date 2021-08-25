#include<bits/stdc++.h>
using namespace std;
int main()
{
    string s;
    cin>>s;

    int l= s.length();
    int digit=(l/2)+1;   //find how many + and digit
    int c=0;

    sort(s.begin(),s.end());  // after sort +++1123231313
    s.erase(0,digit-1); // remove + sign

    for(int i=0; i<digit; i++)
    {
        c++;
        cout<<s[i];

        if(c!=digit)
            cout<<"+";
    }

    return 0;
}



