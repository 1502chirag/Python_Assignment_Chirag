'''

Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters

'''

def upper(string):
    
    if len(string)>=4:
        up_count=0
        for i in string[:4]:     # up_count=sum(i.isupper() for i in string)
                up_count+=1
        if up_count>=2:
            return string.upper()
    return string

name="HeLLo World!"
print(upper(name))