'''

Write a Python program to count the number of characters (character frequency) in a string

⚫ Sample String:google.com'

Expected Result: (o 3, 'g: 2, 1, 'e': 1, T: 1, 'm: 1, 'e: 1)

'''


def character_founder(string):
    output={}
    for i in string:
        key=output.keys()
        if i not in key:
            output[i]=1
        else:
            output[i] +=1
    return output
name=input("please enter the string")
print(f"expected result: {character_founder(name)}")