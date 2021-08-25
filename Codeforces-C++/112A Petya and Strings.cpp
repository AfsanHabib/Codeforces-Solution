#include<bits/stdc++.h>
#include<string>
using namespace std;
int main()
{
    string a;
    string b;
    int i;

    cin>>a>>b;

    transform(a.begin(), a.end(), a.begin(), :: tolower);
    transform(b.begin(), b.end(), b.begin(), :: tolower);

    if(a==b)
        printf("0");
    else
    {
        for(i =0; i<a.size(); i++)
        {
            if(a[i]>b[i])
            {
                printf("1");
                break;
            }
            if(b[i]>a[i])
            {
                printf("-1");
                break;
            }
        }
    }

    return 0;
}


