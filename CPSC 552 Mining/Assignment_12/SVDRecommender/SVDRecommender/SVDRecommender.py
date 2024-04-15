import sys
import numpy as np


def main ( ) :
    UP_Rating = np.array ( [ [ 0 , 2 , 0 , 0 , 3 , 0 , 0 , 0 , 0 , 0 ] ,
                             [ 4 , 0 , 0 , 0 , 3 , 0 , 0 , 0 , 5 , 0 ] ,
                             [ 0 , 0 , 0 , 0 , 0 , 3 , 0 , 0 , 0 , 0 ] ,
                             [ 0 , 5 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 2 ] ,
                             [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 5 , 0 , 0 ] ,
                             [ 5 , 2 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ] ,
                             [ 0 , 0 , 0 , 3 , 0 , 0 , 4 , 0 , 5 , 2 ] ,
                             [ 0 , 3 , 0 , 4 , 0 , 0 , 0 , 0 , 0 , 0 ] ,
                             [ 0 , 0 , 4 , 0 , 0 , 2 , 0 , 0 , 0 , 1 ] ,
                             [ 0 , 0 , 0 , 0 , 5 , 0 , 3 , 0 , 2 , 0 ] ,
                             [ 1 , 5 , 0 , 0 , 0 , 4 , 0 , 0 , 0 , 0 ] ,
                             [ 0 , 0 , 4 , 0 , 5 , 0 , 0 , 3 , 0 , 2 ] ,
                             [ 1 , 0 , 0 , 4 , 0 , 0 , 0 , 1 , 0 , 0 ] ,
                             [ 0 , 5 , 0 , 3 , 0 , 0 , 0 , 0 , 4 , 0 ] ,
                             [ 4 , 0 , 0 , 0 , 4 , 0 , 0 , 0 , 0 , 0 ] ,
                             [ 0 , 0 , 0 , 5 , 0 , 2 , 0 , 0 , 0 , 0 ] ,
                             [ 0 , 3 , 0 , 0 , 0 , 0 , 4 , 0 , 0 , 0 ] ,
                             [ 3 , 3 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 5 ] ] )
    
    u , s , vh = np.linalg.svd ( UP_Rating , full_matrices = False )


    print ( f'shape of U {u.shape}' )
    print ( f'shape of s {s.shape}' )
    print ( f'shape of vh {vh.shape}\n' )
    
    num_components = 3
    low_rank_reconstruction = u [ : , :num_components ] @ np.diag ( s [ :num_components ] ) @ vh [ :num_components , : ]
    print ( '---------reconstructed user-product rating matrix' )
    print ( np.round ( low_rank_reconstruction ) )

if __name__ == "__main__" :
    sys.exit ( int ( main ( ) or 0 ) )
