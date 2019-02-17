def to_integer(p):
    return p(lambda x: x + 1)(0)


def to_boolean(p):
    return p(True)(False)


def to_array(proc):
    array = []
    while to_boolean(NOT(IS_EMPTY(proc))):
        array.append(FIRST(proc))
        proc = REST(proc)
    return array


def to_char(c):
    return '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[to_integer(c)]


def to_string(s):
    return ''.join([to_char(c) for c in to_array(s)])


ZERO = lambda p: lambda x: x
ONE = lambda p: lambda x: p(x)
TWO = lambda p: lambda x: p(p(x))
THREE = lambda p: lambda x: p(p(p(x)))
FOUR = lambda p: lambda x: p(p(p(p(x))))
FIVE = lambda p: lambda x: p(p(p(p(p(x)))))
TRUE = lambda x: lambda y: x
FALSE = lambda x: lambda y: y
AND = lambda p: lambda q: p(q)(FALSE)
OR = lambda p: lambda q: p(TRUE)(q)
NOT = lambda p: p(FALSE)(TRUE)
IF = lambda b: lambda x: lambda y: b(x)(y)
IS_ZERO = lambda n: n(lambda x: FALSE)(TRUE)
PAIR = lambda x: lambda y: lambda f: f(x)(y)
LEFT = lambda p: p(lambda x: lambda y: x)
RIGHT = lambda p: p(lambda x: lambda y: y)
INCREMENT = lambda n: lambda p: lambda x: p(n(p)(x))
SLIDE = lambda p: PAIR(RIGHT(p))(INCREMENT(RIGHT(p)))
DECREMENT = lambda n: LEFT(n(SLIDE)(PAIR(ZERO)(ZERO)))
ADD = lambda m: lambda n: n(INCREMENT)(m)
SUBTRACT = lambda m: lambda n: n(DECREMENT)(m)
MULTIPLY = lambda m: lambda n: n(ADD(m))(ZERO)
POWER = lambda m: lambda n: n(MULTIPLY(m))(ONE)
SIX = ADD(THREE)(THREE)
SEVEN = ADD(THREE)(FOUR)
EIGHT = ADD(THREE)(FIVE)
NINE = ADD(FOUR)(FIVE)
TEN = ADD(FIVE)(FIVE)
FIFTEEN = MULTIPLY(THREE)(FIVE)
HUNDRED = POWER(TEN)(TWO)
IS_LESS_OR_EQUAL = lambda m: lambda n: IS_ZERO(SUBTRACT(m)(n))
ZED = lambda f: (lambda x: f(lambda y: x(x)(y)))(
    lambda x: f(lambda y: x(x)(y)))
MOD = ZED(lambda f: lambda m: lambda n: IF(IS_LESS_OR_EQUAL(n)(m))(
    lambda x: f(SUBTRACT(m)(n))(n)(x)
)(
    m
))
EMPTY = PAIR(TRUE)(TRUE)
UNSHIFT = lambda l: lambda x: PAIR(FALSE)(PAIR(x)(l))
IS_EMPTY = LEFT
FIRST = lambda l: LEFT(RIGHT(l))
REST = lambda l: RIGHT(RIGHT(l))
LENGTH = ZED(lambda g: lambda c: lambda x: IF(
    IS_EMPTY(x))(c)(lambda y: g(INCREMENT(c))(REST(x))(y)))(ZERO)
RANGE = ZED(lambda f: lambda m: lambda n: IF(IS_LESS_OR_EQUAL(m)(n))(
    lambda x: UNSHIFT(f(INCREMENT(m))(n))(m)(x)
)(
    EMPTY
))
FOLD = ZED(lambda f: lambda l: lambda x: lambda g: IF(IS_EMPTY(l))(
    x
)(
    lambda y: g(f(REST(l))(x)(g))(FIRST(l))(y)
))
MAP = lambda k: lambda f: FOLD(k)(EMPTY)(lambda l: lambda x: UNSHIFT(l)(f(x)))
A = TEN
B = INCREMENT(A)
C = INCREMENT(B)
D = INCREMENT(C)
E = INCREMENT(D)
F = INCREMENT(E)
G = INCREMENT(F)
H = INCREMENT(G)
I = INCREMENT(H)
J = INCREMENT(I)
K = INCREMENT(J)
L = INCREMENT(K)
M = INCREMENT(L)
N = INCREMENT(M)
O = INCREMENT(N)
P = INCREMENT(O)
Q = INCREMENT(P)
R = INCREMENT(Q)
S = INCREMENT(R)
T = INCREMENT(S)
U = INCREMENT(T)
V = INCREMENT(U)
W = INCREMENT(V)
X = INCREMENT(W)
Y = INCREMENT(X)
Z = INCREMENT(Y)
DIV = ZED(lambda f: lambda m: lambda n: IF(IS_LESS_OR_EQUAL(n)(m))(
    lambda x: INCREMENT(f(SUBTRACT(m)(n))(n))(x)
)(
    ZERO
))
PUSH = lambda l: lambda x: FOLD(l)(UNSHIFT(EMPTY)(x))(UNSHIFT)
TO_DIGITS = ZED(lambda f: lambda n: PUSH(
    IF(IS_LESS_OR_EQUAL(n)(NINE))(
        EMPTY
    )(
        lambda x: f(DIV(n)(TEN))(x)
    )
)(MOD(n)(TEN)))
