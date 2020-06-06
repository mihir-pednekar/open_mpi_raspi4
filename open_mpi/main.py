from ScapyUtil import ScapyUtil

packets = scapy.read_pcap("example.pcap")

for i in range(0,5):
    for pkt in packets:
        scapy = ScapyUtil()
        file_name = "pkt_"+str(scapy.get_timestamp())
        print(file_name)
        scapy.write_pcap(pkt, file_name)
    
