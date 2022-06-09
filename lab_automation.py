import os

cmd = 'ansible-playbook nested2.yml -e "ansible_sudo_pass=12345"'
os.system(cmd)
