# for loop + zip
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']
for a, b in zip(alist, blist) :
    print(a, b)

# list comprehension + zip
a, b, c = zip((1, 2, 3), (10, 20, 30), (100, 200, 300))
print(a, b, c)
print([sum(x) for x in zip((1, 2, 3), (10, 20, 30), (100, 200, 300))])

# enumerate + zip
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']
for i, (a, b) in enumerate(zip(alist, blist)) :
    print(i, a, b)