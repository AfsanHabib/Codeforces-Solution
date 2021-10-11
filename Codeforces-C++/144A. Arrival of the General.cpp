#include<bits/stdc++.h>
using namespace std;

int main()
{
    int soldiers;
    cin>>soldiers;
    int height[soldiers],i,max_height=0,min_height=101,max_index,min_index;

    for (i=0; i<soldiers;i++)
    {
        cin>>height[i];
        if(height[i]>max_height)
        {
            max_height=height[i];
            max_index=i;
        }
        if(height[i]<=min_height)
        {
            min_height=height[i];
            min_index=i;
        }
    }
    if(max_index>min_index)
    {
        min_index++;
    }
    cout<<max_index+(soldiers-1)-min_index;

}
