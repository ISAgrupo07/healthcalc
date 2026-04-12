from behave import given, when, then
from healthcalc.health_calc_impl import HealthCalcImpl

@given('que tengo un BMI de {bmi}')
def step_bmi_value(context, bmi):
    context.bmi_value = float(bmi)

@when('clasifico el BMI')
def step_clasificar_bmi(context):
    try:
        calc = HealthCalcImpl()
        context.resultado = calc.bmi_classification(context.bmi_value)
    except Exception:
        context.resultado = "error"

@then('el resultado debe ser "{esperado}"')
def step_resultado_clasificacion(context, esperado):
    assert context.resultado == esperado