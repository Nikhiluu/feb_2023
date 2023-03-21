print("This is My first program")#print is prints the given value
#We use hash symbol to write single-line or in-line comments 
'''
Tripple quotes 
are used to write the
multi-line or block comments
'''
Nikhil = 123 #single value assign to a variable
print(Nikhil)
Nikhil = 123,456,789 #Multiple values assign to single variable
print(Nikhil)
Nikhil=MSD = 7 #Single value assign to multiple variables
print(Nikhil,MSD)
Nikhil,MSD,Raina = 3,7,8 #Multiple values assign to multiple variables
print(Nikhil,MSD,Raina)

nikhil = 10
print(id(nikhil)) # id() function is used to get the address of the value

#working on variable rules
#Valid variable names
nikhil = 1 #Starting with letter
print(nikhil)
_nikhil = 2 #Starting with underscore
print(_nikhil)
ni_khil7 = 123 #Alpha numeric underscore
print(ni_khil7)
#Invalid variable names
'''
12nik = 1 #variable cannot start with numbers
n@34$ = 12 #Variable we don't use the special chars
true = 1 #Keywords cannot used as a variable
'''
#Variable cases
""" 
1. Camel case(camelCase)
2. Pascal case(PascalCase)
3. Snake case(snake_case)
"""
nikhilVallepu = 1 #camel case
print(nikhilVallepu)
nikhil_vallepu = 2 #snake case
print(nikhil_vallepu)
NikhilVallepu = 3 #pascal case
print(NikhilVallepu)

#Python is case sensitive
Nikhil = 1
nikhil = 2
NIKHIL = 3
print(Nikhil,nikhil,NIKHIL)

a=1#int
b=2.0#float
c=2+3j#complex
d=True#bool
e=False#bool
print(a,b,c,d,e)
print(type(a),type(b),type(c),type(d),type(e))#type function is used to know datatype of a variable

#Type Conversions
a=10#int
print(float(a))
print(complex(a))
print(bool(a))
b=12.5#float
print(int(b))
print(complex(b))
print(bool(b))
c=3+4j#We cannot convert the complex into int and float
#print(int(c))
#print(float(c))
print(bool(c))
