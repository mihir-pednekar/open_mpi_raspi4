from ScapyUtil import ScapyUtil

scapy = ScapyUtil()
packets = scapy.read_pcap("example.pcap")
i = 0

for pkt in packets:
    new_scapy = ScapyUtil()
    file_name = "pkt_"+str(int(new_scapy.get_timestamp())+i)+".pcap"
    i += 1
    print(file_name)
    new_scapy.write_pcap(pkt, file_name)
    
