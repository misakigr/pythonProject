import subprocess
import platform
try:
    def ping(host):
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        command = ['ping', param, '2', host]
        return subprocess.call(command)

    host = 'google.com'
    print(ping(host))
    os.remove(t)
except:
    pass