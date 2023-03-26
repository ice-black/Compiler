import lexical_Analyzer

tokens = lexical_Analyzer.lex('program.c')

# Define a class to represent a node in the parse tree
class ParseTreeNode:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def add_child(self, child):
        self.children.append(child)


# Define the production rules for the language
# This is a simplified set of rules for illustration purposes only
rules = [
    ('<program>', ['<include_list>',  '<declaration>']),
    ('<include_list>', ['INCLUDE_DIRECTIVE']),

    ('<declaration>', ['<function_declaration>*', '<include_list>']),
    ('<declaration>', []),


    ('<function_declaration>', ['<type_specifier>', '<identifier>', '<parameter_list>',  '<compound_statement>']),

    #('<function_declaration_closure>', ['<type_specifier>', '<identifier>', '<parameter_list>',  '<compound_statement>']),

    ('<parameter_list>', ['LEFT_PAREN', '<type_specifier>', '<identifier>', 'RIGHT_PAREN']),
    ('<more_parameters>', ['COMMA', '<type_specifier>', '<identifier>', '<more_parameters>']),
    ('<more_parameters>', []),

    ('<type_specifier>', ['KEYWORD']),
    ('<identifier>', ['IDENTIFIER']),
    ('<identifier>', ['main_f']),

    ('<comma>', ['COMMA']),
    ('<compound_statement>', ['LEFT_BRACE', 'RIGHT_BRACE']),


]






# ('<function_declaration>', ['<type_specifier>', '<identifier>', 'LEFT_PAREN', 'RIGHT_PAREN', '<compound_statement>']),

# Define a function that recursively generates a parse tree from the token stream using the production rules
def parse(tokens, rule, kleene_dict=None):
    node = ParseTreeNode(rule[0])
    print(rule[0])
    for production in rule[1]:
        if production.endswith('*'):
            non_terminal = production[:-1]
            subrules = [r for r in rules if r[0] == non_terminal]
            if not subrules:
                raise ValueError("Invalid production rule: " + non_terminal)
            while True:
                match_found = False
                for subrule in subrules:
                    try:
                        child = parse(tokens, subrule, kleene_dict)
                        node.add_child(child)
                        print('\t \t Match', subrule)
                        match_found = True
                    except ValueError:
                        pass
                if not match_found:
                    break
                if not tokens:
                    break

        elif production.startswith('<'):
            # If the production is a non-terminal, recursively generate a subtree using the corresponding rule
            subrules = [r for r in rules if r[0] == production]
            if not subrules:
                raise ValueError("Invalid production rule: " + production)
            match_found = False
            for subrule in subrules:
                try:
                    child = parse(tokens, subrule, kleene_dict)
                    node.add_child(child)
                    match_found = True
                    print('\t \t Match', subrule)
                    break
                except ValueError as e:
                    print('r', e)

            if not match_found:
                raise ValueError("No matching subrule found for production rule: ", production)
        else:
            # If the production is a terminal, consume a token from the token stream and match it against the production
            if not tokens:
                raise ValueError("Unexpected end of input")

            token = tokens.pop(0)
            print('============', token)
            if token[0] != production:
                raise ValueError(f"Expected token type {production}, got {token[0]}: {token[1]}")
            node.add_child(ParseTreeNode(token))

    # Handle Kleene closure specified in the rule
    if kleene_dict and rule[0] in kleene_dict:
        while True:
            match_found = False
            for subrule in subrules:
                try:
                    child = parse(tokens, subrule, rules, kleene_dict)
                    node.add_child(child)
                    print('\t \t Kleene closure')
                    match_found = True
                except ValueError:
                    pass
            if not match_found:
                break
            if not tokens:
                break
    else:
        if not node.children and not tokens:
            raise ValueError("Unexpected end of input: expected more tokens")


# Define a function that runs the syntax analyzer on the token stream
def syntax_analyze(tokens):
    tree = parse(tokens, rules[0])
    if tokens:
        raise ValueError("Unexpected tokens at end of input")
    return tree


print('\nTOKENS\n\t', tokens)
tree = syntax_analyze(tokens)
print("tree", tree)
