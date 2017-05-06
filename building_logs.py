import time
import random

#Build log_message components
#build an IP address
ip = ""
def build_ip():
    ip = str(random.randrange(1,255)) + "." + str(random.randrange(1,255)) + "." + str(random.randrange(1, 255)) + "." + str(random.randrange(1,255))
    return ip

#build src_port
def build_dst_port():
    port_n = str(random.randrange(1,1024))
    return port_n

#build src port
def build_src_port():
    port_n = str(random.randrange(1025,65535))
    return port_n


#build proto
def build_proto():
    proto = ["TCP", "UDP"]
    p = proto[random.randrange(0,2)]
    return p

#build action
def build_action():
    act = ["BLOCKED", "ALLOWED"]
    a = act[random.randrange(0,2)]
    return a

#full message build
def build_full_msg():
    src_ip = build_ip() + " "
    src_port = build_src_port() + " "
    dest_ip = build_ip() + " "
    dest_port = build_dst_port() + " "
    protocol = build_proto() + " "
    action = build_action() + " "
    evnt_time = str(time.asctime()) + " "
    seconds = random.randrange(1, 5)
    time.sleep(seconds)
    log_message = evnt_time + "TRAFFIC: " + "src_ip=" + src_ip + "src_port=" + src_port + "dest_ip=" + dest_ip + "dest_port=" + dest_port + "protocol=" + protocol + "acton=" + action
    return log_message

#main code run
while True:
    log_message = build_full_msg()
    print(log_message)
