from ScapyUtil import ScapyUtil

class FileList:
    
    def list_of_file(self, size, pcap_file_name):
        scapy = ScapyUtil()
        packets = scapy.read_pcap(pcap_file_name)
        p_len = len(packets)
        n = int(p_len/size)
        inner_lst = []
        size_diff = ((size*n)-n)
        
        for j in range(0, p_len, n):
            if j == size_diff:
                local_lst = []
                local_lst.append(str(j)+":"+str(p_len-1))
                inner_lst.append(local_lst)
                break
            else:
                local_lst = []
                local_lst.append(str(j)+":"+str(j+(n-1)))
                inner_lst.append(local_lst)
            
        print(inner_lst)
        print("<================ BREAK INTO DATASETS ================>")
        
        return inner_lst, packets, p_len
    
    def read_rule(self, rule_file_name):
        #read all rules
        rule_file = open(rule_file_name, 'r')
        rules = rule_file.readlines()
        return rules
    
    def map_of_rules(self, rules):
        #list_rule_map = []
        final_map = {'Ethernet' : [], 'IP' : [], 'TCP' : [], 'ICMP' : [], 'Raw' : []}
        for rule in rules:
            rule_map = {}
            x = rule.split(" ", 7)
            rule_map['task'] = x[0]
            #rule_map['proto'] = x[1]
            rule_map['direc'] = x[4]
            if x[4] == '->':
                rule_map['src'] = x[2]
                rule_map['sport'] = x[3]
                rule_map['dst'] = x[5]
                rule_map['dport'] = x[6]
                
            else:
                rule_map['src'] = x[5]
                rule_map['sport'] = x[6]
                rule_map['dst'] = x[2]
                rule_map['dport'] = x[3]
            
            trim_str = x[7].strip('(').strip(')')
            trim_list = trim_str.split("; ")
            temp_map = {}
            
            for trim in trim_list:
                temp_list = trim.strip(';').split(":")
                #print(temp_list)
                temp_map[temp_list[0]] = temp_list[1].strip(";)\n").strip('"').strip('"')
            
            rule_map['para'] = temp_map
            final_map[x[1]].append(rule_map)
            #list_rule_map.append(rule_map)
        
        return final_map
    
    def get_min_max(self, scatter_lst):
        min_index = 0
        max_index = 0
        for scattr in scatter_lst:
            scat_list = scattr.split(':', 1)
            min_index = int(scat_list[0])
            max_index = int(scat_list[1])
        
        return min_index, max_index
    
    def create_proto_map(self, min_index, max_index, pkts, rule_map):
        #create proto_map = {0: {'Ethernet': {}, 'IP': {}, 'TCP': {}}}
        proto_map = {}
        for itr in range(min_index, max_index+1):
            proto_map[itr] = {}
            for protocol in rule_map:
                proto_map[itr][protocol] = {}
                if len(rule_map[protocol]) != 0:
                    if pkts[itr].haslayer(protocol):
                        #print(pkts[itr].show())
                        for field in pkts[itr][protocol].fields_desc:
                            proto_map[itr][protocol][field.name] = {}
                            proto_map[itr][protocol][field.name] = getattr(pkts[itr][protocol], field.name)
        
        return proto_map
    
    def process_pkt(self, min_index, max_index, proto_map, rule_map):
        #process pkt to rule set if match then print message
        msg_set = set()
        for itr in range(min_index, max_index+1):
             for proto in rule_map:
                 if len(rule_map[proto]) != 0:
                     for field_map in rule_map[proto]:
                         if field_map['src']!='any' and field_map['dst']!='any' and field_map['src']!=proto_map[itr]['IP']['src'] and field_map['dst']!=proto_map[itr]['IP']['dst']:
                             break;
                         elif field_map['sport']!='any' and field_map['dport']!='any' and field_map['sport']!=proto_map[itr]['TCP']['sport'] and field_map['dport']!=proto_map[itr]['TCP']['dport']:
                             break;
                         msg_set.add(field_map['para']['msg'])
        return msg_set
        
file_list_obj = FileList()
rules = file_list_obj.read_rule("local.rules")
rule_map = file_list_obj.map_of_rules(rules)
file_lst, pkts, p_len = file_list_obj.list_of_file(4, "example.pcap")
scatter_lst = ['0:19']
min_index, max_index = file_list_obj.get_min_max(scatter_lst)
proto_map = file_list_obj.create_proto_map(min_index, max_index, pkts, rule_map)
print(proto_map)
print(file_list_obj.process_pkt(min_index, max_index, proto_map, rule_map))