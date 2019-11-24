use, intrinsic :: iso_fortran_env, only: stderr=>error_unit, sp=>real32
implicit none


integer, parameter :: LRATIO=8
integer, parameter :: M=2, N=2

integer, parameter :: Lwork = LRATIO*M !at least 5M for sgesvd

real(sp) :: U(M,M), VT(N,N), errmag(N)
real(sp) :: S(N), truthS(N), SWORK(LRATIO*M) !this Swork is real

integer :: info
real(sp) :: A(M, N)

A = reshape([1., 1./2, &
             1./2, 1./3], shape(A), order=[2,1])

truthS = [1.267592, 0.065741]

call sgesvd('A','N',M,N, A, M,S,U,M,VT, N, SWORK, LWORK, info)

if(info /= 0) error stop 'sgesvd errored'

errmag = abs(s-truthS)
if (any(errmag > 1e-3)) then
  print *,'estimated singular values: ',S
  print *,'true singular values: ',truthS
  write(stderr,*) 'large error on singular values', errmag
  stop 1
endif

print *,'OK: Fortran SVD'

end program