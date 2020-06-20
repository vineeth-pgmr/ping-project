# import built-in os library
# https://docs.python.org/3/library/os.html

import os

from datetime import datetime
from colorama import Fore

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

# Open file for saving ping results
results_file = open("results.txt", "w+")
    
ip_list = ["8.8.8.8"]

for ip in ip_list:
    response = os.popen(f"ping {ip} -n 1").read()
    if "Received = 1" and "Approximate" in response:
        print(Fore.GREEN + current_time +f"UP {ip} Ping Successful")
        results_file.write(current_time+ " "+f"UP {ip} Ping Successful" + "\n")
    else:
        print(Fore.RED + current_time +f"Down {ip} Ping Unsuccessful")
        results_file.write(current_time + " " +f"Down {ip} Ping Unsuccessful" + "\n")
# Close file when script completes
results_file.close()