'''

Write a Python program to count and display the vowels of a given text

'''


def fvowel(string):
    vowel_li=[]
    vowel="aeiouAEIOU"
    vo_count=0
    for i in string:
        if i in vowel:
             vo_count +=1
        if i not in vowel_li:
            vowel_li.append(i)
    return vowel_li,vo_count

name="Rahul"
print(fvowel(name))
    

