from ScapyUtil import ScapyUtil

class FileList:
    
    def list_of_file(self, size):
        scapy = ScapyUtil()
        packets = scapy.read_pcap("example.pcap")
        p_len = len(packets)
        n = int(p_len/size)
        inner_lst = []
        #mod_diff = (p_len - (p_len%size) -1)
        
        for j in range(0, p_len, n):
            if j == ((size*n)-n):
                inner_lst.append(str(j)+":"+str(p_len-1))
                break
            else:
                inner_lst.append(str(j)+":"+str(j+(n-1)))
            
        print(inner_lst)
        print("BREAK INTO DATASETS...")
        
        return inner_lst
    
obj = FileList()
print(len(obj.list_of_file(4)))