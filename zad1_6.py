from __future__ import annotations
import re
import abc
import datetime
from typing import Union, Optional, Match


class IPv4Address:
    def __init__(self, ip):
        self.ip = ip


class SSHLogEntry(metaclass=abc.ABCMeta):
    def __init__(self, log_line: str) ->None:

        self._raw_text: str = log_line
        self.ip:Union[str,None] 

        pattern_time: str = r'([A-Z])\w+\s+\d+\s\d+:\d+:\d+'
        pattern_host: str = r'([A-Z])\w\w([A-Z])+'
        pattern_PID: str = r'\s[a-z].+?]'


        result_time: Optional[Match[str]] = re.match(pattern_time,log_line)
        result_host: Optional[Match[str]] = re.search(pattern_host,log_line)
        result_PID: Optional[Match[str]] = re.search(pattern_PID,log_line)


        assert result_time is not None
        self.time: str = result_time.group(0)
        assert result_host is not None
        self.host: str = result_host.group(0)
        assert result_PID is not None
        self.pid: str = result_PID.group(0)[1:]



    #zamiana na ciag znakow
    def turnToString(self) -> str:
        return f'Time: {self.time}, Host: {self.host}, PID: {self.pid}, Raw_text: {self._raw_text}'

    #sprawdzamy czy dres ip jest w opisie
    def checkIfIP(self) ->Union[IPv4Address,str]:
        descr: str = f'{self._raw_text}'
        patter_ip: str = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
        ip: Optional[Match[str]] = re.search(patter_ip,descr)
        result:Union[IPv4Address,str]
        if ip !=None:
            assert ip is not None
            result = IPv4Address(ip.group(0))
            self.ip = ip.group(0)
            print('Stworzono obiekt IPv4Address')
        else:
            result = 'None'
        #print(result)
        return result

    @property
    def has_ip(self) -> bool:
        if self.checkIfIP() == 'None':
            return False
        else:
            return True

    @abc.abstractmethod
    def validate(self) -> bool:
        pass
    
    def __repr__(self) -> str:
        return f'Time: {self.time}, Host: {self.host}, PID: {self.pid}, Raw_text: {self._raw_text}'

    def __eq__(self,other: object ) -> bool:
        assert self.time is not None
        #return datetime.datetime.strptime(self.time, "%b %d %H:%M:%S") == datetime.datetime.strptime(other.time, "%b %d %H:%M:%S") and self._raw_text==other._raw_text
        if not isinstance(other, SSHLogEntry):
             return NotImplemented
        return datetime.datetime.strptime(self.time, "%b %d %H:%M:%S") == datetime.datetime.strptime(other.time, "%b %d %H:%M:%S") and self._raw_text==other._raw_text
        

    def __lt__(self,other: SSHLogEntry) -> bool:
        assert self.time is not None
        czas1: str = self.time
        czas2: str = other.time
        if self.time !=None:
            assert self.time is not None
        return datetime.datetime.strptime(czas1, "%b %d %H:%M:%S") < datetime.datetime.strptime(czas2, "%b %d %H:%M:%S")
        
    
    def __gt__(self,other: SSHLogEntry) -> bool:
        assert self.time is not None
        return datetime.datetime.strptime(self.time, "%b %d %H:%M:%S") > datetime.datetime.strptime(other.time, "%b %d %H:%M:%S")
        

class FailedPassword(SSHLogEntry):
    #pattern_user = r'Failed password for (?:invalid user )?(\w+)'
    def __init__(self, log_line: str) -> None:
        super().__init__(log_line)
      
        pattern_user: str = r'Failed password for (?:invalid user )?(\w+)'
        user: Optional[Match[str]] = re.search(pattern_user,log_line)
        if user!=None:
            pattern_ip: str = r'(?<=from\s)\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
            assert user is not None
            self.user:str = user.group(1)
            ip : Optional[Match[str]]= re.search(pattern_ip, log_line)
            if ip:
                self.ip: str = ip.group(0)
                #print(self.ip)
        else:
            print("Podany log nie jest może być obiektem FailedPassword")
    
    def validate(self) -> bool:
        pattern_user: str = r'Failed password for (?:invalid user )?(\w+)'
        user: Optional[Match[str]] = re.search(pattern_user, self._raw_text)
        pattern_ip: str = r'(?<=from\s)\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        ip: Optional[Match[str]] = re.search(pattern_ip, self._raw_text)

        if not user or not ip:
            print("Podany log nie jest może być obiektem FailedPassword")

        if user and self.user == user.group(1) and ip and self.ip == ip.group(0):
            return True
        else:
            return False


    def turnToString(self) -> str:
        try:
            return f"{self.time} {self.host} {self.pid}: Password rejected for user {self.user} from {self.ip}"
        except AttributeError:
            return "Brak potrzebnych parametrow"
            

class AcceptedPassword(SSHLogEntry):
    def __init__(self, log_line: str) -> None:
        super().__init__(log_line)
        
        pattern_user: str = r'Accepted password for (\w+)'
        user: Optional[Match[str]] = re.search(pattern_user,log_line)
        if user:
            pattern_ip: str = r'(?<=from\s)\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
            self.user: str = user.group(1)
            ip: Optional[Match[str]] = re.search(pattern_ip, log_line)
            if ip:
                self.ip: str = ip.group(0)
               
        else:
            print("Podany log nie jest może być obiektem AcceptedPassword")
    
    def validate(self) -> bool:
        pattern_user:str = r'Accepted password for (?:invalid user )?(\w+)'
        user: Optional[Match[str]] = re.search(pattern_user, self._raw_text)
        pattern_ip: str = r'(?<=from\s)\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        ip: Optional[Match[str]] = re.search(pattern_ip, self._raw_text)

        if not user or not ip:
            print("Podany log nie powinien być być obiektem AcceptedPassword")
            
        if user and self.user == user.group(1) and ip and self.ip == ip.group(0):
            return True
        else:
            return False


    def turnToString(self) -> str:
        try:
            return f"{self.time} {self.host} {self.pid}: Password accepted for user {self.user} from {self.ip}"
        except AttributeError:
            return "Brak potrzebnych parametrow"
    
class Error(SSHLogEntry):
    def __init__(self, log_line: str) -> None:
        super().__init__(log_line)
        pattern_error: str = r'error: Received disconnect from (\d+\.\d+\.\d+\.\d+): \d+: (.*) \[preauth\]'
        error: Optional[Match [str]] = re.search(pattern_error,log_line)
        if error:
            self.ip_address: str = error.group(1)
            self.error_message: str = error.group(2)  
        else:
            print("Podany log nie jest może być obiektem Error")
    
    def validate(self) -> bool:
        pattern_error: str = r'error: Received disconnect from (\d+\.\d+\.\d+\.\d+): \d+: (.*) \[preauth\]'
        error: Optional[Match[ str]] = re.search(pattern_error,self._raw_text)

        if not error:
            print("Podany log nie powinien być obiektem Error")
            
        if error and self.ip_address == error.group(1) and self.error_message == error.group(2):
            return True
        else:
            return False


    def turnToString(self) -> str:
        try:
            return f"{self.time} {self.host} {self.pid}: IP address: {self.ip_address}, Error message: {self.error_message}"
        except AttributeError:
            return "Brak potrzebnych parametrow"


class OtherInfo(SSHLogEntry):
    def __init__(self, log_line: str) -> None:
        super().__init__(log_line)
        self.ip = None
        pattern_failed: str = r'Failed password for (?:invalid user )?(\w+)'
        pattern_accepted: str = r'Accepted password for (\w+)'
        pattern_error: str = r'error: Received disconnect from (\d+\.\d+\.\d+\.\d+): \d+: (.*) \[preauth\]'

        failed: Optional[Match [str]] = re.search(pattern_failed,log_line)
        accepted: Optional[Match[str]] = re.search(pattern_accepted,log_line)
        error:Optional[Match[str]] = re.search(pattern_error,log_line)

        if not failed and not accepted and not error:
            pattern_description: str = r':\s.+$'
            description: Optional[Match[str]] = re.search(pattern_description,log_line)
            assert description is not None
            self.description: str = description.group(0)
        else:
            print("Podany log nie może być obiektem OtherInfo")

    def validate(self) -> bool:
        return True


    def turnToString(self) -> str:
        try:
            return f"{self.time} {self.host} {self.pid}: Info: {self.description}"
        except AttributeError:
            return "Log powinien byc obiektem FailedPassword, AcceptedPassword lub Error"



