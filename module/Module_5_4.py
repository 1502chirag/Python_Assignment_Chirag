'''

Write a Python program to count the occurrences of each word in a given sentence

'''



def occur(sentence):
    sentence=sentence.replace("."," ")
    sentence=sentence.replace(","," ")
    output={}
    char=sentence.split()
    for i in char:
        output[i]=output.get(i, 0)+1
    return output

name="The kids were loud. They were way too loud for Jerry, especially since this was a four-hour flight. The parents didn't seem to be able, or simply didn't want, to control them. They were yelling and fighting among themselves and it was impossible for any of the passengers to concentrate or rest. He thought about politely tapping on the parents' shoulders and asking them to try and get their kids under a bit more control, but before he did he came up with a better idea. Sure, it was a bit sinister, and he'd probably end p in a lot of trouble, but he really didn't care at that point."
print(occur(name))
