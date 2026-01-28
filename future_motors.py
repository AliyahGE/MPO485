class Vehicle:
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