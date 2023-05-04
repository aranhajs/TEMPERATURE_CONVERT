#CONVERSÃO DE TEMPERATURA
import emoji
print(emoji.emojize('Olá, Mundo!:globe_showing_Americas:'))

print('#'*45)
temp01 = float(input('Informe a Temperatura em °C: '))
print('#'*45)
Fahrenheit = (temp01 * 9/5)+32
Kelvin = (temp01 + 273.15)

print(f'A Temperatura {temp01}°C corresponde a {Fahrenheit}°F')
print(f'A Temperatura {temp01}°C corresponde a {Kelvin}K')
print('#'*45)

print(emoji.emojize(':termômetro:', language='pt')*32)
