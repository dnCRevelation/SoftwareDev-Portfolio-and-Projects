import urllib.request, urllib.parse
import html, json, ssl

# Heavily rate limited proxy of https://geoapify.com/ api #
serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print('======Type exit or press enter to quit======')
    address = input('Enter location: ')
    
    if len(address) < 1:
        print('\n')
        print('Thank you for visiting!')
        print('\n')
        print('Exiting program...') 
        break
    elif address == 'exit':
        print('\n')
        print('Thank you for visiting!')
        print('\n')
        print('Exiting program...')
        break
    

    address = address.strip()
    parms = {}
    parms['q'] = address

    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving:', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))

    try:
        js = json.loads(data)
    except:
        js = None
    
    if not js or 'features' not in js:
        print('======= DOWNLOAD ERROR =======')
        print(data)
        break

    if len(js['features']) == 0:
        print('======= OBJECT NOT FOUND ========')
        print(data)
        break

    lat = js['features'][0]['properties']['lat']
    lon = js['features'][0]['properties']['lon']
    #print('\nLatitude:', lat, 'Longitude', lon)

    cnty = js['features'][0]['properties']['county']
    location = js['features'][0]['properties']['formatted']
    timezone = js['features'][0]['properties']['timezone']['abbreviation_STD']
    plus_code = js['features'][0]['properties']['plus_code']
    print(location, '\nPlus Code:', plus_code)

    #print('\n', '\n', json.dumps(js, indent=4))

    