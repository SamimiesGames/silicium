def translate(source, variable, value):
    variable = "{%" + f" {variable} " + "%}"
    source = source.replace(variable, value)

    return source
