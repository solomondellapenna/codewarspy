# import datetime



# def age100(name, age):
#     x = 100 - age
#     now = datetime.datetime.now()
#     finalyear = now.year + x
#     output = name + ', you will turn 100 in ' + str(finalyear)
#     print(output)

# name = input("What's your name? " )
# age = int(input("How old will you be at the end of the year? "))
# age100(name, age)


# import collections
# def list_diff(l1, l2):
#     a = set(l1) & set(l2)
#     print(a)

# l1 = [1,2,3]
# l2 = [3,1,2]
# list_diff(l1,l2)


def tower_builder(n_floors):
    i=0
    x = []
    a=0
    y = " " * n_floors
    while i < n_floors:
        x.append("{0}".format(y))
        i += 1
    x = str(x)
    while a < n_floors:
        x[:5] + '*' + x[5:]
        i += 8
    #print(x)
tower_builder(6)
