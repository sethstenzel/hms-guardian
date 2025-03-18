import psutil, time
from src.hms_desktop_client.classes.db import Databases
from src.hms_desktop_client.classes.application import Application

def get_active_processes():
    """
    Retrieves a list of all active processes.

    Returns:
        list of dict: Each dictionary contains 'pid', 'name', and 'status' of a process.
    """
    processes = []
    for process in psutil.process_iter(attrs=['pid', 'name', 'status', 'username']):
        processes.append(process.info)
    
    return processes

def kill_processes_by_name(process_name):
    for proc in psutil.process_iter():
        if str(proc.name) and process_name in str(proc.name):
            p = psutil.Process(proc.pid)
            print(p)
            proc.kill()

def kill_process_by_pid():
   pass

def main():
    dbs = Databases()
    applications_data = dbs.read_applications_db()
    applications = []
    for _, row in applications_data.iterrows():
        row_dict = row.to_dict()
        new_application = Application(**row_dict)
        applications.append(new_application)

    while True:
        active_processes = get_active_processes()
        for process in active_processes:
            for application in applications:
                if application.name in str(process):
                    print(process)
                    print(application.name)
            
        time.sleep(1)

if __name__ == "__main__":
    main()