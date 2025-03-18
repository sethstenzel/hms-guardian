import psutil, time
from classes.db import Databases
from classes.application import Application
def get_active_processes():
    """
    Retrieves a list of all active processes.

    Returns:
        list of dict: Each dictionary contains 'pid', 'name', and 'status' of a process.
    """
    processes = []
    for process in psutil.process_iter(attrs=['pid', 'name', 'status']):
        processes.append(process.info)
    
    return processes

def main():
    dbs = Databases()
    applications_data = dbs.read_applications_db()
    for col in applications_data:
        print(f"{applications_data["application_name"]}")

    while False:
        active_processes = get_active_processes()
        time.sleep(0.01)

if __name__ == "__main__":
    main()