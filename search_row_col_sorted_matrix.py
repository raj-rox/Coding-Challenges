from typing import List

from test_framework import generic_test
#x=[[1,2][3,4]]

def matrix_search(A: List[List[int]], x: int) -> bool:
    # TODO - you fill in here.
    #rows=len(A)
    cols=len(A[0])-1
    rows=0

    while rows<len(A) and cols >= 0:
        if(x==A[rows][cols]):
            return True
        elif(x<A[rows][cols]):
            cols-=1
        else:
            rows+=1
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_row_col_sorted_matrix.py',
                                       'search_row_col_sorted_matrix.tsv',
                                       matrix_search))
