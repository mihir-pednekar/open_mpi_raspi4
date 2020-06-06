from ScapyUtil import ScapyUtil

scapy = ScapyUtil()
packets = scapy.read_pcap("example.pcap")

time_lst = []

for pkt in packets:
    new_scapy = ScapyUtil()
    time_lst.append(new_scapy)
    
for pkt in packets:
    for i in range(5):
        file_name = "pkt_"+str(time_lst[i].get_timestamp())+".pcap"
        print(file_name)
        new_scapy.write_pcap(pkt, file_name)
    
