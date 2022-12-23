import numpy as np
#1
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
def list_so_thuc():
    v=np.linspace(start=a,stop=b,num=c,dtype=float)
    return v
 #2

def tang_dan():
 a1 = sorted(list_so_thuc(), reverse=False)
 return a1
print( tang_dan())
def giam_dan():
  a2 = sorted(list_so_thuc(), reverse=True)
  return a2
print(giam_dan())
#3

def tim_vi_tri(list_so_thuc):
    n = float(input('n='))
    s=0
    for i in range(len(list_so_thuc)):
        if list_so_thuc[i]==n:
             s=i
    if s==0:
        print("không tìm thấy vị trí :",n)
    else:
        print('vị trí',s)

def tim_vi_tri1(giam_dan):
    n = float(input('n='))
    s=0
    for i in range(len(giam_dan)):
        if giam_dan[i]==n:
             s=i
    if s==0:
        print("không tìm thấy vị trí :",n)
    else:
        print('vị trí',s)



#4
import os
import pickle
def luu_tap_tin(list_so_thuc):
    x='wb'
    y='wt'
    path="C:\\Users\\HOT_BOY\\PycharmProjects\\pythonProject"
    filename= "chuong.txt"

    with open(os.path.join(path,filename),x) as f:
        pickle.dump(list_so_thuc,f)
    print('kết thúc chương trình lưu tập tin')

# luu_tap_tin(list_so_thuc())
def luu_tap_tin1(giam_dan):
    x = 'wb'
    y = 'wt'
    path = "C:\\Users\\HOT_BOY\\PycharmProjects\\pythonProject"
    filename = "chuong.txt"

    with open(os.path.join(path, filename), x) as f:
        pickle.dump(giam_dan, f)
    print('kết thúc chương trình lưu tập tin')


#5
def main():
    list_so_thuc()
    luu_tap_tin(list_so_thuc)
    giam_dan()
    luu_tap_tin1(giam_dan)
    tim_vi_tri1(giam_dan())

if __name__=="__main__":
    main()

