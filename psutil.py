# We are going to use the psutil command to format a script to check these items.  cpu times, cpu percentatge, disk partion's, users and net connections.  
# You may have to do some extra modification to make the ouput be more readable.


import psutil

import psutil
import datetime

def format_time(seconds):
    return str(datetime.timedelta(seconds=seconds))

def check_system():
    print("--- CPU Info ---")
    print(f"Time used by programs: {format_time(psutil.cpu_times().user)}")
    print(f"Time used by system: {format_time(psutil.cpu_times().system)}")
    print(f"Time doing nothing: {format_time(psutil.cpu_times().idle)}")
    print(f"CPU is working at: {psutil.cpu_percent(interval=1)}%\n")
    
    print("--- Storage Info ---")
    for partition in psutil.disk_partitions():
        print(f"Drive: {partition.device}")
        print(f"Location: {partition.mountpoint}")
        print(f"Type: {partition.fstype}\n")
    
    print("--- Who is using the computer? ---")
    for user in psutil.users():
        print(f"User: {user.name}, From: {user.host}, Logged in at: {datetime.datetime.fromtimestamp(user.started)}")
    print()
    
    print("--- Internet Connections ---")
    for conn in psutil.net_connections(kind='inet')[:5]:  # Show only 5
        print(f"Type: {conn.type.name}, From: {conn.laddr}, To: {conn.raddr if conn.raddr else 'N/A'}, Status: {conn.status}")
    
if __name__ == "__main__":
    check_system()
