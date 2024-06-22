
##########################
## Example of MapReduce ##
list_of_strings = ['abc', 'python', 'dima']

import time
from multiprocessing import Pool
from functools import reduce

N = 80_000_000 # size of data 
chsz = 20_000_000 # size of a chunk
procpool = 4 # number of processors

print("Data size:" + str(N))
print("Chunk size:" + str(chsz))
print("Processor Pool size:" + str(procpool))

llos = list_of_strings*N
## Sequencial with One Processor ##
# step 1:
start_time = time.time() # time before the run
list_of_string_lens = [len(s) for s in llos]
list_of_string_lens = zip(llos, list_of_string_lens)

#step 2:
max_len = max(list_of_string_lens, key=lambda t: t[1])
print("Time with One Processor")
print(time.time() - start_time)# time when done

## MapReduce ##

mapper = len

def reducer(p, c):
	if p[1] > c[1]:
		return p
	return c
## create data chuks to be processed
def chunkify(lst,n=1):
	return [lst[i:i + n] for i in range(0, len(lst), n)] 


def chunks_mapper(chunk):
    mapped_chunk = map(mapper, chunk) 
    mapped_chunk = zip(chunk, mapped_chunk)
    return reduce(reducer, mapped_chunk)

## Create a pool of processors to handle the chunks
## Here Pool() has the number of processors. 
## Check how many processors your vmachine can have
## you can start 1,2,3,4..etc

pool = Pool(procpool)

data_chunks = chunkify(llos, n=chsz)

start_time = time.time() # time before run

#step 1:
mapped = pool.map(chunks_mapper, data_chunks)

#step 2:
reduced = reduce(reducer, mapped)
print("Time with Multi Processor:"+str(procpool))
print(time.time() - start_time) # time when done
print(reduced)
