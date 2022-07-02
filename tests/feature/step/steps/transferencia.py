from behave import *

from src.clases.clasesBancarias import Cliente, CuentaDeAhorros

use_step_matcher("re")


@step("que Miguel tiene una cuenta de ahorros con \$100\.00 dólares de saldo")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # Aquí realizamos el análisis.
    # Aquí creamos la petición de métodos que debe tener el sistema (pregunta a mirar video)
    context.clienteOrigen = Cliente("Miguel", CuentaDeAhorros(100))
    # assert context.cliente.listar_saldos_de_cuentas()
    assert (context.clienteOrigen.listar_saldo_cuenta() == 100)


@step("que Gabriel tiene otra cuenta de ahorros con \$10\.00 dólares de saldo")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """

    context.clienteDestino = Cliente("Gabriel", CuentaDeAhorros(10))
    assert context.clienteDestino.listar_saldo_cuenta() == 10



@step("Miguel transfiere un monto de \$50\.00 dólares a Gabriel")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """

    context.clienteOrigen.cuenta.transferir_cuenta(50, context.clienteDestino)


@step("Miguel tendrá \$50\.00 dólares de saldo")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """

    assert context.clienteOrigen.listar_saldo_cuenta() == 50


@step("Gabriel tendrá \$60\.00 dólares de saldo")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.clienteDestino.listar_saldo_cuenta() == 60


@step("que Miguel tiene una cuenta de ahorros con \$10\.00 dólares de saldo")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.clienteOrigen = Cliente("Miguel", CuentaDeAhorros(10))
    # assert context.cliente.listar_saldos_de_cuentas()
    assert (context.clienteOrigen.listar_saldo_cuenta() == 10)

# tendríamos que hacer muchos casos de estos, por lo que no es eficiente
@step('que Miguel tiene una cuenta de ahorros con \$"10\.00" dólares de saldo')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Dado que Miguel tiene una cuenta de ahorros con $"10.00" dólares de saldo')