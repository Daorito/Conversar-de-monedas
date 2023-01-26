import requests

def currency_converter(from_currency, to_currency, amount):
    # URL de la API a utilizar
    url = f'https://api.exchangerate-api.com/v4/latest/{from_currency}'
    
    # Obtener los datos de la API
    response = requests.get(url)
    data = response.json()
    
    # Calcular el valor de la conversión
    from_rate = data['rates'][from_currency]
    to_rate = data['rates'][to_currency]
    converted_amount = amount * (to_rate / from_rate)
    
    return converted_amount

# Prueba del conversor
print(currency_converter('USD', 'EUR', 100))


print("------------------------------------------------------------------------------------")
print("Puede que en un futuo actualice la erramienta.")
print("github.com/Daorito")
print("replit.com/@BotDaorito")