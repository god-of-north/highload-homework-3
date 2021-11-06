import os
from subprocess import Popen

if not os.path.isfile('/opt/airflow/installed.flag'):
    p = Popen(['airflow', 'db', 'init'])
    p.wait()
    p = Popen(['airflow', 'users', 'create', '-r', 'Admin', '-u', 'admin', '-p', 'qwerty', '-f', 'fff', '-l', 'lll', '-e', 'ddd@ddd.dd'])
    p.wait()
    open('/opt/airflow/installed.flag', 'w')
    

d = Popen(['airflow', 'dags', 'list'])
d.wait()

s = Popen(['airflow', 'scheduler'])
w = Popen(['airflow', 'webserver'])

s.wait()
w.wait()
 
