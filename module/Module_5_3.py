'''

Write a Python function that takes a list of words and returns the length of the longest one

'''




def leng(string1):
     
     if not string1:
          return " "
     else:
          max_len=len(string1[0])
          max_name=string1[0]
          for i in string1:
               if len(i)>max_len:
                    max_len=len(i)
                    max_name=i
          return max_len,max_name
     
list1=["Ganesh","chirag","rahul","kalpana","vijay"]
print(f"lonest word of list : {leng(list1)}")
                



