def buscar_codigo_postal(distrito):
    """
    Busca los códigos postales asociados a un distrito específico.

    Args:
        distrito (str): El nombre del distrito a buscar.

    Returns:
        list[str] | str: Lista de códigos postales si el distrito existe, 
                        mensaje de error en caso contrario.
    """

    if not isinstance(distrito, str) or not distrito.isalpha():
        raise ValueError("El distrito debe ser una cadena de texto solo con letras.")

    codigos_postales = {
        "Pueblo Libre": ["15083", "15084", "15086", "15088"],
        "Magdalena del Mar": ["15086"],
        "San Miguel": ["15086"],
    }

    if distrito not in codigos_postales:
        return f"El distrito '{distrito}' no existe."

    return codigos_postales[distrito]


def buscar_distritos_por_codigo(codigo_postal):
    """
    Busca el distrito asociado a un código postal específico.

    Args:
        codigo_postal (str): El código postal a buscar.

    Returns:
        str | str: Nombre del distrito si el código postal existe, 
                        mensaje de error en caso contrario.
    """

    if not isinstance(codigo_postal, str) or not codigo_postal.isdigit():
        raise ValueError("El código postal debe ser una cadena de números.")

    codigos_postales = {
        "Pueblo Libre": ["15083", "15084", "15086", "15088"],
        "Magdalena del Mar": ["15086"],
        "San Miguel": ["15086"],
    }

    for distrito, codigos in codigos_postales.items():
        if codigo_postal in codigos:
            return distrito

    return f"El código postal '{codigo_postal}' no existe."


# Bloque de código principal
try:
    distrito = input("Ingrese el distrito: ")

    if distrito.isdigit():
        codigo = distrito
        print(f"Distrito buscado por código postal '{codigo}': {buscar_distritos_por_codigo(codigo)}")
    else:
        codigos_postales_str = input("Ingrese los códigos postales separados por espacio: ")
        codigos_postales = codigos_postales_str.split()

        for codigo_postal in codigos_postales:
            print(f"Distrito buscado por código postal '{codigo_postal}': {buscar_distritos_por_codigo(codigo_postal)}")


except ValueError as e:
    print(f"Error: {e}")