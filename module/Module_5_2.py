def cou(string):
   if not string:
    return " "
   else:
     f_char=string[0]
     mod_string=f_char+ string[1:].replace(f_char,'$')
     return mod_string

name=input("please enter the string")
print(f"expected result:{cou(name)}")
   
