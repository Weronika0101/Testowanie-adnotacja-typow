from __future__ import annotations
import re
import abc
import datetime
from typing import Union, Optional, Match

class InvalidIPv4Address(Exception):
    "Raised when ip address is incorrect"
    pass

class IPv4Address:
    def __init__(self, ip):
        self.ip = ip


class SSHLogEntry():
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
        patter_ip: str = r'\b(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})\b'
        ip: Optional[Match[str]] = re.search(patter_ip,descr)
        result:Union[IPv4Address,str]
        result = 'None'

        if ip !=None:
            
                assert ip is not None
                if not 0<=int(ip.group(1))<256 or not 0<=int(ip.group(2))<256 or not 0<=int(ip.group(3))<256 or not 0<=int(ip.group(4))<256:
                    raise InvalidIPv4Address
                else:
                    result = IPv4Address(ip.group(0))
                    self.ip = ip.group(0)
                    print('Stworzono obiekt IPv4Address')
                        
        return result

    @property
    def has_ip(self) -> bool:
        if self.checkIfIP() == 'None':
            return False
        else:
            return True

    
    def __repr__(self) -> str:
        return f'Time: {self.time}, Host: {self.host}, PID: {self.pid}, Raw_text: {self._raw_text}'

    def __eq__(self,other: object ) -> bool:
        assert self.time is not None 
        if not isinstance(other, SSHLogEntry):
             return NotImplemented
        return datetime.datetime.strptime(self.time, "%b %d %H:%M:%S") == datetime.datetime.strptime(other.time, "%b %d %H:%M:%S") and self._raw_text==other._raw_text
        

    def __lt__(self,other: SSHLogEntry) -> bool:
        assert self.time is not None
        return datetime.datetime.strptime(self.time, "%b %d %H:%M:%S") < datetime.datetime.strptime(other.time, "%b %d %H:%M:%S")
        
    
    def __gt__(self,other: SSHLogEntry) -> bool:
        assert self.time is not None
        return datetime.datetime.strptime(self.time, "%b %d %H:%M:%S") > datetime.datetime.strptime(other.time, "%b %d %H:%M:%S")
        



