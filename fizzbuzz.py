from lambdacalculus import *

FIZZ = PUSH(PUSH(PUSH(PUSH(EMPTY)(F))(I))(Z))(Z)
BUZZ = PUSH(PUSH(PUSH(PUSH(EMPTY)(B))(U))(Z))(Z)
FIZZBUZZ = PUSH(PUSH(PUSH(PUSH(FIZZ)(B))(U))(Z))(Z)

solution = MAP(RANGE(ONE)(HUNDRED))(lambda n: IF(IS_ZERO(MOD(n)(FIFTEEN)))(
    FIZZBUZZ
)(IF(IS_ZERO(MOD(n)(THREE)))(
    FIZZ
)(IF(IS_ZERO(MOD(n)(FIVE)))(
    BUZZ
)(
    TO_DIGITS(n)
))))

for s in to_array(solution):
    print(to_string(s))
