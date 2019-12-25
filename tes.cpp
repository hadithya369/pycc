#include <bits/stdc++.h>
/*#include <boost/multiprecision/cpp_int.hpp>

using namespace boost::multiprecision;*/
using namespace std;
#define mod 1000000007
#define ll long long int
#define fastio  ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)
long long solve(){
    int n,t;
    cin>>n;
    for(int i=0;i<n;i++){
        cin>>t;
        cout<<t<<' ';
    }
    cout<<endl;
    return 0;
}
int main(){
    fastio;
    freopen("a_output.txt","w",stdout);
    freopen("a_input.txt","r",stdin);
    int t;
    cin>>t;
    while(t--){
        solve();
        //cout<<solve()<<"\n";
    }
}