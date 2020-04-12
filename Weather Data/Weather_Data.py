import requests
from bs4 import BeautifulSoup

def Fahrenheit_to_celcius(temp_F):
    return(temp_F-32)*5/9

def get_city_data(city_name):

    url='https://www.wunderground.com/weather/in/'
    #Only for Indian cities
    url=url+city_name

    r=requests.get(url)
    soup=BeautifulSoup(r.content, 'html5lib')

    div_temp=soup.find_all('div', class_='current-temp')
    span_temp=div_temp[0].find('span', class_='wu-value wu-value-to')
    city_temp=span_temp.contents[0]

    div_humidity=soup.find_all('div', class_='small-8 columns')
    span_humidity=div_humidity[0].find('span', class_='wu-value wu-value-to')
    city_humidity=span_humidity.contents[0]
    
    city_temp=Fahrenheit_to_celcius(int(city_temp))      #converting from F to C
    city_temp=int(city_temp)
    city_humidity=float(city_humidity)
    city_humidity=int(city_humidity)
    return city_temp, city_humidity

#getting data from input.txt file

input_data=open('input.txt', 'r')
city_names=input_data.readlines()
input_data.close()

output_data=open('output.txt', 'a')

for city in city_names:
    city=city.strip()
    temp, humidity = get_city_data(city)
    output_data.write(city+' '+str(temp)+' '+str(humidity)+'%'+'\n')

output_data.close()