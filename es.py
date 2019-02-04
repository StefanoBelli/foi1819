# funz ricorsiva
# 2 lug 2013 testo 1

def sum_even_from_list(l_intg):
    # @param l_intg : list
# @return int
    if not len(l_intg):
        return 0

    if l_intg[0] % 2 == 0:
        return l_intg[0] + sum_even_from_list(l_intg[1:])

    return sum_even_from_list(l_intg[1:])

# classe

class Quadrato:
    def __init__(self, lato):
        self.lato = lato

    def Area(self):
        return self.lato * self.lato

    def Perimetro(self):
        return self.lato * 4

quad = Quadrato(2)
print(quad.Area())
print(quad.Perimetro())

# conv di base
#x = 1100110 B=2
#y = 2012 B=3

#x = 1100110 = 1 * 2^6 + 1 * 2^5 + 0 + 0 + 1 * 2^2 + 1 * 2^1 + 0 = 64 + 32 + 4 + 2 = 102 B=10
#y = 2012 = 2 * 3^3 + 0 + 1 * 3^1 + 2 * 3^0 = 54 + 3 + 2 = 59 B=10

#relazione d'ordine: y < x <=> x > y

##  2 lug 13 altro testo, solo prob 1

def concat_strings_even_length(s_list):
    if not len(s_list):
        return ""

    if not len(s_list[0]) % 2:
        return s_list[0] + concat_strings_even_length(s_list[1:])

    return concat_strings_even_length(s_list[1:])

## 20 sett 2013
def atleast_one_string_has_x_char(s_list, x):
    if not len(s_list):
        return False

    if s_list[0].find(x) == -1:
        return atleast_one_string_has_x_char(s_list[1:], x)
    
    return True

print(atleast_one_string_has_x_char(["kiao","kiaone"], 'k'))

## 15 lug 2014
def dotted_after_alpha_or_digit(st):
    if not len(st):
        return str()

    if st[0].isalpha() or st[0].isdigit():
        return st[0] + '.' + dotted_after_alpha_or_digit(st[1:])

    return st[0] + dotted_after_alpha_or_digit(st[1:])

print(dotted_after_alpha_or_digit("kiao123"))

# (102 -01) => ( 1 * 3 ^ -1 + 0 + 2 * 3^-3 )10^-1

## 18 lug 2013

def delete_cc(x):

    x_len = len(x)
    if x_len == 1:
        return x[0]
    
    if x[0] == x[1]:
        return delete_cc(x[1:])

    return x[0] + delete_cc(x[1:])

print(delete_cc("aaaabbcc"))

## 19 feb 2014

def k_pos_multiple(L,V,K, idx = 0):
    if len(L) == idx:
        return True

    if (idx+1) % K == 0:
        if L[idx] != V:
            return False

    return k_pos_multiple(L,V,K,idx + 1)

print(k_pos_multiple([1,3,2,3], 3, 2))

## 18 lug 2014

def space_between(s):
    if not len(s):
        return ""

    return s[0] + ' ' + space_between(s[1:])

print(space_between("kiao"))

class Persona:
    def __init__(self, eta, nome, amici):
        self.eta = eta
        self.nome = nome
        self.amici = amici

    def get_eta(self):
        return self.eta

    def get_nome(self):
        return self.nome

    def aggiungi_amico(self, nuovo_amico):
        self.amici.append(nuovo_amico)

p = Persona(19, "ste", [ Persona(18, "fra", []), Persona(18, "manu", []) ])
print(p.get_eta())
print(p.get_nome())
p.aggiungi_amico(Persona(20, "andre", []))

class Insegnante(Persona):
    def __init__(self, eta, nome, amici, materia, stipendio):
        Persona.__init__(self, eta, nome, amici)
        self.materia = materia
        self.stipendio = stipendio

    def get_materia(self):
        return self.materia

    def get_stipendio(self):
        return self.stipendio

    def set_materia(self, nome_materia):
        self.materia = nome_materia

i = Insegnante(50, "Vincenzo Grassi", [], "Fondamenti di Informatica", 600)
print(i.get_eta())
print(i.get_nome())
print(i.get_materia())
i.set_materia("cosmologia")
print(i.get_materia())

## 30 giugn 2014
def __sum_in_listL(L):
    if not len(L):
        return 0

    return L[0] + __sum_in_listL(L[1:])

def is_sum_even(L):
    return __sum_in_listL(L) % 2 == 0

print(is_sum_even([1,2,3,1]))

#----

def is_sum_even_v2(L, keep_sum=0):
    if not len(L):
        return keep_sum % 2 == 0

    first_elem = L[0]
    return is_sum_even_v2(L[1:], keep_sum + first_elem)

print(is_sum_even_v2([]))

## 5 sett 2013

# lis[i] + lis[len(lis) - i - 1] = x per ogni i < len(lis)/2

def check_prop(lis, x, i=0):
    lislen = len(lis)
    midpoint = lislen / 2

    if i > midpoint:
        return True

    if i < midpoint and not lis[i] + lis[lislen - i - 1] == x:
            return False

    return check_prop(lis, x, i + 1)

print(check_prop([1,5,3,6,4,8], 9))
print(check_prop([1,5,3,7,6,4,8], 9))
print(check_prop([1,5,2,6,4,8], 9))
