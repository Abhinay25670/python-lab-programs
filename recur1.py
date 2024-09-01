def gcd_with_recursive(a,b):
    if b == 0:
        return a
    else:
        return gcd_with_recursive(b,a%b)
    
def gcd_without_recursive(c,d):
    while d :
        c,d= d,c%d
    return c

a =81
b=27
c=48
d=36

print(gcd_with_recursive(a,b))
print(gcd_with_recursive(c,d))
print(gcd_without_recursive(c,d))
print(gcd_without_recursive(a,b))