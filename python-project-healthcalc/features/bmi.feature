Feature: Cálculo del índice de masa corporal (BMI)

  Como usuario
  Quiero calcular mi BMI
  Para conocer mi estado de salud

  Scenario: Calcular BMI correctamente
    Given que introduzco una altura de 1.70 metros
    And un peso de 65 kg
    When calculo el BMI
    Then el resultado debe ser 22.49

  Scenario: Altura inválida
    Given que introduzco una altura de 0 metros
    And un peso de 65 kg
    When calculo el BMI
    Then se muestra un error

  Scenario: Peso inválido
    Given que introduzco una altura de 1.70 metros
    And un peso de -5 kg
    When calculo el BMI
    Then se muestra un error