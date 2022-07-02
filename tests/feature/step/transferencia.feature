# Created by JairG at 2/7/2022
# language:es

  Característica: Transferencia bancaria
    Como titular de una cuenta bancaria, deseo realizar una transferencia local segura
    para aumentar la confianza del banco
  Escenario:  Transferencia entre cuentas del mismo banco
    Dado que Miguel tiene una cuenta de ahorros con $100.00 dólares de saldo
    Y que Gabriel tiene otra cuenta de ahorros con $10.00 dólares de saldo
    Cuando Miguel transfiere un monto de $50.00 dólares a Gabriel
    Entonces Miguel tendrá $50.00 dólares de saldo
    Y Gabriel tendrá $60.00 dólares de saldo