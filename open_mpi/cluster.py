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
   
print("<================ RANK "+str(rank)+" ==================>")
scatter_lst = comm.scatter(file_lst, root=0)
print(scatter_lst)
print("<================ RANK "+str(rank)+" ==================>")