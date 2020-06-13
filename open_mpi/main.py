from ScapyUtil import ScapyUtil

class FileList:
    
    def list_of_file(self, size):
        scapy = ScapyUtil()
        packets = scapy.read_pcap("example.pcap")
        i = 0
        file_lst = []
        
        for pkt in packets:
            new_scapy = ScapyUtil()
            file_name = "pkt_"+str(int(new_scapy.get_timestamp())+i)+".pcap"
            file_lst.append(str(pkt.summary())) 
            i += 1
            print(file_name)
            new_scapy.write_pcap(pkt, file_name)
            
        mod_size = (i/size)+1
        final_lst = []
        inner_lst = []
        
        print("Chunking datasets....")
        for k in range(i):
            if (k+1) % mod_size == 0:
                inner_lst.append(file_lst[k])
                final_lst.append(inner_lst)
                inner_lst = []
                
            else:
                inner_lst.append(file_lst[k])
        
        if len(inner_lst) != 0:
            final_lst.append(inner_lst)
            
        return final_lst