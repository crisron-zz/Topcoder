#include <iostream>

using namespace std;

class Football {
    int scores[ 3 ];
    int fetchComb( int, int );
    public:
        Football();
        int fetchCombinations( int );
};

Football::Football() {
    scores[ 0 ] = 2;
    scores[ 1 ] = 3;
    scores[ 2 ] = 7;
}

int Football::fetchCombinations( int n ) {
    return fetchComb( n, 2 );
}

int Football::fetchComb( int n, int i ) {
    if( !n ) {
        return 1;
    }
    if( n < 0 || i < 0 ) {
        return 0;
    }
    return fetchComb( n - scores[ i ], i ) + fetchComb( n, i - 1 );
}

int main() {
    int n;
    cin >> n;
    Football fb = Football();
    cout << fb.fetchCombinations( n ) << endl;
    return 0;
}
