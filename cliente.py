from cuentas import *
from tipo_clientes import *
from tarjetas import Tarjeta

class Cliente():
    def __init__(self, name, apellido, dni, idCliente, ingresos):
        self._tipo_cuenta = Tipo_Classic()
        self._cuentas = [CajaAhorroPeso(name + " " + apellido, 0)]
        self._name = name
        self._apellido = apellido
        self._dni = dni
        self._idCliente = idCliente 
        self._ingresos = ingresos
        self._tarjetas = []

    #Getters
    def getNombre(self):
        return self._name

    def getApellido(self):
        return self._apellido

    def getDni(self):
        return self._dni

    def getIdCliente(self):
        return self._idCliente

    def getIngresos(self):
        return self._ingresos

    def getTipoCuenta(self):
        return self._tipo_cuenta.tipo

    def getTarjetas(self):
        return self._tarjetas


    #Setters
    def editName(self, a): 
        if( a.__len__() < 3): 
            print("El nombre debe tener al menos 3 caracteres")
            return
        self._name = a

    def editApellido(self, a): 
        if( a.__len__() < 3): 
            print("El apelido debe tener al menos 3 caracteres")
            return
        self._apellido = a

    def editDni(self, d): 
        #Extender para validar que sean numeros
        if( d.__len__() != 8): 
            print("El DNI debe tener 8 caracteres")
            return
        self._dni = d

    def editIdCliente(self, i): 
        #Validacion cualquiera
        #Hay que validar que los id's no se repitan, no se si corresponde igual hacer eso
        if( i < 1): 
            print("El Id del Cliente no debe ser menor que 1")
            return
        self._idCliente = i

    def editIngresos(self, i): 
        if( i < 50): 
            print("Debe tener ingresos superiores a $50 pesos mensuales")
            return
        self._ingresos = i


    def upgradear(self):
        if self._tipo_cuenta_str == "classic":
            self.tipo_cuenta = Tipo_Gold()
            self._tipo_cuenta_str = "gold"

    def __str__(self) -> str:
        return self._tipo_cuenta_str

    def crear_cuenta(self):
        if len(self._cuentas) < self._tipo_cuenta.caja_de_ahorro:
            print("Cuenta Creada")
            self._cuentas.append(Caja_de_Ahorro())
        else:
            print("No capo, no podes crear mas")

    def retirar_dinero(self, monto):
        if monto <= self._tipo_cuenta.retiros()["monto_limite_retiro"]:
            print(self._cuentas[0].retirar(monto))
        else:
            print("No capo tu limite es:", self._tipo_cuenta.retiros()["monto_limite_retiro"])

    def consultar_saldo(self):
        print(self._cuentas[0].consultar_saldo())

    def depositar(self, monto):
        print(self._cuentas[0].depositar(monto))

  #REVISAR
    def alta_caja_de_ahorro_pesos(self):
        self._cuentas.append()


c1 = Cliente("Aldo", "Andres", "44614368", 1, 30000)
print(c1.getNombre() + " " + c1.getApellido())
c1.consultar_saldo()
c1.retirar_dinero(15000)
c1.depositar(20000)
c1.retirar_dinero(10000)