from mpi4py import MPI
from ScapyUtil import ScapyUtil
import main

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
   file_lst = main.list_of_file()
   
else:
   data = None
   
file_lst = comm.scatter(file_lst, root=0)

print(" File List in rank "+rank+" File_Lst : "+file_lst)