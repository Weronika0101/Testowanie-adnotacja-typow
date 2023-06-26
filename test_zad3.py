import pytest
from zad1_6 import SSHLogEntry, AcceptedPassword, FailedPassword, Error, OtherInfo
from zad7 import SSHLogJournal

@pytest.mark.parametrize("log_entry_type,log_entry_str",
    [(AcceptedPassword,"Dec 21 23:42:08 LabSZ sshd[21010]: Accepted password for hxu from 111.222.107.90 port 43009 ssh2"),
    (FailedPassword,"Dec 22 04:50:18 LabSZ sshd[22642]: Failed password for invalid user default from 460.248.21.32 port 37906 ssh2"),
    (Error,"Dec 22 04:50:19 LabSZ sshd[22647]: error: Received disconnect from 195.154.37.122: 3: com.jcraft.jsch.JSchException: Auth fail [preauth]"),
    (OtherInfo,"Dec 21 23:42:08 LabSZ sshd[21010]: pam_unix(sshd:session): session opened for user hxu by (uid=0)")
    ])
def test_append_type(log_entry_type,log_entry_str):
    journal = SSHLogJournal()
    journal.append(log_entry_str)
    #sprawdzanie czy ostatni dodany element journala jest oczekiwanego typu
    assert isinstance(journal.logs[-1], log_entry_type)
    