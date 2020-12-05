from abc import abstractmethod, ABC

class Musician(ABC):

    def __init__(self,name):
        self.name = name

    def play_solo(self):
        pass
        
    def get_instrument(self):
        pass

    def __str__(self):
            
        return 'My name is '+self.name+' and I play '+self.get_instrument()

        
    def __repr__(self):
        
        return self.__class__.__name__+' instance. Name = '+self.name



class Guitarist(Musician):
    '''
    to create new guitarists
    '''
    def play_solo(self):
        return "face melting guitar solo"

    def get_instrument(self):
        return "guitar" 


class Bassist(Musician):
    '''
    to create new bassists
    '''
    def play_solo(self):
        return "bom bom buh bom"
    def get_instrument(self):
        return "bass" 


class Drummer(Musician):
    '''
    to create new drummers
    '''
    def play_solo(self):
        return "rattle boom crash"
    def get_instrument(self):
        return "drums" 



class Band(ABC):
    '''
    to create a band instance
    '''
    all_members=[]

    def __init__(self, name, members):
        self.name = name 
        self.members = members
        Band.all_members.append(self)
        


    def play_solos(self):
        solos = []

        if len(self.members) !=0:
            for i in self.members:
                solos.append(i.play_solo())
            return solos


        else:
            return 'No members yet'


    def __str__(self):
        return (' Band '+ self.name + ' Members: '+self.members).strip()

    def __repr__(self):
        return (' Band '+ self.name + ' Members: '+self.members).strip()
        

    @classmethod
    def to_list(cls):
        return cls.all_members




if __name__ == "__main__":
    new_guitarist = Guitarist("jason")
    new_bassist = Bassist("adi")
    new_drummer = Drummer("katy")

    miami_Band = Band('miami',[])
    print(miami_Band.to_list())


        
        


