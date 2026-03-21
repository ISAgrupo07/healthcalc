from behave import given, when, then
from healthcalc.health_calc_impl import HealthCalcImpl

@given('que tengo un BMI de {bmi}')
def step_bmi(context, bmi):
    context.bmi = float(bmi)

@when('clasifico el BMI')
def step_clasificar(context):
    try:
        calc = HealthCalcImpl()
        context.resultado = calc.bmi_classification(context.bmi)
    except Exception:
        context.resultado = "error"

@then('el resultado debe ser "{esperado}"')
def step_resultado(context, esperado):
    assert context.resultado == esperado

