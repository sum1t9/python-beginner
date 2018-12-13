tree_height = input('Enter the height of the tree')
tree_height = int(tree_height)
center_width = input("Enter the Width :")

center_height = input("Enter the height :")

base_height = input("Enter the base Height")
hashes =tree_height+ 1
spaces = 0

while tree_height != 0:


    for i in range(spaces):
        print(' ',end="")

    for i in range(hashes):
        print('#',end="")

    print()
    hashes -= 2
    spaces += 1
    tree_height -=1


center_width = int(center_width)
center_height = int(center_height)

hashes_1 = center_height

while center_height != 0:
    for i in range(hashes_1):
        print("#",end="")
    for i in range(center_width):
        print("#",end="")

    print()
    center_height -= 1


base_height = int(base_height)
hashes_2 = 1
spaces_2 = base_height - 1

while base_height != 0:
    for i in range(spaces_2):
        print(" ",end="")
    for i in range(hashes_2):
        print("#",end="")

    print()
    base_height -=1
    hashes_2 +=2
    spaces_2 -= 1

