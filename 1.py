#!/usr/bin/env python3
import os
bash_command = ["cd ~/devops-netology/","git status"]
bash_command1 = ["cd ~/devops-netology/","pwd"]
result_os = os.popen(' && '.join(bash_command)).read()
result_pwd = os.popen(' && '.join(bash_command1)).read()
result_pwd =result_pwd.split('\n')
is_change1 = False
for result in result_os.split('\n'):
    if result.find('новый файл') != -1:
        prepare_result = result.replace('\tновый файл:    ', '')
        print(str(result_pwd[0])+"/"+prepare_result)
    if result.find('изменено') != -1:
        prepare_result = result.replace('\tизменено:      ', '')
        print(str(result_pwd[0])+"/"+prepare_result)