from ScapyUtil import ScapyUtil

scapy = ScapyUtil()
packets = scapy.read_pcap("example.pcap")
i = 0
file_lst = []

def list_of_file():
    for pkt in packets:
        new_scapy = ScapyUtil()
        file_name = "pkt_"+str(int(new_scapy.get_timestamp())+i)+".pcap"
        file_lst.append(file_name) 
        i += 1
        print(file_name)
        new_scapy.write_pcap(pkt, file_name)
        return file_lst
    
