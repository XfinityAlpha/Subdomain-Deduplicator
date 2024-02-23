XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
   _____       __        __                      _                   ____           __            ___            __            
  / ___/__  __/ /_  ____/ /___  ____ ___  ____ _(_)___              / __ \___  ____/ /_  ______  / (_)________ _/ /_____  _____
  \__ \/ / / / __ \/ __  / __ \/ __ `__ \/ __ `/ / __ \   ______   / / / / _ \/ __  / / / / __ \/ / / ___/ __ `/ __/ __ \/ ___/
 ___/ / /_/ / /_/ / /_/ / /_/ / / / / / / /_/ / / / / /  /_____/  / /_/ /  __/ /_/ / /_/ / /_/ / / / /__/ /_/ / /_/ /_/ / /    
/____/\__,_/_.___/\__,_/\____/_/ /_/ /_/\__,_/_/_/ /_/           /_____/\___/\__,_/\__,_/ .___/_/_/\___/\__,_/\__/\____/_/     
                                                                                       /_/                                     

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

The SubdomainDeduplicator tool efficiently removes duplicate subdomains from multiple text files.It achieves this by utilizing 
asynchronous I/O operations, which allow for concurrent reading and processing of files.By leveraging asyncio and aiofiles, 
the tool minimizes waiting time for I/O operations, ensuring fast and efficient deduplication of subdomains.Simply provide the 
filenames as command-line arguments, and the tool will produce a final list of unique subdomains in the "unique_subdomains.txt" file.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Usage : python3 sdd.py file1.txt file2.txt fileN.txt
