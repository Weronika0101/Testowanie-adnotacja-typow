from zad1_6_notabstract import SSHLogEntry,InvalidIPv4Address
import pytest

@pytest.mark.parametrize("log_entry_str, expected_output", [
    ("Dec 10 06:55:48 LabSZ sshd[24200]: Failed password for invalid user webmaster from 234.98.88.213 port 38926 ssh2","234.98.88.213"),
    ("Dec 21 23:41:09 LabSZ sshd[21008]: Received disconnect from 115.71.16.143: 11: Bye Bye [preauth]","115.71.16.143"),
    ("Dec 21 23:43:05 LabSZ sshd[21110]: Did not receive identification string from 5.188.10.182","5.188.10.182"),
    ("Dec 11 00:12:09 LabSZ sshd[20161]: Invalid user packer from 58.42.244.194","58.42.244.194")
])
def test_ipv4_extraction_correct_ip(log_entry_str, expected_output):
    # tworzenie obiektu klasy SSHLogEntry
    log = SSHLogEntry(log_entry_str)
    ip_object = log.checkIfIP()

    # porównanie wyniku z oczekiwanym rezultatem
    assert ip_object.ip == expected_output


@pytest.mark.parametrize("log_entry_str", [
    ("Dec 10 06:55:48 LabSZ sshd[24200]: Failed password for invalid user webmaster from 284.98.88.213 port 38926 ssh2"),
    ("Dec 21 23:41:09 LabSZ sshd[21008]: Received disconnect from 666.345.16.143: 11: Bye Bye [preauth]"),
    ("Dec 10 06:55:48 LabSZ sshd[24200]: Failed password for invalid user webmaster from 666.777.88.213 port 38926 ssh2"),
    ("Dec 11 00:12:09 LabSZ sshd[20161]: Invalid user packer from 58.42.244.500")
])
def test_ipv4_extraction_incorrect_ip(log_entry_str):
    # tworzenie obiektu klasy SSHLogEntry
    log = SSHLogEntry(log_entry_str)

    #sprawdzanie czy funkcja rzuca wyjątek InvalidIpv4Address (Raised when ip address is incorrect)
    with pytest.raises(InvalidIPv4Address):
        log.checkIfIP()



@pytest.mark.parametrize("log_entry_str", [
    ("Dec 21 23:42:08 LabSZ sshd[21010]: pam_unix(sshd:session): session opened for user hxu by (uid=0)"),
    ("Dec 11 00:11:46 LabSZ sshd[20145]: input_userauth_request: invalid user packer [preauth]"),
    ("Dec 11 00:11:51 LabSZ sshd[20147]: pam_unix(sshd:auth): check pass; user unknown"),
    ("Dec 11 00:11:58 LabSZ sshd[20153]: input_userauth_request: invalid user packer [preauth]")
])
def test_ipv4_extraction_none(log_entry_str):
    # tworzenie obiektu klasy SSHLogEntry
    log = SSHLogEntry(log_entry_str)

    # porównanie wyniku z oczekiwanym rezultatem
    assert log.checkIfIP()== 'None'
