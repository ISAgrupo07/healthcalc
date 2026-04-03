from behave import given, when, then
from healthcalc.health_calc_impl import HealthCalcImpl

@given(u'la calculadora clínica está iniciada')
def step_impl(context):
    context.calculadora = HealthCalcImpl()
    # valores por defecto 
    context.frecResp = 15
    context.oxSat = 98
    context.oxSup = False
    context.preArtSis = 120
    context.frecCard = 75
    context.consciente = "alerta"
    context.temp = 37.0

@given(u'que el paciente tiene una frecuencia respiratoria de {respiracion:d} rpm')
def step_respiracion(context, respiracion):
    context.frecResp = respiracion

@given(u'una saturación de oxígeno del {saturacion:d} %')
def step_saturacion(context, saturacion):
    context.oxSat = saturacion

@given(u'el uso de soporte de oxígeno es {soporte}')
def step_soporte(context, soporte):
    context.oxSup = (soporte.lower() == 'true')

@given(u'una presión arterial sistólica de {presion:d} mmHg')
def step_presion(context, presion):
    context.preArtSis = presion

@given(u'una frecuencia cardíaca de {pulso:d} lpm')
def step_pulso(context, pulso):
    context.frecCard = pulso

@given(u'el nivel de consciencia es "{consciencia}"')
def step_consciencia(context, consciencia):
    context.consciente = consciencia

@given(u'la temperatura corporal es de {temp:f} ºC')
def step_temp(context, temp):
    context.temp = temp

@given(u'el valor de entrada de la métrica {metrica} es {valor:g}')
def step_metrics_error(context, metrica, valor):
    metrica = metrica.lower()
    if "respiratoria" in metrica:
        context.frecResp = valor
    elif "saturación" in metrica:
        context.oxSat = valor
    elif "sistólica" in metrica:
        context.preArtSis = valor
    elif "cardíaca" in metrica:
        context.frecCard = valor
    elif "temperatura" in metrica:
        context.temp = valor

@when(u'calculo la puntuación NEWS2')
def step_calculo(context):
    try:
        context.resultado = context.calculadora.news2(
            frecResp=context.frecResp,
            oxSat=context.oxSat,
            oxSup=context.oxSup,
            preArtSis=context.preArtSis,
            frecCard=context.frecCard,
            consciente=context.consciente,
            temp=context.temp
        )
        context.error_lanzado = False
    except Exception as e:
        context.error_lanzado = True
        context.excepcion = e

@then(u'el resultado debe ser {valor:d}')
def step_verificar(context, valor):
    assert not context.error_lanzado, f"Se lanzó una excepción inesperada: {context.excepcion}"
    assert context.resultado == valor, f"Esperaba {valor} pero obtuve {context.resultado}"

@then(u'el sistema debe lanzar una excepción')
def step_exception(context):
    assert context.error_lanzado, "Se esperaba una InvalidHealthDataException pero el código no lanzó nada."