def add_product(l,add_p):
    l.append(add_p)
    print(l)
def remove_product(l,remove_p):
    l.remove(remove_p)
def search_product(l,search_p):
    if search_p in l:
        return "elemenent found"
    else:
        return "element not found"
def display(l):
    return l
def total_p(l):
    return len(l)
def sort_l(l):
    l.sort()
    return l
def clear_l(l):
    l.clear()
    return l

l=list(map(str,input().split()))
d=int(input())
for i in range(d):
   choice=int(input())
   match choice:
        case 1:
            add_p=input()
            add_product(l,add_p)
            print("itenm added:",add_p)
        case 2:
            remove_p=input()
            remove_product(l,remove_p)
            print("itenm removed:",remove_p)
        case 3:
            search_p=input()
            print("itenm searchrd:",search_product(l,search_p))
        case 4:
            print(display(l))
        case 5:
            print(total_p(l))
        case 6:
            print("sorted list",sort_l(l))
        case 7:
           print("clear list:",clear_l(l))
        case 8:
           print("exiting")







    
