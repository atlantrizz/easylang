
variables = {}

def execute_command(command):
    tokens = command.strip().split()
    
    if tokens[0] == "bro" and len(tokens) >= 3 and tokens[2] == "=":
        var_name = tokens[1]
        value = eval(" ".join(tokens[3:]), {}, variables)  # Evaluate the expression
        variables[var_name] = value
        return f"{var_name} is now set to {value}"

    elif tokens[0] == "bro" and tokens[1] == "give" and tokens[2] == "me":
        var_name = tokens[3]
        return variables.get(var_name, f"that's a NameError, bro")

    elif tokens[0] == "bro" and tokens[1] == "import":
        module_name = tokens[2]
        globals()[module_name] = __import__(module_name)
        return f"bro, {module_name} imported"

    else:
        raise SyntaxError("Invalid command")
