# https://github.com/jacksoninfosec/elliptic-curves/blob/main/ec_basepoint.py

INF_POINT = None


class EllipticCurve :
    def __init__ ( self , p , a , b ) :
        self.p = p
        self.a = a
        self.b = b

    def addition ( self , P1 , P2 ) :
        if P1 == INF_POINT :
            return P2
        if P2 == INF_POINT :
            return P1
        (x1 , y1) = P1
        (x2 , y2) = P2

        if self.equal_modp ( x1 , x2 ) and self.equal_modp ( y1 , -y2 ) :
            return INF_POINT

        if self.equal_modp ( x1 , x2 ) and self.equal_modp ( y1 , y2 ) :
            u = self.reduce_modp ( (3 * x1 * x1 + self.a) * self.inverse_modp ( 2 * y1 ) )
        else :
            u = self.reduce_modp ( (y1 - y2) * self.inverse_modp ( x1 - x2 ) )

        v = self.reduce_modp ( y1 - u * x1 )
        x3 = self.reduce_modp ( u * u - x1 - x2 )
        y3 = self.reduce_modp ( -u * x3 - v )
        return (x3 , y3)

    def subtract ( self , P1 , P2 ) :
        ''' Subtraction is the same as adding with y mirrored
			(x1,y1) - (x2,y2) =>  (x1,y1) + (x2,-y2)
		'''
        return self.addition ( P1 , (P2 [ 0 ] , -P2 [ 1 ]) )

    def multiply ( self , k , P ) :
        Q = INF_POINT
        while k != 0 :
            if k & 1 != 0 :
                Q = self.addition ( Q , P )
            P = self.addition ( P , P )
            k >>= 1
        return Q

    def is_point_on_curve ( self , x , y ) :
        return self.equal_modp ( y * y , x * x * x + self.a * x + self.b )

    def discriminant ( self ) :
        D = -16 * (4 * self.a * self.a * self.a + 27 * self.b * self.b)
        return self.reduce_modp ( D )

    def set_private_key ( self , private_key ) :
        self.private_key = private_key

    def get_public_key ( self ) :
        self.public_key = self.multiply ( self.private_key , self.G )

    def set_G ( self , G ) :
        self.G = G

    def encode ( self , message , k ) :

        encrypted = [ ]

        for a in [ ord ( c ) for c in message ] :
            Pm = self.multiply ( a , self.G )

            Cm = (self.multiply(k , self.G) , self.subtract ( Pm , self.multiply ( k , self.public_key ) ))
            encrypted.append ( Cm )

        return encrypted

    def decode ( self , message ) :
        lookup = {self.multiply ( c , self.G ) : chr ( c ) for c in range ( 256 )}
        decoded = [ ]
        for Cm in message :
            m = self.addition ( Cm [ 1 ] , self.multiply ( self.private_key , Cm [ 0 ] ) )
            decoded.append ( lookup [ m ] )
        return decoded

    # helper functions

    def reduce_modp ( self , x ) :
        return x % self.p

    def equal_modp ( self , x , y ) :
        return self.reduce_modp ( x - y ) == 0

    def inverse_modp ( self , x ) :
        ''' Based on Fermat's Little Theorem'''
        if self.reduce_modp ( x ) == 0 :
            return None
        return pow ( x , self.p - 2 , self.p )


if __name__ == '__main__' :
    # Elliptic Curve 224
    p = 26959946667150639794667015087019630673557916260026308143510066298881
    a = -3
    b = 18958286285566608000408668544493926415504680968679321075787234672564
    Gx = 19277929113566293071110308034699488026831934219452440156649784352033
    Gy = 19926808758034470970197974370888749184205991990603949537637343198772
    n = 26959946667150639794667015087019625940457807714424391721682722368061

    ec = EllipticCurve ( p , a , b )

    ec.set_G ( (Gx , Gy) )  # starting point, all points defined from here

    # Get the private and public keys
    ec.set_private_key ( 131071 )  # random prime
    ec.get_public_key ( )

    message = 'University of Bridgeport'

    Cm = ec.encode ( message , k = 17 )

    m = ec.decode ( Cm )

    print ( message )
    print ( Cm )
    print ( ''.join ( m ) )