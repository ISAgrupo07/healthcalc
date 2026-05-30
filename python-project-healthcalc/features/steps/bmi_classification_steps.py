from behave import given, when, then
from healthcalc.health_calc_impl import HealthCalcImpl
from healthcalc.patient import Patient
from healthcalc.gender import Gender

CATEGORY_LABELS = {
    "SEVERE_THINNESS": "Severe thinness",
    "MODERATE_THINNESS": "Moderate thinness",
    "MILD_THINNESS": "Mild thinness",
    "NORMAL": "Normal weight",
    "OVERWEIGHT": "Overweight",
    "OBESE_CLASS_I": "Obesity class I",
    "OBESE_CLASS_II": "Obesity class II",
    "OBESE_CLASS_III": "Obesity class III",
}

@given('que tengo un BMI de {bmi}')
def step_bmi_value(context, bmi):
    context.bmi_value = float(bmi)

@when('clasifico el BMI')
def step_clasificar_bmi(context):
    try:
        calc = HealthCalcImpl()
        persona = Patient(context.bmi_value, 1.0, Gender.MALE, 30)
        categoria = calc.bmi_classification(persona)
        context.resultado = CATEGORY_LABELS[categoria.name]
    except Exception:
        context.resultado = "error"

@then('el resultado debe ser "{esperado}"')
def step_resultado_clasificacion(context, esperado):
    assert context.resultado == esperado