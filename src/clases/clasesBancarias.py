class Cliente:
    def __init__(self, nombre, cuenta):
        self.nombre = nombre
        self.cuenta = cuenta

    def listar_saldo_cuenta(self):
        return self.cuenta.obtener_saldo()


class CuentaDeAhorros:

    def __init__(self, saldo):
        self.saldo = saldo

    def obtener_saldo(self):
        return self.saldo

    def transferir_cuenta(self, monto, cliente):
        if self.tiene_fondos_suficientes(monto):
            self.debitar(monto)
            self.acreditar(cliente, monto)
        else:
            print("No tiene saldo suficiente")

    def tiene_fondos_suficientes(self, monto):
        return monto <= self.saldo

    def acreditar(self, cliente, monto):
        cliente.cuenta.saldo += monto

    def debitar(self, monto):
        self.saldo -= monto
