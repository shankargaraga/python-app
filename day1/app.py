'''Custom module:app.py'''
import os,sys
print("hi")

name="shankar"  #global variable

def greet(ename):
    # os.system('cls')
    data=[10,20,"shankar"] # private variables
    print(type(data))
    print(data)
    emps=[
        {'eno':10,'ename':'swamy'},
        {'eno':20,'ename':'shankar'}
    ]
    print(type(emps))
    print(emps)
    first,second=(100,200)
    print(first)

if __name__ == "__main__":  # ✅ Correct syntax

  greet("swamy")
  sys.exit()
