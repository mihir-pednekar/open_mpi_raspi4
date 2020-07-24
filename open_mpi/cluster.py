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
list_rule_map = None

if rank == 0:
   rules = file_list_obj.read_rule(rule_file_name)
   list_rule_map = file_list_obj.map_of_rules(rules)
   file_lst, pkts, p_len = file_list_obj.list_of_file(size, pcap_file_name)
    
else:
   rules = file_list_obj.read_rule(rule_file_name)
   list_rule_map = file_list_obj.map_of_rules(rules)
   file_lst, pkts, p_len = file_list_obj.list_of_file(size, pcap_file_name)
   for pkt in pkts:
       for field in pkt['Ethernet'].fields_desc:
           print(field.name)
   
scatter_lst = comm.scatter(file_lst, root=0)

# get max min index from scatter_lst

for scattr in scatter_lst:
    scat_list = scattr.split(':', 1)
    min_index = scat_list[0]
    max_index = scat_list[1]

print("min : "+min_index)
print("max : "+max_index)
#traverse list of packets
proto_map = {}
for itr in range(0, p_len):
    if pkts[itr].haslayer('Ethernet'):
        print("haslayer(Ethernet)")
           
    elif pkts[itr].haslayer(IP):
        print("haslayer(IP)")
           
for pkt in pkts:
    for field in pkt['Ethernet'].fields_desc:
        print(field.name)

n2=dt.datetime.now()
print("<================ RANK "+str(rank)+" TIME DIFF : "+str(((n2-n1).microseconds)/1000)+" ms. ================>")