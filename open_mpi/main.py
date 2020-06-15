from ScapyUtil import ScapyUtil

class FileList:
    
    def list_of_file(self, size):
        scapy = ScapyUtil()
        packets = scapy.read_pcap("example.pcap")
        i = 0
        file_lst = []
        
        for pkt in packets:
            file_lst.append(str(pkt.summary())) 
            i += 1
            
        mod_size = (i/size)
        final_lst = []
        inner_lst = []
        
        print("BREAK INTO DATASETS...")
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