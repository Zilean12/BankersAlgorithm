
from tabulate import tabulate

def Bankers(process, Allocation, maximum, avail):
    l = len(process)
    K = len(avail)

    Need = [[maximum[R][q] - Allocation[R][q] for q in range(K)] for R in range(l)]
    Safe_Seq = []
    A = avail[:] 
    finish = [False] * l

    while True:
        found = False
        for R in range(l):
            if not finish[R] and all(Need[R][Q] <= A[Q] for Q in range(K)):
                A = [A[Q] + Allocation[R][Q] for Q in range(K)]
                finish[R] = True
                Safe_Seq.append(process[R])
                found = True

        if not found:
            break

    if all(finish):
        table_headers = ["process", "allocation", "max", "available", "need"]
        table_data = []
        for R in range(l):
            row = [process[R], Allocation[R], maximum[R], avail, Need[R]]
            table_data.append(row)
        
        print(tabulate(table_data, headers=table_headers, tablefmt="rounded_grid"))
        print("\n safe sequence:", Safe_Seq)
    else:
        print("unsafe state.")


process = ['p0', 'p1', 'p2', 'p3', 'p4']
Allocation = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]
maximum = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
avail = [3, 3, 2]

Bankers(process, Allocation, maximum, avail)
