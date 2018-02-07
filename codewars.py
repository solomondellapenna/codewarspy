
#LEVEL 1 PYTHON
# from collections import Counter

# def printer_error(s):
#     total = str(len(s))
#     a = Counter(s)
#     detect = str(a['n'] + a['o'] + a['p'] + a['q'] + a['r'] + a['s'] + a['t'] + a['u'] + a['v'] + a['w'] + a['x'] + a['y'] + a['z'])
#     print(detect + '/' + total)
# s = "aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
# printer_error(s)

#LEVEL 2 PYTHON
# from collections import Counter
# def compare(s, t):
#     if s[0] == t[0]:
#         s.pop(0)
#     elif s[0] == t[1]:
#         s.pop(0)
#     print(s)

#compare([1,2], [2,1])

# def array_diff(a, b):
#     removal_list = [i for i in a if i in b]
#     try:
#         a.remove(removal_list[0])
#         a.remove(removal_list[1])
#         a.remove(removal_list[2])
#         a.remove(removal_list[3])
#         a.remove(removal_list[4])
#         a.remove(removal_list[5])
#         a.remove(removal_list[6])
#     except IndexError:
#         print(a)
    

# array_diff([1,2],[1])



#LEVEL 3 PYTHON

# from collections import Counter
# def find_it(seq):
#     x = Counter(seq)
#     if x[5] % 2 != 0:
#         print(x) 
    






# #Test if number is square
# def is_square(n):
#     try:
#         if (n**(1/2.0)).is_integer():
#             return True
#         else:
#             return False
#     except AttributeError:
#         return False
#     except ValueError:
#         return False
        