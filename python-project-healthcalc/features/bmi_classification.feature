Feature: Clasificación del índice de masa corporal (BMI)

  Como usuario
  Quiero conocer la clasificación de mi BMI
  Para entender mi estado de salud

  Scenario: Clasificación normal
    Given que tengo un BMI de 22
    When clasifico el BMI
    Then el resultado debe ser "Normal weight"

  Scenario: Bajo peso
    Given que tengo un BMI de 17
    When clasifico el BMI
    Then el resultado debe ser "Moderate thinness"

  Scenario: Sobrepeso
    Given que tengo un BMI de 27
    When clasifico el BMI
    Then el resultado debe ser "Overweight"

  Scenario: BMI inválido negativo
    Given que tengo un BMI de -5
    When clasifico el BMI
    Then se muestra un error