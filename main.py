from zad1_6 import FailedPassword,AcceptedPassword,Error,OtherInfo
from zad1_6_notabstract import SSHLogEntry

log: SSHLogEntry = SSHLogEntry('Dec 22 04:50:18 LabSZ sshd[22642]: Failed password for invalid user default from 460.248.21.32 port 37906 ssh2')
logg: SSHLogEntry = SSHLogEntry('Dec 21 23:42:08 LabSZ sshd[21010]: Accepted password for hxu from 111.222.107.90 port 43009 ssh2')
print(log < logg)
print(log > logg)
print(log==logg)
print(log==log)

log1: FailedPassword= FailedPassword('Dec 22 04:50:18 LabSZ sshd[22642]: Failed password for invalid user default from 46.148.21.32 port 37906 ssh2')
print(log1.turnToString())
print(log1.checkIfIP())
print(log1.ip)
print(log1.user)
#print(log1.validate())
#log1.user='other user'
#print(log1.user)
#print(log1.validate())
#print(log1.has_ip)
#print(log1.time)

log2: AcceptedPassword= AcceptedPassword('Dec 21 23:42:08 LabSZ sshd[21010]: Accepted password for hxu from 111.222.107.90 port 43009 ssh2')
#print(log2.turnToString())
#print(log2.checkIfIP())
#print(log2.validate())
#print(log2.has_ip)

log3: Error= Error('Dec 22 04:50:19 LabSZ sshd[22647]: error: Received disconnect from 195.154.37.122: 3: com.jcraft.jsch.JSchException: Auth fail [preauth]')
#print(log3.turnToString())
#print(log3.checkIfIP())
#print(log3.validate())
#print(log3.has_ip)

log4: OtherInfo= OtherInfo('Dec 21 23:42:08 LabSZ sshd[21010]: pam_unix(sshd:session): session opened for user hxu by (uid=0)')
print(log4.turnToString())
print(log4.checkIfIP())
print(log4.time)
#print(log4.validate())
#log4.host='other time'
#print(log4.time)
#print(log4.validate())
#print(log4.has_ip)

#print(log1)
#print(log2)
#print(log3)
print(log2 < log1)
print(log2 > log1)
print(log1==log3)
print(log1 == log1)


