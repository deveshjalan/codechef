
/*
1   
6 6 1 6
1 1 2 2
2 2 3 3
3 3 4 4
4 4 6 6
1 1 5 5
5 5 4 4
*/


#include <iostream>
#include<bits/stdc++.h>

using namespace std;

//global_variable
int N, M, X, Y;
int A[200001], B[200001], C[200001], D[200001];
int res;
int E[200001];

vector<long long int> s1,s2;

bool check(long long int a , long long int b)
{
    for(int i=0;i<s1.size();i++)
    {
        if(a<=s2[i] && b>=s1[i])
            return true;
    }
    return false;
}


void solution() {
    cin >>N >>M >>X >>Y;
    for (int i = 0; i < M; i++) {
        cin >> A[i] >> B[i] >> C[i] >> D[i];
        E[i]=0;
    }
    res = -1;

    if ( X==Y)
        res=0;
    else 
    {
        long long int dis=0;
        vector<long long int> a1,b1;
        a1.push_back(X);
        b1.push_back(X);
        while((res==-1)&&(a1.size()>0))
        {
            s1=a1;
            s2=b1;
            vector<long long int> c1,d1;
            for(int i=0;i<M;i++)
            {
                if((E[i]==0)&&check(A[i],B[i]))
                {
                    //cout<<A[i]<<" "<<B[i]<<endl;
                    c1.push_back(C[i]);
                    d1.push_back(D[i]);
                    if(C[i]<=Y && D[i]>=Y )
                    {
                        res=dis+1;
                    }
                    E[i]=1;

                }
            }
            a1=c1;
            b1=d1;
            dis++;

        }
    }

    cout <<res << endl;
}

int main() {
    int T;
    cin >> T;
    while (T--) 
        solution();
    return 0;
}