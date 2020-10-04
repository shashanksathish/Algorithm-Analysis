import math
import sys

def shortest_useful_rope(input_file_path, output_file_path):
    f = open(input_file_path, "r")
    data = f.read()

    input1 = data.translate({ord('('):None}).split('\n')

    data1 = input1[0].split('),')
    data1[len(data1)-1] = str(data1[len(data1)-1]).translate({ord(')'):None})
    p = []
    for i in range(0,len(data1)):
        p.append(list(map(int, data1[i].split(','))))

    data2 = input1[1].split('),')
    data2[len(data2)-1] = str(data2[len(data2)-1]).translate({ord(')'):None})
    q = []
    for i in range(0,len(data2)):
        q.append(list(map(int, data2[i].split(','))))
    
    def dist(p,q):
        dpdist = math.ceil(math.sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q))))
        return dpdist
    
    def dpf(p, q):
        m = len(p)
        n = len(q)

        dp = [[0 for x in range(n+1)] for y in range(m+1)] 

        for j in range(len(q)-1,-1,-1):
            for i in range(len(p)-1,-1,-1):
                dp[i][j] = max(dp[i+1][j], dp[i][j+1], dp[i+1][j+1], dist(p[i],q[j]))

        i = 0
        j = 0
        new_i = 0
        new_j = 0
        while i < len(p) and j < len(q):
            minlist = [dp[i][j+1],dp[i+1][j],dp[i+1][j+1]]
            rope = min(minlist)
            index = [i for i, j in enumerate(minlist) if j == rope]
            if(len(index)>1):
                index = [index[len(index)-1]]
            if(index == [0]):
                new_i = i
                new_j = j+1
            if(index == [1]):
                new_i = i+1
                new_j = j
            if(index == [2]):
                new_i = i+1
                new_j = j+1
            i=new_i
            j=new_j 
        if rope < dist(p[0],q[0]):
            rope = dist(p[0],q[0])
        if(len(p)==1 and len(q) !=1):
            for i in range(0,len(q)-1):
                rope = max(dp[len(p)-1][i],dp[len(p)-1][i+1])
        if(len(p)!=1 and len(q)==1):
            for j in range(0,len(p)-1):
                rope= max(dp[j][len(q)-1], dp[j+1][len(q)-1])
        
        with open (output_file_path, 'w') as file:
            file.write(str(rope))
            
        return rope
        
    dpf(p,q)

    
