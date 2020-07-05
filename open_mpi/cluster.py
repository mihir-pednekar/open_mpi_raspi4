from mpi4py import MPI
from ScapyUtil import ScapyUtil
from main import FileList
import datetime as dt
import sys

n1=dt.datetime.now()
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
file_lst = None
pcap_file_name = sys.argv[1]
rule_file_name = sys.argv[2]

if rank == 0:
   file_lst, pkts = FileList().list_of_file(size, pcap_file_name)
    
else:
   file_lst = None
   
scatter_lst = comm.scatter(file_lst, root=0)
for pcap_file in scatter_lst:
    #IDS Algorithm left to be implemented..
    print(pcap_file)

n2=dt.datetime.now()
print("<================ RANK "+str(rank)+" TIME DIFF : "+str(((n2-n1).microseconds)/1000)+" ms. ================>")