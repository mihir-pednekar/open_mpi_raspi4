from ScapyUtil import ScapyUtil

scapy = ScapyUtil()

packets = scapy.read_pcap("example.pcap")

for i in range(0,5):
    for pkt in packets:
        file_name = "pkt_"+str(scapy.get_timestamp())
        print(file_name)
        scapy.write_pcap(pkt[i], file_name)
    
