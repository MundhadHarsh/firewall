![image](https://github.com/MundhadHarsh/firewall/assets/97428445/47636234-ac3a-4cf9-a8dd-1fa5adacba33)# Windows Host-Based Firewall

A Firewall that goes beyond traditional firewall functionalities and integrates additional features such as packet filtering, IP blocking and Port Blocking. 
Provides better visibility and control over network traffic.
It has the bility to provide comprehensive protection for all traffic entering and leaving an organization's network![image](https://github.com/MundhadHarsh/firewall/assets/97428445/32c699f4-7ce6-42e0-a52a-0d663db2e9c6)


## Technology
The main technology used for the firewall is WinDivert

Windows Packet Divert (WinDivert) is a user-mode packet capture-and-divert package for Windows 10, Windows 11, and Windows Server.

WinDivert allows user-mode applications to capture/modify/drop network packets sent to/from the Windows network stack. In summary, WinDivert can:

capture network packets
filter/drop network packets
sniff network packets
(re)inject network packets
modify network packets
WinDivert can be used to implement user-mode packet filters, packet sniffers, firewalls, NAT, VPNs, tunneling applications, etc.

## Working of Windivert 
1. A new packet enters the network stack and is intercepted by WinDivert.sys
2. If the packet matches the PROGRAM-defined filter, it is diverted. The program can then read the packet using a call to WinDivertRecv().
3. If the packet does not match the filter, the packet continues as normal.
4. PROGRAM either drops, modifies, or re-injects the packet. the program can re-inject the (modified) using a call to WinDivertSend().

![image](https://github.com/MundhadHarsh/firewall/assets/97428445/93e24466-546c-4516-8425-f41263600155)

## Developed by Harsh Mundhada

gmail [@mailId](harshmundhada@gmail.com)
Linkedin[@linkedin](https://www.linkedin.com/in/harsh-mundhada-473864229)
