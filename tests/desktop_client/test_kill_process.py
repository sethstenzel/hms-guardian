import subprocess
import os
import pytest
import shutil
import psutil
import time
from src.hms_desktop_client.main import kill_processes_by_name



def check_process_running(process_name):
    """
    Checks if a process with the given name is currently running.

    Args:
        process_name: The name of the process to check.

    Returns:
        True if the process is running, False otherwise.
    """
    for process in psutil.process_iter(['name']):
        if process.info['name'] == process_name:
            return True
    return False


@pytest.fixture
def test_directory(request):
    return os.path.dirname(request.module.__file__)


def test_kill_processes_by_name(test_directory):
    test_process_name = "hms_test_exec.exe"
    assert not check_process_running(test_process_name)
    if not os.path.exists(f"{test_directory}\\hms_test_exec.exe"):
        command = f"pyinstaller --onefile --distpath {test_directory} --workpath {test_directory}\\build -n {test_directory}\\hms_test_exec {test_directory}\\hms_test_exec.py"
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout_string = ""
        for line in p.stdout.readlines():
            stdout_string += line.decode("utf-8")
        retval = p.wait()
        stdout_string += f"\n Return Value {retval}"
        shutil.rmtree(f"{test_directory}\\build")
        os.remove(f"{test_directory}\\hms_test_exec.spec")
        assert "Build complete! The results are available" in stdout_string
    assert os.path.exists(f"{test_directory}\\hms_test_exec.exe")

    command = f"{test_directory}\\hms_test_exec.exe"
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    time.sleep(3)

    assert check_process_running(test_process_name)
    kill_processes_by_name(test_process_name)
    time.sleep(3)
    assert not check_process_running(test_process_name)

