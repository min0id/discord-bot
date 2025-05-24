import re
import random

def __calc_dice(dice_expression):
    raw_dices = []
    sum_dices = 0
    
    index = re.search(r'[das]',dice_expression)
    
    if not index:
        sum_dices = int(dice_expression)
        return raw_dices, sum_dices
        
    index = index.start()
        
    count = int(dice_expression[:index]) if dice_expression[:index] != '' else 1
    letter = dice_expression[index:index+1]
    dice = int(dice_expression[index+1:])
    match letter:
        case "d":
            raw_dices = [random.randint(1, dice) for _ in range(count)]
            sum_dices = sum(raw_dices)
        case "a":
            raw_dices = [sorted([random.randint(1, dice), random.randint(1, dice)], reverse=True) for _ in range(count)]
            sum_dices = sum([pair[0] for pair in raw_dices])
        case "s":
            raw_dices = [sorted([random.randint(1, dice), random.randint(1, dice)]) for _ in range(count)]
            sum_dices = sum([pair[0] for pair in raw_dices])
    
    return raw_dices, sum_dices

def __calc_expression(dice_expressions, operators):
    result = 0
    result += dice_expressions[0][1]
    for i, operator in enumerate(operators):
        match operator:
            case '+':
                result += dice_expressions[i+1][1]
            case '-':
                result -= dice_expressions[i+1][1]
    return result

def roll(exp):
    exp = exp.replace(' ','')
    dice_expressions = re.findall(r'[A-Za-z0-9]+', exp)
    operators = re.findall(r'[+-]', exp)

    expressions = []
    
    for dice_expression in dice_expressions:
        expressions.append(__calc_dice(dice_expression))
        
    result = __calc_expression(expressions, operators)
    return expressions, operators, result

def __get_pretty_dice(dice_exression):

    if len(dice_exression[0]) == 0:
        return str(dice_exression[1])
    if type(dice_exression[0][0]) == int:
        return f"{dice_exression[0]}"
    if len(dice_exression[0]) == 1:
        return f'[**{dice_exression[0][0][0]}**, {dice_exression[0][0][1]}]'
    
    result = "{"
    
    for dice in dice_exression[0]:
        result += f'[**{dice[0]}**, {dice[1]}], '
    
    result = result [:-2] + "}"
    return result

def pretty_roll(exp):
    try:
        expressions, operators, result = roll(exp)
        
        res_string = __get_pretty_dice(expressions[0])
        
        for i, operator in enumerate(operators):
            res_string += f' {operator} '
            res_string += __get_pretty_dice(expressions[i+1])
        
    except:
        return "Error"
    return res_string, result

def main():
    eq = input('> ').replace(' ','')
    dice_expressions = re.findall(r'[A-Za-z0-9]+', eq)
    operators = re.findall(r'[+-]', eq)

    print(pretty_roll(eq))

    # expressions = []

    # # print(dice_expressions)
    # # print(operators)

    # for dice_expression in dice_expressions:
    #     expressions.append(__calc_dice(dice_expression))
        
    # print(expressions)
    # print(__calc_expression(expressions, operators))
    
    # for expression in expressions:
    #     print(__get_pretty_dice(expression))

if __name__ == '__main__':
    main()