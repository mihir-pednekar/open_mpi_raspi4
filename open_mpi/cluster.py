from mpi4py import MPI
from ScapyUtil import ScapyUtil

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
   scapy = ScapyUtil()
   packets = scapy.read_pcap("example.pcap")
   
else:
   data = None
   
data = comm.scatter(data, root=0)
data += 1
print 'rank',rank,'has data:',data

newData = comm.gather(data,root=0)

if rank == 0:
   print 'master:',newData