import inspect

class E:
    pass


class D:
    pass


class C(E):
    pass


class B(D):
    pass


class A(B, C):
    pass


print(inspect.getmro(A))