class Motor:
    def __init__(self,rpm=1650,potencia=0.33):
        self._rpm_motor = rpm
        self._potencia = potencia

    @property
    def rpm_motor(self):
        return self._rpm_motor
    
    @property
    def potencia(self):
        return self._potencia
    
    def calcula_torque(self):
        return 716.2*self.potencia/self.rpm_motor #[kgf.m]

class Redutor(Motor):
    def __init__(self,reducao):
        super(). __init__(rpm=1650,potencia=0.33)
        self.reducao = reducao
        self.rpm_entrada = self.rpm_motor #mesmo do motor
        self.rpm_saida = self.rpm_entrada/self.reducao

    def calcula_torque(self):
        return super().calcula_torque()* self.reducao #[kgf.m]

class Roda(Redutor):
    def __init__(self,diametro,reducao):
        super(). __init__(reducao)
        self.diametro = diametro #metros
        self.reducao = reducao

    def forca_puxada(self):
        return self.calcula_torque()*2/self.diametro #[kgf.m]

    def velocidade_tangencial(self):
        return self.diametro * 3.14159 * self.rpm_saida



        
