#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#ifdef __INTEL_COMPILER
#include "mkl_lapacke.h"
#else
#include "lapacke.h"
#endif

int main(void) {

    int n, nrhs, lda, ldb, info;
    double *A, *b;
    int *ipiv;

    n = 2; nrhs = 1;


     lda=n, ldb=n;
     A = (double *)malloc(n*n*sizeof(double));
     b = (double *)malloc(n*nrhs*sizeof(double));
     ipiv = (int *)malloc(n*sizeof(int)) ;


     A[0] = 1.;
     A[1] = 0.5;
     A[2] = 0.5;
     A[3] = 1./3.;

//     info = clapack_dgesv( 102, n, nrhs, A, lda, ipiv, b, ldb );
     info = LAPACKE_dgesv( LAPACK_COL_MAJOR, n, nrhs, A, lda, ipiv, b, ldb );

     if (info != 0) return 1;

     return 0;
}