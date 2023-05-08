import time  # for measuring 'intermediate generator' run time
import parser  # import parser file to provide parser tree
disct = {}  # dictionary to store variable information in each scope as the Intimidate_Code_Generator generates Intimidate_Code and assign temporary variable
count = 1  # keep track of temporary variables in the Intimidate_Code
label_track = 1  # keep track of Lable variables in the Intimidate_Code that are used for ~ goto ~

parser_tree = parser.parser_tree # referencing the parser tree list

def serach(my_dict, target_value):  # function that is used to search for same information in our disct dictionary
    for key, value in my_dict.items():
        if value[1] == target_value:
            return key
    return target_value


def Intemidiet_Code_Generator(list_of_tuples):
    global disct, count, label_track
    for node_name, *children in list_of_tuples:
        if node_name == "DECLARATION":
            hold1 = None
            hold2 = None
            for child in children:
                if child[0] == 'type_specifer':
                    hold1 = child[1]
                if child[0] == 'IDENTIFIER':
                    hold2 = child[1]
            t_v = f't{count}'
            disct[t_v] = (hold1, hold2, None)
            count += 1

        elif node_name == "variable_assignment":
            value = []
            store = ''
            t_v = None
            for child in children:
                if child[0] == "IDENTIFIER":
                    hold1 = child[1]
                    t_v = serach(disct, hold1)
                elif child[0] == "expression":
                    for t in child[1]:
                        t = serach(disct, t)
                        value.append(t)
                    trm = disct[t_v]
                    disct[t_v] = (trm[0], trm[1], ' '.join(str(x) for x in value))
                    count += 1
                    store += f"{t_v} = " + ' '.join(str(x) for x in value)
            print(store)

        elif node_name == "INITIALIZATION":
            store = ""
            hold1 = None
            hold2 = None
            for child in children:
                if child[0] == "type_specifier":
                    hold1 = child[1]
                elif child[0] == "IDENTIFIER":
                    hold2 = child[1]
                else:
                    value = []
                    for t in child[1]:
                        t = serach(disct, t)
                        value.append(t)
                    t_v = f't{count}'
                    disct[t_v] = (hold1, hold2, ' '.join(str(x) for x in value))
                    count += 1
                    store += f"{t_v} = " + ' '.join(str(x) for x in value)

            print(store)

        elif node_name == "FUNCTION":
            i = 0
            hold1 = None
            hold2 = None
            value = None
            scope = None
            for child in children:
                if child[0] == 'function_name':
                    scope = child[1]
                    print("func begin", child[1])
                elif child[0] == 'function_parameter':

                    for child in child[1]:
                        for child in child:
                            if isinstance(child, tuple):
                                if child[0] == "type_specifier":
                                    hold1 = child[1]
                                if child[0] != "type_specifier":
                                    hold2 = child[1]
                                    value = f"addr({child[1]})"
                                    t_v = f't{count}'
                                    disct[t_v] = (hold1, hold2, value)
                                    count += 1
                                    print(f"{t_v}  = {value}")

                            elif child != "IDENTIFIER":
                                hold2 = child
                                value = f"addr({child})"

                                t_v = f't{count}'
                                disct[t_v] = (hold1, hold2, value)
                                count += 1
                                print(f"{t_v}  = {value}")

                elif child[0] == 'function_body':
                    for sub_child in child[1]:
                        Intemidiet_Code_Generator([sub_child])
                    disct.clear()
                    print("func end")
                    print("\n")

        elif node_name == "WHILE-STATEMENT":
            vae = ""
            for child in children:
                if child[0] == 'condition':
                    for x in child[1]:
                        if isinstance(x, tuple):
                            for i in x:
                                t = serach(disct, i)
                                vae += t
                        else:
                            if x == '==':
                                x = '!='
                            elif x == '!=':
                                x = '=='
                            elif x == '<':
                                x = '>='
                            elif x == '>':
                                x = '<='
                            vae += x

                elif child[0] == 'while_body':
                    l = label_track
                    r = label_track + 1
                    print(f"L{l}: if ({vae}) goto L{r}")
                    for sub_child in child[1]:
                        label_track += 2
                        Intemidiet_Code_Generator([sub_child])
                    print(f"L{r} : ")

                if child[0] == 'return_statement':
                    print(f"L2:  return {child[1]}")

        elif node_name == "if_statment":
            end = int((len(children[0]) - 1) / 2 + 2)
            end = end + label_track - 1
            for child in children[0]:
                if child[0] == 'if_condition':
                    vae = ""
                    for x in child[1]:
                        if isinstance(x, tuple):
                            for i in x:
                                t = serach(disct, i)
                                vae += t
                        else:
                            if x == '==':
                                x = '!='
                            elif x == '!=':
                                x = '=='
                            elif x == '<':
                                x = '>='
                            elif x == '>':
                                x = '<='
                            vae += x
                    l = label_track
                    r = label_track + 1
                    print(f"L{l} : if ( {vae} ) goto L{r}")
                    label_track += 1

                elif child[0] == 'if_body':
                    for sub_child in child[1]:
                        Intemidiet_Code_Generator([sub_child])
                    print(f"goto  L{end}")

                elif child[0] == 'elif_condition':
                    vae = ""
                    for x in child[1]:
                        if isinstance(x, tuple):
                            for i in x:
                                t = serach(disct, i)
                                vae += t
                        else:
                            if x == '==':
                                x = '!='
                            elif x == '!=':
                                x = '=='
                            elif x == '<':
                                x = '>='
                            elif x == '>':
                                x = '<='
                            vae += x
                    l = label_track
                    r = label_track + 1
                    print(f"L{l} : if ( {vae} ) goto L{r}")
                    label_track += 1

                elif child[0] == 'elif_body':
                    for sub_child in child[1]:
                        Intemidiet_Code_Generator([sub_child])
                    print(f"goto  L{end}")

                elif child[0] == 'else_body':
                    l = label_track
                    label_track += 1
                    print(f'L{l} :')
                    for sub_child in child[1]:
                        Intemidiet_Code_Generator([sub_child])
                    print(f"L{end} :")
            label_track += 1

        elif node_name == "function_assignment":
            t = []
            function_name = None
            variable_name = None
            for child in children:
                if child[0] == 'IDENTIFIER':
                    variable_name = child[1]
                if child[0] == 'f_name':
                    function_name = child[1]
                if child[0] == 'param':
                    for parm in child[1]:
                        u = serach(disct, parm[1])
                        t.append(u)

            u = serach(disct, variable_name)
            my_t = disct[u]
            disct[u] = (my_t[0], my_t[1], f"{function_name}, {', '.join(str(x) for x in t)}")
            print(f"{u} = call {function_name}, {', '.join(str(x) for x in t)}")

        elif node_name == "return_statement":
            for child in children:
                t = serach(disct, child)
                print("return: ", t)


start_run_time_time = time.time()  # Record the Start run time-time of Intimidate_Code_Generator
Intemidiet_Code_Generator(parser_tree)  # calling the Intimidate_Code_Generator function and passing parser_tree-list
End_run_time_time = time.time()  # Record the End run time-time of Intimidate_Code_Generator
Program_Run_time = End_run_time_time - start_run_time_time  # Calculate the elapsed time (run time of Intimidate_Code_Generator function)
print(f"\nIntimidate_Code_Generator Program Runtime  :  {Program_Run_time} seconds")
