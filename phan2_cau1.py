import numpy as np
np.random.seed(123)

#1
def vector_nhan_matran():
    x=np.arange(5,dtype=int)
    _A=np.random.randint(low=-10,high=10,size=20).reshape(4,5)
    A=np.array(_A)
    b=x*A
    print("x:",x)
    print('A:',A)
    print('b=',b)
    return b
#2
def nhan2_ma_tran():
    _A = np.random.randint(low=-10, high=10, size=20).reshape(4, 5)
    A = np.array(_A)
    _B=np.random.randint(low=-10,high=10,size=20).reshape(4,5)
    B=np.array(_B)
    D=np.multiply(A,B)
    print('D=',D)
    return D
def nhan2_ma_tran1():
    _A = np.random.randint(low=-10, high=10, size=20).reshape(4, 5)
    A = np.array(_A)
    A_chuyenvi=A.T
    _B = np.random.randint(low=-10, high=10, size=20).reshape(4, 5)
    B = np.array(_B)
    Z=np.dot(A_chuyenvi,B)
    print('z=',Z)
    return Z

def main():
    vector_nhan_matran()
    nhan2_ma_tran()
    nhan2_ma_tran1()

if __name__=='__main__':
    main()