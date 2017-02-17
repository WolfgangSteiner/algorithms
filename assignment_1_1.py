def multiply(a,b):
    def add(a,b) : return str(int(a) + int(b))
    def sub(a,b) : return str(int(a) - int(b))
    def shift(a,shift) : return a + "0" * shift

    if len(a) == 1 and len(b) == 1:
        return str(int(a) * int(b))
    elif len(a) > len(b):
        a,b = b,a

    b = "0" * (len(b) % 2) + b
    a = "0" * (len(b)-len(a)) + a

    a1, a2 = a[0:len(a)//2], a[len(a)//2:]
    b1, b2 = b[0:len(b)//2], b[len(b)//2:]

    A = multiply(a1,b1)
    B = multiply(a2,b2)
    C = multiply(add(a1,a2), add(b1,b2))
    K = sub(sub(C,A),B)
    T1 = shift(A, 2 * len(b) // 2)
    T2 = shift(K, len(b) // 2)
    return add(add(T1, T2), B)


a = "3141592653589793238462643383279502884197169399375105820974944592"
b = "2718281828459045235360287471352662497757247093699959574966967627"
assert(str(int(a) * int(b)) == multiply(a,b))
