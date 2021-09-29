""" Napisati kod koji za date katete a i b (a<b) pravouglog trougla računa površinu i
zapreminu tijela koje se dobija rotacijom trougla oko manje katete. 
"""
import math
"""
Prilikom rotacije pravouglog trougla dobijamo pravu kupu, gdje je a poluporecnik kupe, a stranica b je kruzni isjecak s
"""
a=1
b=2
c = math.sqrt(a*a+b*b)
p = a*(a+c)*3.14
v = (a*a*3.14*b)*1/3

print(c)
print(p)
print(v)