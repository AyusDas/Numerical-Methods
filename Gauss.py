coeff = [[1,1,-1,-2],[2,-1,1,5],[-1,2,2,1],[0,0,0,0]]
soln = []
N = len(coeff)

def display(arr):
    print("")
    for i in arr:
        for j in i:
            print(j,end=" ")
        print("")
    print("")

def gaussElimination(arr):
    display(arr[:-1])   
    for c in range(N) :
        for r in range(c+1,N):
            m,n = arr[c][c], arr[r][c]
            for k in range(N):
                arr[r][k] = m*arr[r][k] - n*arr[c][k]            

    arr = arr[:-1]
    for j,i in enumerate(arr):
        k = i[j]
        for n in range(len(i)):
            if k != 0:
                i[n] = i[n]/k
                if abs(i[n]-int(i[n])) == 0 : i[n] = int(i[n]) 
    display(arr)

    for i in arr:
        soln.append(i[-1])
    for i in range(len(soln)-2,-1,-1):
        k = i + 1
        for j in range(i+1,N-1):
            soln[i] -= arr[i][j]*soln[k]
            k += 1          
    print("\nsolutions :\n",soln,"\n")

gaussElimination(coeff)
