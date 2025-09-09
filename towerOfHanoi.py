def tower(n,source,helper,destination):
    #base case
    if n == 0:
        return
    #recursive case
    
    # move n disks from source to destination using help

    # 1. ask your friend to move n-1 disks from source to helper

    tower(n-1,source,destination,helper)

    # 2. move the largest disk from source to destination

    print(f'move disk {n} from {source} to {destination}')

    # 3. ask your friend to moove n-1 disk from healper to destination using source

    tower(n-1,helper,source,destination)
    
    


n = int(input())
tower(n,'A','B','C')
    
    
