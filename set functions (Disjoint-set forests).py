class Node:
    def __init__(self,data):
        self.data = data
      #  self.parent=self
      #  self.rank = 0

def makeset(x):   # this function creates a single set / node
    s = Node(x)
    s.parent = s   # it stats that that the s is a single note/set thats why 's' is the parent of iteself .
    s.rank=0       # initial rank = 0
    return s

def findset(x):    # this will return the parent/ representative of a tree / set
                   # the parent pointers of each node found along the way to point to the representative. 
    if x != x.parent:
        x.parent = findset(x.parent)
    return x.parent

def union(x, y):     # this will unite 2 trees/sets and will return their new representative/parent
                     # by comparing the ranks of both trees /sets

        if findset(x).rank > findset(y).rank:
            findset(y).parent = findset(x)
            return x
        else:
            findset(x).parent = findset(y)
            if findset(x).rank == findset(y).rank:      # if both have same ranks it will increment the rank of anyone of them.
                                                        # to make it parent
                findset(y).rank = findset(y).rank + 1       # we have incremented the rank of y to make it parent
            return y


# DRIVER CODE

# making disjoint sets out of them
print('---make set---')

# tree 1
s1 = makeset('d')
s2 = makeset('f')
s3 = makeset('g')

# tree 2
s4=makeset('b')
s5=makeset('c')
s6=makeset('e')
s7=makeset('h')

# these should print Nodes object
print('tree 1')
print("Set 1:",s1.data) # if u want to print their values, do s1.data otherwise if you want its location remove .data
print("Set 2:",s2.data)
print("Set 3:",s3.data)
print('tree 2')
print("Set 4:",s4.data)
print("Set 5:",s5.data)
print("Set 6:",s6.data)
print("Set 7:",s7.data)

# taking their union for tree 1
print('---Union---')

s1_s2 = union(s1,s2) #union of s1 and s2
s = union(s1_s2,s3) # union of s1, s2 and s3
print("Representative of the new set  (for tree 1):",s.data) # should print a Node i.e representative of set s

# taking their union for tree 1
s4_s5= union(s4,s5)  #union of s4 and s5
s6_s7 = union(s6,s7) # union of s6 and s7
s4_s7=union(s6_s7,s4_s5)  #complete union of tree 2
print("Representative of the new set  (for tree 2):",s4_s7.data) # should print a Node i.e representative of set

#### final union of both trees :
final_union = union(s4_s7,s)
print("Representative of the final set(union of both trees) :",final_union.data)


print('---find set--')
representative_of_s = findset(s) # parent/representative of set
print("Value of the Representative(for tree 1):",representative_of_s.data) # printing value of representative

representative_of_s2 = findset(s4_s7) # parent/representative of set
print("Value of the Representative(for tree 2):",representative_of_s2.data) # printing value of representative

#### final representative for both trees after union :
representative_of_s3 = findset(final_union) # parent/representative of set
print("Value of the Representative(after union of both trees):",representative_of_s3.data) # printing value of representative