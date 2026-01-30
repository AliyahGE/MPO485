from abc import ABC, abstractmethod

class Vehicle(ABC):

    def __init__(self, matricula, model, kms_inicials):
        self.matricula = matricula
        self._model = model 
        self.__kms = kms_inicials 

    def llegir_kms(self):
        return self.__kms

    def actualitzar_kms(self, nous_kms):
        if self.__kms > nous_kms:
            return False 
        else:
            self.__kms = nous_kms
            return True

    @abstractmethod
    def calcular_preu(self,dies):
        pass

class Esportiu(Vehicle):
    def calcular_preu(self,dies):
        return dies * 100

class Camio(Vehicle):
    def __init__(self,matricula, model, kms_inicials,tones):
        super().__init__(matricula, model, kms_inicials)
        self.tones = tones

    def calcular_preu(self,dies):
        return (dies * 50) + (self.tones * 20)

class EmpresaRent():
    def __init__(self):
        self.vehicles = []

    def afegir_vehicle(self,vehicle):
        self.vehicles.append(vehicle)

    def informe_guanys(self,dies):
        guanys_totals = 0
        for vehicle in self.vehicles:
            preu = vehicle.calcular_preu(dies)
            guanys_totals = guanys_totals + preu
        return guanys_totals
