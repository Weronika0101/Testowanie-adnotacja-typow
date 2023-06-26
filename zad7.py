from zad1_6 import FailedPassword,AcceptedPassword,Error,OtherInfo
import re
from typing import List,Callable,TYPE_CHECKING,Iterator,Union,Optional,Match
from zad1_6 import SSHLogEntry

class SSHLogJournal:

    def __init__(self) -> None:
        self.logs: List[SSHLogEntry] = []

    def __len__(self) -> int:
        return len(self.logs)

    def __iter__(self) -> Iterator[SSHLogEntry]:
        #reveal_type(iter(self.logs))
        return iter(self.logs)

    def __contains__(self, item: SSHLogEntry) -> bool:
        return item in self.logs
    
    def append(self, log_line: str) -> None:
        pattern_failed: str = r'Failed password for (?:invalid user )?(\w+)'
        pattern_accepted: str = r'Accepted password for (\w+)'
        pattern_error: str = r'error: Received disconnect from (\d+\.\d+\.\d+\.\d+): \d+: (.*) \[preauth\]'

        failed: Optional[Match[str]] = re.search(pattern_failed,log_line)
        accepted: Optional[Match[str]] = re.search(pattern_accepted,log_line)
        error: Optional[Match[str]] = re.search(pattern_error,log_line)

        ssh_log_entry: Union[FailedPassword,AcceptedPassword,Error,OtherInfo]
        if failed:
            ssh_log_entry = FailedPassword(log_line)
        elif accepted:
            ssh_log_entry = AcceptedPassword(log_line)
        elif error:
            ssh_log_entry = Error(log_line)
        else:
            ssh_log_entry = OtherInfo(log_line)

        if ssh_log_entry.validate():
            self.logs.append(ssh_log_entry)

    def get_logs_by_criteria(self, criteria:Callable[[SSHLogEntry], bool]) -> List[SSHLogEntry]:
        filtered_logs:List[SSHLogEntry] = []
        for log in self.logs:       
            if criteria(log):                
                filtered_logs.append(log)
        return filtered_logs
    

journal: SSHLogJournal = SSHLogJournal()
journal.__iter__
journal.append('Dec 21 23:48:15 LabSZ sshd[21169]: Invalid user test2 from 122.224.69.34')
journal.append('Dec 21 23:45:35 LabSZ sshd[21165]: Failed password for root from 114.112.48.155 port 46140 ssh2')
#journal.append('Dec 21 23:42:08 LabSZ sshd[21010]: Accepted password for hxu from 111.222.107.90 port 43009 ssh2')
#print(journal.logs)

print(journal.get_logs_by_criteria(lambda x: True if (x.ip=='114.112.48.155') else False))
#print(journal.get_logs_by_criteria(lambda x: True if (x.ip=='random ip') else False))
