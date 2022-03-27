

from abc import ABC, abstractmethod

class listeningService(ABC):

    @abstractmethod
    def receiveData(self):
        pass

class transformlisteningService(listeningService):
    
    @abstractmethod
    def receiveData(self):
        pass






