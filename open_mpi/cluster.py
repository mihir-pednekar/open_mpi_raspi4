from mpi4py import MPI
from ScapyUtil import ScapyUtil
from main import FileList

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
print("<================ RANK "+str(rank)+" ==================>")
print(scatter_lst)

for pcap_file in scatter_lst:
    pkt = ScapyUtil().read_pcap(pcap_file)
    print(pkt[0].nsummary())
print("<================ RANK "+str(rank)+" ==================>")