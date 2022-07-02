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
        self.saldo -= monto
        cliente.cuenta.saldo += monto
