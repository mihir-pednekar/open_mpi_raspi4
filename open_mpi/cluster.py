from mpi4py import MPI
from ScapyUtil import ScapyUtil
from main import FileList
import datetime as dt

n1=dt.datetime.now()
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
bcast_lst = []
file_lst = None

if rank == 0:
   file_lst = FileList().list_of_file(size)
    
else:
   file_lst = None
   
scatter_lst = comm.scatter(file_lst, root=0)
print("<================ RANK "+str(rank)+" Time Started : "+str(n1)+" ms. ===========>")
print(scatter_lst)
print("RANK "+str(rank)+" time : "+str(n1.microsecond)+" ms.")
for pcap_file in scatter_lst:
    #pkt = ScapyUtil().read_pcap(pcap_file)
    print(pcap_file)

n2=dt.datetime.now()
(n2-n1).microseconds
(n2.microsecond-n1.microsecond)/1e6

print("<================ RANK "+str(rank)+" Time Ended : "+str(n2)+" ms. ===========>")
print("<============= RANK "+str(rank)+" Time Calculated : "+str((n2.microsecond-n1.microsecond)/1e6)+" ms. =====>")