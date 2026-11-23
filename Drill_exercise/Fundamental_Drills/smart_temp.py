def smart_temperature(value):
    # value in kelvin
    # Celsius = 0
    # if int(value[0]).isdigit():
    #     Celsius = value - 273.15
    # else:
    #     return ""
    try:
        k = float(value)
    except (ValueError, TypeError):
        return "Invalid temperature"

    Celsius = k
    fahrenheit = (Celsius * 9/5 ) + 32
    
    if Celsius <= 0:
        status = "freezing"
    elif Celsius < 20:
        status = "cold"
    elif Celsius >= 20 and Celsius <= 30:
        status = "warm"
    else:
        status = "hot"

    return f"Celsius: {Celsius}\nFahrenheit: {fahrenheit}\nStatus: {status}"

