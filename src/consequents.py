from numpy import arange
from skfuzzy import control

disease = control.Consequent(arange(0, 10, 1), 'doenças')

disease.automf(names=['dengue', 'zika', 'chikungunya'])
