import os

#cmd = 'cd Automation-with-Ansible/'
os.chdir('Automation-with-Ansible/')

#cmd = 'ansible-playbook nested2.yml -e "ansible_sudo_pass=12345"'
cmd = 'python3 lab_automation.py'
os.system(cmd)
