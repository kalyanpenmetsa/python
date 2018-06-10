#Triangular series addition
def tri(n):
        n = n + 1
        sum=0
        for i in range(1,n+1):
                sum = sum + (n-i)
        print(sum)
#Fibonacci Function
def fibo(n):
        fibolist = [1,2]
        for i in range(1,n-1):
                fibolist.append(fibolist[i] + fibolist[i-1])
        print(fibolist)
fibo(50)
