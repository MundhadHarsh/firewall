
import pydivert
filterStr=""
firstoption=True 
number=int(input("Enter the Number of packets to be captured: "))

while(True):
        print('\n\nselect the filter options:\n',
              '1.Is outbound?\n',
              '2.Is inbound?\n',
              '3.Is IPv4?\n',
              '4.Is IPv6?\n',
              '5.Is ICMP?\n',
              '6.Is ICMPv6??\n',
              '7.Is TCP?\n',
              '8.Is UDP?\n',
              '9.Any particular local tcp port?\n'
              '10.Is UDP?\n',
              '11.Is UDP?\n',
              '12.Is UDP?\n',
              'c.Capture packets'

              )
        inputStr=input("")
    
#       to exit while loop and start capturing packets
        if(inputStr=='c'):
            break
            
#       to check if outbound  
        elif(inputStr=='1'):
            if(firstoption==False):
                filterStr=filterStr+" and "
            filterStr=filterStr+" outbound "
            print(filterStr)
            firstoption=False

#       to check if inbound  
        elif(inputStr=='2'):
            if(firstoption==False):
                filterStr=filterStr+" and "
            filterStr=filterStr+" inbound "
            print(filterStr)
            firstoption=False
            
#       to check if particular local tcp port   
        elif(inputStr=='9'):
            portStr=""
            portStr==input("enter the port")
            if(firstoption==False):
                filterStr=filterStr+" and "
            filterStr=filterStr+"tcp.DstPort == "+ portStr 
            print(filterStr)
            firstoption=False

            
            
# opening log file to write
loggingFile = open("PacketLog.txt", "w")


for s in range(number):
# capturing packets with filter 
#         w = pydivert.WinDivert(filterStr) 
        w = pydivert.WinDivert(filterStr)
        w.open()  # packets will be captured from now on
        packet = w.recv()  # read a single packet
    
#             for packet in w:
        txt=packet
        print(packet)
        w.send(packet)
        # writing in logging file
        loggingFile.write(str(txt))
        w.close()  # stop capturing packets

loggingFile.close()
