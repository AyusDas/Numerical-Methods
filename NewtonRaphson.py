EQN = [[3,1],[2,4],[1,1],[0,-6]] # user
ERROR = 0.001
visited = set()
deg = max(EQN)[0]

def plug(eqn,x0):
        val = 0
        for term in eqn:
            if term[0] == 0:
                val += term[1]
            else:
                val += term[1]*(x0**term[0])
        return val

def getTan(eqn):
        tan = [[] for i in range(deg+1)]
        for i,term in enumerate(eqn):
            if term[0] == 0:
                tan[i].append(1) 
                tan[i].append(0)
            else:
                tan[i].append(term[0]-1)
                tan[i].append(term[1]*term[0])
        return tan

def getTanIntercept(eqn,root):
        if plug(getTan(eqn),root) == 0 :
            return root+1
        else:
            return root-(plug(eqn,root)/plug(getTan(eqn),root))

def getRoot(eqn,root):
        while abs(plug(eqn,root)) > ERROR:
            if root not in visited:
                visited.add(root)
                root = getTanIntercept(eqn,root)
            else:
                visited.clear()
                root += 1
        print("root = ", root)

getRoot(EQN,0)
