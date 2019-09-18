"""
Contains utility functions to be used across the project
"""
def clean_string(function):
    """
    A decorator to replace characters based on a given rule set
    rule: [(char_to_replace, new_char)]
    """
    def do_cleaning(num, rules):
        """
        num: int, float
        rules: list of set
        """
        word = function(num, rules)
        if word and rules:
            for rule in rules:
                word = word.replace(rule[0], rule[1])
            return word
        return None
    return do_cleaning

@clean_string
def format_num(input_number, clean_rule):
    """
    input_number: int, float
    """
    if input_number == 0 or input_number and clean_rule:
        format_rule = "{:,.2f}"
        result = format_rule.format(float(input_number))
        return result
    return None
