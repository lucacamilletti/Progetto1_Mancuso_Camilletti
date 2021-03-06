from Progetto_1 import Partizione
from time import time
import cProfile
import pstats
a = [7, 10, 20, 40, 100]
f = [1000, 5000, 10000, 30000, 50000, 80000, 100000]

for k in f:
    t = str(k)
    for seq in range(1, 3):
        for j in a:
        
            t2 = str(j)
            print("Risultati per " + t + " elementi con partizione grandi "+ t2 + " : ")
            dic = Partizione(j, int(k/j)*j + j, j)

            start = time()
            cProfile.run('for i in range(k): dic.insert_main(i*seq, i*3)', 'fileOutput')
            p = pstats.Stats('fileOutput')
            p.strip_dirs().sort_stats("time").print_stats()
            temp_insert = time() - start

            print(temp_insert)

            start = time()
            cProfile.run('for i in range(k): dic.search_main(i*seq)', 'fileOutput')
            p = pstats.Stats('fileOutput')
            p.strip_dirs().sort_stats("time").print_stats()
            temp_search = time() - start

            print(temp_search)

            start = time()
            cProfile.run('for i in range(k): dic.delete_main(i*seq)', 'fileOutput')
            p = pstats.Stats('fileOutput')
            p.strip_dirs().sort_stats("time").print_stats()
            temp_delete = time() - start

            print(temp_delete)

    dic = {}

    print("Risultati per " + t + " elementi: ")
    print("\nInserimento:")
    start = time()
    cProfile.run('for i in range(k): dic[i] = i*2', 'fileOutput')
    p = pstats.Stats('fileOutput')
    p.strip_dirs().sort_stats("time").print_stats()
    temp_delete = time() - start
    print(temp_delete)

    print("\nSearch:")
    start = time()
    cProfile.run('for i in range(k): dic[i]', 'fileOutput')
    p = pstats.Stats('fileOutput')
    p.strip_dirs().sort_stats("time").print_stats()
    temp_delete = time() - start
    print(temp_delete)

    print("\nDelete:")
    start = time()
    cProfile.run('for i in range(k): del dic[i]', 'fileOutput')
    p = pstats.Stats('fileOutput')
    p.strip_dirs().sort_stats("time").print_stats()
    temp_delete = time() - start
    print(temp_delete)

    cProfile.run('dic[1] = 2', 'fileOutput')
    p = pstats.Stats('fileOutput')
    p.strip_dirs().sort_stats("time").print_stats()
