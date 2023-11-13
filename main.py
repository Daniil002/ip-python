import requests
from pyfiglet import Figlet
import folium

def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        data = {
            '[IP]': response.get('query'),
            '[Country]': response.get('country'),
            '[Region Name]': response.get('regionName'),
            '[City]': response.get('city'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon')
        }
        
        for k, v in data.items():
            print(f'{k} : {v}')
            
        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        area.save(f'{response.get("country")}_{response.get("city")}.html')
        
    except requests.exceptions.ConnectionError:
        print('[!] Please check your connection!')
    
    
def main():
    prewiev = Figlet(font='slant')
    print(prewiev.renderText('IP INFO'))
    ip = input('Please enter a target IP: ')
    
    get_info_by_ip(ip=ip)
    
if __name__ == '__main__':
    main()