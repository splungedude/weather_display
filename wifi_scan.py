import network
import time
import urequests

timeout = 0

wifi = network.WLAN(network.STA_IF)
wifi.active(True)

wifi.connect('TMNL-8D42B2_2.4G', 'NEJH3C9GEY6MR8D7')

meteo_api = 'https://api.open-meteo.com/v1/forecast?latitude=52.1275&longitude=4.4486&hourly=temperature_2m,relative_humidity_2m,precipitation&daily=weather_code,temperature_2m_max,temperature_2m_min,sunrise,sunset,daylight_duration&timezone=Europe%2FBerlin&forecast_days=1&models=knmi_seamless'

if not wifi.isconnected():
    print('connecting...')
    while (not wifi.isconnected() and timeout < 5):
        print(5 - timeout)
        timeout += 1
        time.sleep(1)
        
if wifi.isconnected():
    # print('Connected:',wifi.ifconfig())
    req = urequests.get(meteo_api)
    # print(req.status_code)
    # print(req.text)
    meteo_data = eval(req.text)
    meteo_data_hourly = meteo_data['hourly']
    p = 0
    for i in meteo_data_hourly['time']:
        print(i, meteo_data_hourly['temperature_2m'][p], meteo_data_hourly['relative_humidity_2m'][p])
        p += 1
    # print(meteo_data['hourly'])
else:
    print('Time Out')

    
