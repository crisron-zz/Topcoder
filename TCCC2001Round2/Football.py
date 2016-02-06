# Problem Statement Link: https://community.topcoder.com/stat?c=problem_statement&pm=42&rd=2001

class Football():
    def __init__( self ):
        self.__scores = []
        self.__scores.append( 2 )
        self.__scores.append( 3 )
        self.__scores.append( 7 )

    def fetchCombinations( self, n ):
        dp = [ [ 0 for i in range( len( self.__scores ) ) ] for i in range( n + 1 ) ]
        for i in range( n + 1 ):
            for j in range( len( self.__scores ) ):
                if not i:
                    dp[ i ][ j ] = 1
                else:
                    if j > 0:
                        dp[ i ][ j ] = dp[ i ][ j - 1 ]
                    if i - self.__scores[ j ] >= 0:
                        dp[ i ][ j ] += dp[ i - self.__scores[ j ] ][ j ]
        return dp[ n ][ len( self.__scores ) - 1 ]


n = int( raw_input() )
football = Football()
print football.fetchCombinations( n )
