class movie:
    def __init__(self,Title,Cinema,Hora,ClaveSucursal,NombreSucursal,Pais):
        self.Title = Title
        self.Cinema = Cinema
        self.Hora = Hora
        self.ClaveSurusal = ClaveSucursal
        self.NombreSucursal = NombreSucursal
        self.Pais = Pais
    
    #Sets
    def setTitle(self,TitleParam):
        self.Title = TitleParam
    
    def setCinema(self,CinemaParam):
        self.Cinema = CinemaParam
    
    def setHora(self,HoraParam):
        self.Hora = HoraParam

    def setClaveSurusal(self,ClaveSurusalParam):
        self.ClaveSurusal = ClaveSurusalParam
    
    def setNombreSucursal(self,NombreSucursalParam):
        self.NombreSucursal = NombreSucursalParam
    
    def setPais(self,PaisParam):
        self.Pais = PaisParam

    #Gets
    def getTitle(self):
         return self.Title 
    
    def getCinema(self):
         return self.Cinema 

    def getHora(self):
         return self.Hora 
    
    def getClaveSurusal(self):
         return self.ClaveSurusal 

    def getNombreSucursal(self):
         return self.NombreSucursal 

    def getPais(self):
         return self.Pais  
    
    def __repr__(self):
        return f'Title=${self.Title}, Cinema=${self.Cinema}, Hora=${self.Hora}, ClaveSurusal=${self.ClaveSurusal}, NombreSucursal=${self.NombreSucursal}, Pais=${self.Pais},'

    


