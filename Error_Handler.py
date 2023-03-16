# Grammar rules in dictionary form
grammar_rules = {
    "<program>": [["<statements>"]],
    "<statements>": [["<statement>"], ["<statement>", "<statements>"]],
    "<statement>": [["<expression>", ";"],
                    ["<conditional-statement>"],
                    ["<loop-statement>"],
                    ["<declaration>"]],
    "<declaration>": [["<type>", "<identifier>", ";"]],
    "<type>": [["int"], ["float"], ["double"], ["char"]],
    "<identifier>": [["<letter>"], ["<identifier>", "<letter>"], ["<identifier>", "<digit>"]],
    "<letter>": [["a"], ["b"], ["c"], ["d"], ["e"], ["f"], ["g"], ["h"], ["i"], ["j"],
                 ["k"], ["l"], ["m"], ["n"], ["o"], ["p"], ["q"], ["r"], ["s"], ["t"],
                 ["u"], ["v"], ["w"], ["x"], ["y"], ["z"], ["A"], ["B"], ["C"], ["D"],
                 ["E"], ["F"], ["G"], ["H"], ["I"], ["J"], ["K"], ["L"], ["M"], ["N"],
                 ["O"], ["P"], ["Q"], ["R"], ["S"], ["T"], ["U"], ["V"], ["W"], ["X"],
                 ["Y"], ["Z"], ["_"]],
    "<digit>": [["0"], ["1"], ["2"], ["3"], ["4"], ["5"], ["6"], ["7"], ["8"], ["9"]],
    "<expression>": [["<term>"], ["<term>", "<addop>", "<expression>"]],
    "<term>": [["<factor>"], ["<factor>", "<mulop>", "<term>"]],
    "<factor>": [["<identifier>"], ["<number>"], ["(", "<expression>", ")"]],
    "<addop>": [["+"], ["-"]],
    "<mulop>": [["*"], ["/"], ["%"]],
    "<number>": [["<digit>"], ["<number>", "<digit>"], ["<number>", ".", "<digit>"], ["<number>", "E", "<digit>"]],
    "<conditional-statement>": [["if", "(", "<condition>", ")", "<statement>", "[", "else", "<statement>", "]"],
                                ["if", "(", "<condition>", ")", "<statement>"]],
    "<condition>": [["<expression>", "<relop>", "<expression>"]],
    "<relop>": [["=="], ["!="], ["<"], ["<="], [">"], [">="]],
    "<loop-statement>": [["while", "(", "<condition>", ")", "<statement>"],
                         ["for", "(", "<for-initializer>", "<condition>", ";", "<for-expression>", ")", "<statement>"]],
    "<for-initializer>": [["<declaration>"], ["<expression>"]],
    "<for-expression>": [["<expression>"]]
}

# Terminals in the grammar
terminals = ["int", "float", "double", "char", ";", "(", ")", "{", "}", "<letter>", "<digit>",
             "+", "-", "*", "/", "%", "<number>", "==", "!=", "<", "<=", ">", ">=", "if",
             "else", "while", "for", ",", "="]

# First set for each nonterminal
first_sets = {
    "<program>": ["int", "float", "double", "char"],
        "<statement>": ["int", "float", "double", "char", "<identifier>", "if", "while", "for"],
    "<declaration>": ["int", "float", "double", "char"],
    "<type>": ["int", "float", "double", "char"],
    "<identifier>": ["<letter>"],
    "<letter>": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                 "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z", "A", "B", "C", "D",
                 "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
                 "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
                 "Y", "Z", "_"],
    "<digit>": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
    "<expression>": ["<identifier>", "<number>", "("],
    "<term>": ["<identifier>", "<number>", "("],
    "<factor>": ["<identifier>", "<number>", "("],
    "<addop>": ["+", "-"],
    "<mulop>": ["*", "/", "%"],
    "<number>": ["<digit>"],
    "<conditional-statement>": ["if"],
    "<condition>": ["<identifier>", "<number>", "("],
    "<relop>": ["==", "!=", "<", "<=", ">", ">="],
    "<loop-statement>": ["while", "for"],
    "<for-initializer>": ["int", "float", "double", "char", "<identifier>", "("],
    "<for-expression>": ["<identifier>", "<number>", "("]
}

# Follow set for each nonterminal
follow_sets = {
    "<program>": ["$"],
    "<statements>": ["}"],
    "<statement>": ["int", "float", "double", "char", "<identifier>", "if", "while", "for", "}"],
    "<declaration>": [";"],
    "<type>": ["<identifier>"],
    "<identifier>": [";", ",", "=", "<addop>", "<mulop>", "<relop>", ")"],
    "<letter>": ["<letter>", "<digit>"],
    "<digit>": ["<digit>", "."],
    "<expression>": [";", ",", ")", "<addop>", "<relop>"],
    "<term>": [";", ",", ")", "<addop>", "<relop>"],
    "<factor>": [";", ",", ")", "<addop>", "<mulop>", "<relop>"],
    "<addop>": ["<term>", "<identifier>", "<number>", "("],
    "<mulop>": ["<factor>", "<identifier>", "<number>", "("],
    "<number>": [";", ",", ")", "<addop>", "<mulop>", "<relop>"],
    "<conditional-statement>": ["else", "}"],
    "<condition>": [")"],
    "<relop>": ["<expression>", "<identifier>", "<number>", "("],
    "<loop-statement>": ["else", "}"],
    "<for-initializer>": ["<condition>"],
    "<for-expression>": [")"]
}