from sympy import *
#1
def he_phuong_trinh():
    x,y,z=symbols("x,y,z")
    eq1=Eq(2*x-5*y+z,-5)
    eq2=Eq(4*x+2*y-2*z,2)
    eq3=Eq(x+y-z,0)
    answer=solve((eq1,eq2,eq3),(x,y,z))
    print('a1=',answer)
    return answer
def tinh_gioi_han():
    x=symbols('x')
    f=(x**3-3*x**2)**1/3+sqrt(x**2-2*x)
    answer=limit(f,x,+oo)
    print('a2=',answer)
    return answer

def dao_ham():
    x=symbols('x')
    f=(2*x-1)/(x+2)
    answer=diff(f,x)
    print('a3=',answer)
    return  answer
def nguyen_ham():
    x=symbols('x')
    f=x/(x**2+1)
    answer=integrate(f,x)
    print('a4',answer)
    return answer

def tich_phan():
    x=symbols("x")
    f=(1-x*tan(x))/(x**2*cos(x)+x)
    answer=integrate(f,(x,pi,(2+pi)/3))
    print('a5=',answer)
    return answer
def main():
    he_phuong_trinh()
    tinh_gioi_han()
    dao_ham()
    nguyen_ham()
    tich_phan()

if __name__=='__main__':
    main()