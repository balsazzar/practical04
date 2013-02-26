alist=[]
def find_largest(alist):
    print(max(alist))
running = True
while running:
    a=input("Enter number (enter s to stop): ")
    if a == "s":
        running = False
    else:
        alist.append(int(a))
find_largest(alist)
