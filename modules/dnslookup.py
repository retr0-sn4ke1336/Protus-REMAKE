import socket

class Module2:
    @staticmethod
    def run(domain):
        try:
            results = socket.getaddrinfo(domain, None)

            print('-=' * 15)
            print("\nResults Found:\n")

            ips = set()  # avoids duplicate IP addresses

            for result in results:
                ip = result[4][0]
                ips.add(ip)

            for ip in ips:
                print('--> ' + ip + ' | Discovered')
            print('-=' * 15)

        except socket.gaierror:
            print("Error: The domain could not be resolved.")
