K = int(input())
L = int(input())
M = int(input())
N = int(input())
counter = 0
for i in range(K, 9):
    ##print(i)
    for j in range(9, L-1, -1):
        #print(j)
        # if i % 2 == 0 and j % 2 != 0:
        #     pass
        for k in range(M, 9):
            #print(k)
            for l in range(9, N - 1, -1):
                #print(l)
                if i % 2 == 0 and j % 2 != 0 and k % 2 == 0 and l % 2 != 0:
                    if i != k or j != l:
                        if counter < 6:
                            print(f"{i}{j} - {k}{l}")
                        counter = counter + 1
                    else:
                        if counter < 6:
                            print("Cannot change the same player.")