openingParen = '('
closingParen = ')'
openingBrace = '{'
closingBrace = '}'
openingBracket = '['
closingBracket = ']'

class Syntax():
    def match( self, string ):
        stack = []
        for i in range( len( string ) ):
            if self.isOpening( string[ i ] ):
                stack.append( string[ i ] )
            elif self.isClosing( string[ i ] ):
                if not stack or not self.isMatching( stack.pop(), string[ i ] ):
                    return False
        if not stack:
            return True

    def isOpening( self, char ):
        return ( ( char == openingParen ) or ( char == openingBrace ) or ( char == openingBracket ) )

    def isClosing( self, char ):
        return ( ( char == closingParen ) or ( char == closingBrace ) or ( char == closingBracket ) )

    def isMatching( self, opening, closing ):
        return ( ( ( opening == openingParen ) and ( closing == closingParen ) ) or \
                 ( ( opening == openingBrace ) and ( closing == closingBrace ) ) or \
                 ( ( opening == openingBracket ) and ( closing == closingBracket ) ) )

syntax = Syntax()
string = raw_input()
if syntax.match( string ):
    print "Balanced"
else:
    print "Unbalanced"
