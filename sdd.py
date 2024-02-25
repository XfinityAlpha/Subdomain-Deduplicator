import sys
import os
import asyncio
import aiofiles

if len(sys.argv) == 1 or sys.argv[1] == '-h':
    print("""
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
   _____       __        __                      _                   ____           __            ___            __            
  / ___/__  __/ /_  ____/ /___  ____ ___  ____ _(_)___              / __ \___  ____/ /_  ______  / (_)________ _/ /_____  _____
  \__ \/ / / / __ \/ __  / __ \/ __ `__ \/ __ `/ / __ \   ______   / / / / _ \/ __  / / / / __ \/ / / ___/ __ `/ __/ __ \/ ___/
 ___/ / /_/ / /_/ / /_/ / /_/ / / / / / / /_/ / / / / /  /_____/  / /_/ /  __/ /_/ / /_/ / /_/ / / / /__/ /_/ / /_/ /_/ / /    
/____/\__,_/_.___/\__,_/\____/_/ /_/ /_/\__,_/_/_/ /_/           /_____/\___/\__,_/\__,_/ .___/_/_/\___/\__,_/\__/\____/_/     
                                                                                       /_/                                     

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

SubdomainDeduplicator : A tool to efficiently remove duplicate subdomains from multiple files.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Usage - 1 : python3 sdd.py file1.txt file2.txt fileN.txt /path/to/directory
Usage - 2 : python3 sdd.py /path/to/directory # Directory Containing Files

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX         
""")
    exit()

# Use a set to store unique subdomains
unique_subdomains = set()

async def process_file(filename):
    async with aiofiles.open(filename, mode='r') as f:
        print("[+] Processing", filename)  # Verbose output: Print filename being processed
        async for subdomain in f:
            unique_subdomains.add(subdomain.strip())

async def main():
    for arg in sys.argv[1:]:
        if os.path.isdir(arg):
            # If argument is a directory, process all .txt files within it
            for root, _, files in os.walk(arg):
                for file in files:
                    if file.endswith('.txt'):
                        await process_file(os.path.join(root, file))
        else:
            await process_file(arg)

asyncio.run(main())

print("-------------------------------------------")
print("[-] DONE writing to unique_subdomains.txt")
with open("unique_subdomains.txt", 'w+') as fh:
    fh.write('\n'.join(unique_subdomains))  # Write unique subdomains to the file
