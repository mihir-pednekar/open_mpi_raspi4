from ScapyUtil import ScapyUtil

scapy = ScapyUtil()
packets = scapy.read_pcap("example.pcap")

for pkt in packets:
    new_scapy = ScapyUtil()
    file_name = "pkt_"+str(new_scapy.get_timestamp())+".pcap"
    print(file_name)
    new_scapy.write_pcap(pkt, file_name)
    
