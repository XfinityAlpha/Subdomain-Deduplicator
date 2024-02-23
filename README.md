# Subdomain-Deduplicator
The SubdomainDeduplicator tool efficiently removes duplicate subdomains from multiple text files.It achieves this by utilizing 
asynchronous I/O operations, which allow for concurrent reading and processing of files.By leveraging asyncio and aiofiles, 
the tool minimizes waiting time for I/O operations, ensuring fast and efficient deduplication of subdomains.Simply provide the 
filenames as command-line arguments, and the tool will produce a final list of unique subdomains in the "unique_subdomains.txt" file.

**Requires:** Python 3.5 or above

## Installation
1 - Download or Copy code **sdd.py**
```bash
chmod +x sdd.py
```
Optional : Create a Symbolic Link for faster access 
## Usage
Help Menu:
```bash
python3 sdd.py -h
```
To search within text (txt) files only:
```bash
python3 sdd.py file1.txt file2.txt fileN.txt
```
