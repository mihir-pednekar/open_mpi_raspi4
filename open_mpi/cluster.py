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
pkts = None
pcap_file_name = sys.argv[1]
rule_file_name = sys.argv[2]
file_list_obj = FileList()
rule_map = None

if rank == 0:
   file_lst, pkts = file_list_obj.list_of_file(size, pcap_file_name)
   rules = file_list_obj.read_rule(rule_file_name)
   for pkt in pkts:
       print(pkt[Ether].fields_desc)
    
else:
   file_lst, pkts = file_list_obj.list_of_file(size, pcap_file_name)
   rules = file_list_obj.read_rule(rule_file_name)
   rule_map = file_list_obj.map_of_rules(rules)
   for pkt in pkts:
       print(pkt[Ether].fields_desc)
   
scatter_lst = comm.scatter(file_lst, root=0)

n2=dt.datetime.now()
print("<================ RANK "+str(rank)+" TIME DIFF : "+str(((n2-n1).microseconds)/1000)+" ms. ================>")