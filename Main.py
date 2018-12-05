from X_Project import Partizione
from time import time
import cProfile
import pstats

dic = Partizione(10, 1000010, 10)

start = time()
cProfile.run('for i in range(1000000): dic.insert_main(i, i*2)', 'fileOutput')
p = pstats.Stats('fileOutput')
p.strip_dirs().sort_stats("time").print_stats()
temp_insert = time() - start

print(temp_insert)

start = time()
cProfile.run('for i in range(1000000): dic.search_main(i)', 'fileOutput')
p = pstats.Stats('fileOutput')
p.strip_dirs().sort_stats("time").print_stats()
temp_search = time() - start

print(temp_search)

start = time()
cProfile.run('for i in range(1000000): dic.delete_main(i)', 'fileOutput')
p = pstats.Stats('fileOutput')
p.strip_dirs().sort_stats("time").print_stats()
temp_delete = time() - start

print(temp_delete)