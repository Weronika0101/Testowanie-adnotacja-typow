import re
from zad7 import SSHLogJournal

class SSHUser:
    def __init__(self, username, last_login):
        self.username = username
        self.last_login = last_login

    def validate(self):
        pattern = r'^[a-z_][a-z0-9_-]{0,31}$'
        if re.match(pattern, self.username):
            return True
        else:
            return False
        

log_journal = SSHLogJournal()
log_journal.append('Dec 21 23:43:52 LabSZ sshd[21111]: Failed password for root from 114.112.48.155 port 56398 ssh2')
log_journal.append('Dec 21 23:43:52 LabSZ sshd[21111]: Received disconnect from 114.112.48.155: 11: Bye Bye [preauth]')
log_journal.append('Dec 21 23:43:53 LabSZ sshd[21113]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=114.112.48.155  user=root')
log_journal.append('Dec 21 23:43:55 LabSZ sshd[21113]: Failed password for root from 114.112.48.155 port 58287 ssh2')
log_journal.append('Dec 21 23:43:56 LabSZ sshd[21113]: Received disconnect from 114.112.48.155: 11: Bye Bye [preauth]')

user1 = SSHUser("admin",'Dec 21 23:43:52')
user2 = SSHUser("uzytkownik",'Dec 22 23:53:52')

final_lst = []
for log in log_journal:
    final_lst.append(log)
#print(final_lst)

final_lst.append(user1)
final_lst.append(user2)
print(final_lst)

for log in final_lst:
    print(log.validate())
    print("Zwalidowano")


