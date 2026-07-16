"""Port scanner module using Scapy for network reconnaissance.

Provides SYN scanning with stealth modes and service identification.
"""

from scapy.all import *
from time import sleep

# Stealth mode delays in seconds (0=aggressive, 5=stealth)
STEALTH_MODES = {
    0: 0,
    1: 0.1,
    2: 0.3,
    3: 0.7,
    4: 1.5,
}

# Common services and their port numbers
SERVICES = {
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    6379: "Redis",
    27017: "MongoDB"
}

class Module1:
    """Port scanner module for Protus."""
    
    name = "Protus Port Scanner"
    description = "A port scanner from the Protus Framework"

    @staticmethod
    def run(host, first_port, last_port, time, show):
        """Execute port scan on target host.
        
        Args:
            host: target host address.
            first_port: first port in scan range.
            last_port: last port in scan range.
            time: stealth mode delay index.
            show: result filter, one of 'open', 'filtered', 'all', 'unknown'.
        """
        open_ports = []


        # Scan each port in the specified range
        for port in range(first_port, last_port + 1):
            # Create a SYN packet for the target port
            packet = IP(dst=host) / TCP(dport=port, flags="S")
            
            # Send the packet and wait for a response
            response = sr1(packet, timeout=1, verbose=0)

            if show == "open":
                if response is None:
                    pass
                elif response.haslayer(TCP):
                    if response[TCP].flags == "SA":
                        service_name = SERVICES.get(port, "Unknown")
                        open_ports.append(("[ + ]", port, "is Open", service_name))

                        # Send RST to close the connection
                        send(IP(dst=host) / TCP(dport=port, flags="R"), verbose=0)

            elif show == "filtered":
                if response is None:
                    open_ports.append(("[ ? ]", port, "is", "Filtered"))

            elif show == "all":
                if response is None:
                    open_ports.append(("[ ? ]", port, "is", "Filtered"))
                elif response.haslayer(TCP):
                    if response[TCP].flags == "SA":
                        service_name = SERVICES.get(port, "Unknown")
                        open_ports.append(("[ + ]", port, "is Open", service_name))

                        # Send RST to close the connection
                        send(IP(dst=host) / TCP(dport=port, flags="R"), verbose=0)
                else:
                    open_ports.append(("[ ? ]", port, "is", "Unknown"))

            elif show == "unknown":
                if response is None:
                    pass
                elif response.haslayer(TCP):
                    if response[TCP].flags == "SA":
                        service_name = SERVICES.get(port, "Unknown")
                        pass

                        # Send RST to close the connection
                        send(IP(dst=host) / TCP(dport=port, flags="R"), verbose=0)
                else:
                    open_ports.append(("[ ? ]", port, "is", "Unknown"))

            # Apply stealth delay
            sleep(STEALTH_MODES.get(time, 0))

        # Display results
        for status, port, status_text, service in open_ports:
                print(f"{status} {port} {status_text} - {service}")
        

        return True
