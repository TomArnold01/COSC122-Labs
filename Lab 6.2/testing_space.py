def this():    
    
    a=[1,5,6,7,11,11,12] # the top list
    b=[1,3,5,9,12,15,16] # the bottom list
    c=[0]*10
    k=0
    i=0
    j=0
    while k<10:
        if i<5 and j<5:        
            print('Compare: '+str(a[i])+'----'+str(b[j]))
            if a[i]<=b[j]:
                c[k]=a[i]
                k=k+1
                i=i+1
            else:
                c[k]=b[j]
                k=k+1
                j=j+1
        else:
            if i<5:
                c[k]=a[i]
                k=k+1
                i=i+1
            if j<5:
                c[k]=b[j]
                k=k+1
                j=j+1
    print('The merged list lis: ')
    print(c)   
this()