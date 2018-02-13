
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

# def summation(n):
#     total = [0]
#     x = list(range(1, 10000))
#     for i in x:
#         a = i**3
#         total.append(a + total[-1])
#     try:
#         print(total.index(n))
#     except ValueError:
#         print(-1)

# summation(4183059834009)

# import operator
# import functools
# def persistence(n):
#     x = [int(i) for i in str(n)]
#     y = functools.reduce(operator.mul, x, 1)
#     z = [int(i) for i in str(y)]
#     a = functools.reduce(operator.mul, z, 1)
#     b = [int(i) for i in str(a)]
#     c = functools.reduce(operator.mul, b, 1)
#     d = [int(i) for i in str(c)]
#     e = functools.reduce(operator.mul, d, 1)
#     if len(str(n)) == 1:
#         return 0
#     elif len(str(y)) == 1:
#         return 1
#     elif len(str(a)) == 1:
#         return 2
#     elif len(str(c)) == 1:
#         return 3
#     elif len(str(e)) == 1:
#         return 4
#     else:
#         return 5
  
    
# print(persistence(39))

# def min(arr):
#     x = sorted(arr)
#     return x[0]
    

# def max(arr):
#     x = sorted(arr)
#     return x[-1]

# print(min([1,2,3,6,5]))

# import datetime

# def make_readable(seconds):
#         return time.strftime('%H:%M:%S', time.gmtime(seconds))


# print(make_readable(3600))

# def toJadenCase(string):
#     x = string.split()
#     a = [i.capitalize() for i in x]
#     b = " ".join(a)
#     return b
# print(toJadenCase("How can mirrors be real if our eyes aren't real"))



# def invert(lst):
#     newlst = [-i if i > 0 else -i for i in lst]
#     return newlst
# print(invert([1,-3,2,-4]))
##HELP
# def delete_nth(order,max_e):
#     x = order[::-1]
#     for i in x:
#         if x.count(i) > max_e:
#             x.remove((i))
#     return x[::-1]

# print(delete_nth([1,3,4,1,1],1))

# def tribonacci(signature, n):
#     if n <= 3:
#         return signature[0:n]
#     else:
#         i = 0
#         while i < n - 3:
#             signature.append(signature[-1] + signature[-2] + signature[-3])
#             i = i + 1
#         return signature
# print(tribonacci([1,1,1], 0))

# s = ['armstrong', 'weiner', 'doug']
# x = ' '.join(s)

# print('strong' in x)

# def in_array(array1, array2):
#     r = []
#     x = ' '.join(array2)
#     for i in array1:
#         if i in x:
#             r.append(i)
#     return sorted(list(set(r)))
# print in_array()

# def digital_root(n):
#     while len(str(n)) > 1:
#         x = map(int, str(n))
#         n = sum(x)
#     return n
# print(digital_root(99))


##HELP
# def mxdiflg(a1, a2):
#     x = len(min(a1, key=len))
#     y = len(min(a2, key=len))
#     z = len(max(a1, key=len))
#     w = len(max(a2, key=len))
#     if x > y:
#         a = y
#     else:
#         a = x
#     if z > w:
#         b = z
#     else:
#         b = w
#     return b - a

# s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
# s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
# print(mxdiflg(s1,s2))

# def remove_smallest(numbers):
#     if numbers == []:
#         return numbers
#     else:
#         numbers.remove(min(numbers))
#         return numbers


# def gimme(input_array):
#     return sorted(input_array)[1]

# print(gimme([2,3,1]))

# import itertools
# def to_weird_case(string):
#     if len(string.split(' ')) == 1:
#         x = list(string)
#         a = map(str.upper, x[::2])
#         del x[0]
#         y = x[::2]
#         ans = filter(None, sum(itertools.izip_longest(a, y), ()))
#         return ans
#     else:
#         for i in string.split(' '):
#             x = list(string)
#             a = map(str.upper, x[::2])
#             del x[0]
#             y = x[::2]
#             ans = filter(None, sum(itertools.izip_longest(a, y), ()))
# alphabet = set(ascii_lowercase)
# #alphabet = 'abcdefghijklmnopqrstuvwxyz'
# def find_missing_letter(chars):
#     # x = []
#     # for i in chars:
#     #     if i in alphabet:
#     #         x.append(i)
#     # return x
#     missingletter=(alphabet-chars).pop()
#     return missingletter
        
        
    

    
# print find_missing_letter(['a','b','c','d','f'])

# def series_sum(n):
#     x = [1]
#     for i in range(n):
#       x.append(1/(i+3))
#     return (sum(x))
# print series_sum(2)


# def title_case(title, minor_words):
#     x = title.split()
#     a = [i.capitalize() for i in x]
#     b = " ".join(a)
#     for i in minor_words
#     if i in minor_words:
#         a.remove('A')
#     return a

# print(title_case('a clash of KINGS', 'A An The Of'))

