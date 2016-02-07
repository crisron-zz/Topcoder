function Football() {
    this.__scores = [ 2, 3, 7 ];
}

Football.prototype.fetchCombinations = function( n ) {
    var dp = [];
    for( var i = 0; i <= n; ++i ) {
        dp.push( 0 );
    }
    dp[ 0 ] = 1;
    for( var i = 0; i < this.__scores.length; ++i ) {
        for( var j = this.__scores[ i ]; j <= n; ++j ) {
            dp[ j ] += dp[ j - this.__scores[ i ] ];
        }
    }
    return dp[ n ];
}

var football = new Football();
for( var n = 0; n < 76; ++n ) {
    console.log( "n = ", n );
    console.log( football.fetchCombinations( n ) );
}
