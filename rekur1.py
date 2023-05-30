import timeit
def pangkat(m,n):
    if n==0:#base case
        return 1
    elif n==1:
        return m
    else: return m**pangkat(m,n-1) #recursif case
# print(pangkat(2,2))

def prnt(n):
    # if n==1:#base case
    #     print('Hei')
    # else: #recursif case
    #     print('hei')
    #     prnt(n-1)
    if n>0:
        print(f'{n}d')
        prnt(n-1)
# prnt(2000)

def faktor(n):
    if n==0 or n==1:
        return 1
    else:
        return n*faktor(n-1)
# print(faktor(3))

def fibo(n, list_fibo):
    if n == 1 or n == 2:
        return 1
    else:
        if list_fibo[n-1]!=0:
            return list_fibo[n-1]
        else:
            list_fibo[n-1]=fibo(n-1,list_fibo)+fibo(n+2,list_fibo)
            return fibo(n-1,list_fibo)+fibo(n+2,list_fibo)
# n=5
# list_fibo=[0]*n
# print(fibo(n,list_fibo))


def jumlah(n):
    if n<10:return n
    else: return n%10+jumlah(n//10)
print(jumlah(69))