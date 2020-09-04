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
p_len = None
min_index = None
max_index = None
pcap_file_name = sys.argv[1]
rule_file_name = sys.argv[2]
file_list_obj = FileList()
rule_map = None

if rank == 0:
   rules = file_list_obj.read_rule(rule_file_name)
   rule_map = file_list_obj.map_of_rules(rules)
   file_lst, pkts, p_len = file_list_obj.list_of_file(size, pcap_file_name)
   print(file_lst)
    
else:
   rules = file_list_obj.read_rule(rule_file_name)
   rule_map = file_list_obj.map_of_rules(rules)
   file_lst, pkts, p_len = file_list_obj.list_of_file(size, pcap_file_name)
   
scatter_lst = comm.scatter(file_lst, root=0)

# get max min index from scatter_lst
min_index, max_index = file_list_obj.get_min_max(scatter_lst)
#print("min : "+str(min_index))
#print("max : "+str(max_index))

#create proto_map = {0: {'Ethernet': {}, 'IP': {}, 'TCP': {}}}
proto_map = file_list_obj.create_proto_map(min_index, max_index, pkts, rule_map)
#print(proto_map)
#print("<================================>")
#print(rule_map)
print(file_list_obj.process_pkt(min_index, max_index, proto_map, rule_map))

n2=dt.datetime.now()
print("<================ RANK "+str(rank)+" TIME DIFF : "+str(((n2-n1).microseconds)/1000)+" ms. ================>")