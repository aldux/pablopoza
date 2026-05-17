import urllib.request
import re
import os

os.makedirs('c:/pablopoza/images/medios', exist_ok=True)

urls = {
    'cronista': 'https://www.cronista.com/negocios/la-tercera-oleada-de-la-inteligencia-artificial-va-a-empezar-este-ano/',
    'lanacion': 'https://www.lanacion.com.ar/economia/negocios/formacion-captacion-de-talentos-y-nuevas-oficinas-los-desafios-frente-a-las-transformaciones-nid22112023/'
}

for name, url in urls.items():
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req).read().decode('utf-8')
        match = re.search(r'<meta property="og:image" content="(.*?)"', html)
        if match:
            img_url = match.group(1).replace('&amp;', '&')
            print(f"Downloading {img_url} to {name}.jpg")
            
            # Download using a request with headers to avoid 403
            img_req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(img_req) as response, open(f"c:/pablopoza/images/medios/{name}.jpg", 'wb') as out_file:
                data = response.read()
                out_file.write(data)
        else:
            print(f"No og:image found for {name}")
    except Exception as e:
        print(f"Failed for {name}: {e}")
