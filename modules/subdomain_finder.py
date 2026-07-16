import socket

WORDLISTS = {
    1: "wordlists/n0kovo_subdomains_tiny.txt",
    2: "wordlists/n0kovo_subdomains_small.txt",
    3: "wordlists/n0kovo_subdomains_medium.txt",
    4: "wordlists/n0kovo_subdomains_large.txt",
    5: "wordlists/n0kovo_subdomains_huge.txt"
}

def scan_subdomains(domain, wordlist_path):
    found = 0

    try:
        with open(wordlist_path, "r") as file:
            subdomains = file.read().splitlines()
    except FileNotFoundError:
        print("Wordlist not found.")
        return

    print("\nStarting search...\n")

    filename = "subdomains_found.txt"
    with open(filename, "w") as output:
        output.write("Subdomains found:\n")

        for sub in subdomains:
            full_domain = f"{sub}.{domain}"
            try:
                socket.gethostbyname(full_domain)
                print(f"[+] {full_domain} | Discovered")
                output.write("-=" * 15 + "\n")
                output.write(full_domain + "\n")
                output.flush()
                found += 1
            except socket.gaierror:
                pass

    print(f"\nTotal found: {found}")

class Module3:
    def run(domain, domain_type):
        scan_subdomains(domain, WORDLISTS[domain_type])
