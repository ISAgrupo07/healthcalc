from enum import Enum

# class syntax
class BMICategory(Enum):
    SEVERE_THINNESS = 1;
    MODERATE_THINNESS = 2;
    MILD_THINNESS = 3;
    NORMAL = 4;
    OVERWEIGHT = 5;
    OBESE_CLASS_I = 6;
    OBESE_CLASS_II = 7;
    OBESE_CLASS_III = 8;
