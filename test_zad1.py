from datetime import datetime
from zad1_6_notabstract import SSHLogEntry
import pytest

# Test weryfikujący poprawność ekstrakcji czasu tworzonego obiektu klasy SSHLogEntry

@pytest.mark.parametrize("log_entry_str, expected_time", [
    ("Dec 10 06:55:48 LabSZ sshd[24200]: Failed password for invalid user webmaster from 666.777.88.213 port 38926 ssh2","Dec 10 06:55:48"),
    ("Dec 21 23:41:09 LabSZ sshd[21008]: Received disconnect from 115.71.16.143: 11: Bye Bye [preauth]","Dec 21 23:41:09"),
    ("Dec 21 23:43:05 LabSZ sshd[21110]: Did not receive identification string from 5.188.10.182","Dec 21 23:43:05"),
    ("Dec 11 00:12:09 LabSZ sshd[20161]: Invalid user packer from 58.42.244.194","Dec 11 00:12:09")
])
def test_time_extraction(log_entry_str, expected_time):
    # tworzenie obiektu klasy SSHLogEntry
    log_entry = SSHLogEntry(log_entry_str)
    
    assert log_entry.time == expected_time

