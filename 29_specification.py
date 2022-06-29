#**********************************
# * NSI 1ère Lycée Buffon 2020-2021
# * Estelle Doriot
# *
# * TD Test
#**********************************

def est_valide(s):
    cpt1, cpt2, cpt3 = 0, 0, 0
    for c in s:
        if c == "(":
            cpt1 += 1
        elif c == ")" :
            cpt1 -= 1
        elif c == "[":
            cpt2 += 1
        elif c == "]" :
            cpt2 -= 1
        if c == "{":
            cpt3 += 1
        elif c == "}" :
            cpt3 -= 1
    return cpt1 == 0 and cpt2 == 0 and cpt3 == 0

def test_estvalide():
    assert(est_valide("(x[x+y])-1")) == True, "échec pour s=(x[x+y])-1"
    assert(est_valide("{([]){}()}")) == True, "échec pour s={([]){}()}"
    assert(est_valide("x[][]y()")) == True, "échec pour s=x[][]y()"
    assert(est_valide("{(x+y)]")) == False, "échec pour s={(x+y)]"
    assert(est_valide("((()")) == False, "échec pour s=((()"
    #assert(est_valide('([)]')) == False, "échec pour s=([)]"
    print("Test réussi")

test_estvalide()

def premier(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_prime_2(n):
    return n == 2 or 2**n % n == 2

def pseudo_premier():
    i = 2
    while premier(i) or not is_prime_2(i):
        i += 1
    return i

print(pseudo_premier())