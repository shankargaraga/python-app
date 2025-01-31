'''def add5(val):
    return val+5

print(add5(100))'''

#singleline fucntions are lambda fucntions
# add5=lambda x:x+5

# print(type(add5))
# print(add5(100))

ss=lambda x:True if x.startswith('S') else False
print(ss('sShankar'))

alist=['learn','python','step','by','step']
output=list(map(lambda x:x.upper(),alist))
print(type(output))
print(output)


# scores=[66,35,55,78,89,99]
# # def is_A_student(scores):
# #     return scores> 75

# # over_75=list(filter(is_A_student,scores))
# print(over_75)

scores=[66,35,55,78,89,99]
check=lambda x:x>75
over_75=list(filter(check,scores))
print(over_75)

list1=[("eggs",5.34),("carrot",66.34),("tree",78.3)]
list1.sort(key=lambda x:x[0],reverse=0)
print(list1)

import numpy as np
shankar=np.array([5,6,7,8,9,10])
squares=lambda y:y**2
output=np.array([squares(ss) for ss in shankar])
print(output)