DesiredTemperature = int(input('Введите желаемую температуру '))
TemperatureNow = int(input('Введите температуру в помещении '))
Humidity = int(input('Введите влажность '))
if TemperatureNow > DesiredTemperature and Humidity <= 80:
    print('on')
else:
    print('off')