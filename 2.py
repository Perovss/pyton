#!/usr/bin/env python3
import os
import sys
if len(sys.argv)==1:
    print(len(sys.argv))
    local_dir=input("Введите директорию:")
else:
    local_dir = sys.argv[1]
print(local_dir)
cd_dir="cd "+local_dir
bash_command = [cd_dir,"git status"]
bash_command1 = [cd_dir,"pwd"]
result_os = os.popen(' && '.join(bash_command)).read()
result_pwd = os.popen(' && '.join(bash_command1)).read()
result_pwd =result_pwd.split('\n')
is_change= False
for result in result_os.split('\n'):
    if result.find('новый файл') != -1:
        prepare_result = result.replace('\tновый файл:    ', '')
        print(result_pwd[0]+prepare_result)
    if result.find('изменено') != -1:
        prepare_result = result.replace('\tизменено:      ', '')
        print(result_pwd[0]+prepare_result)
