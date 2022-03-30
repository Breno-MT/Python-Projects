#função fatorial - (n! = n *(n-1)) * ...* 1) - !1=1 !0=1
# 5! = 5*4!
# 4! = 4*3!
# 3! = 3*2!
# 2! = 2*1!
# 1! = 1
def fatorial(n):
    if n == 0:
        return 1
    
    return n * fatorial(n - 1)

print(fatorial(10))
