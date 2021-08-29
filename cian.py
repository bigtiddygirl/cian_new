from bs4 import BeautifulSoup as bs
import requests
import pyexcel as p
import re
import datetime
import gspread
import pandas as pd
import time
import os


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.41 YaBrowser/21.2.0.1122 Yowser/2.5 Safari/537.36'
    }


z = 1
lists = [
'https://ekb.cian.ru/novostroyki-sverdlovskaya-oblast/',
'https://tyumen.cian.ru/novostroyki-tyumenskaya-oblast/',
'https://novosibirsk.cian.ru/novostroyki-novosibirskaya-oblast/',
'https://krasnoyarsk.cian.ru/novostroyki-krasnoyarskiy-kray/',
'https://krasnodar.cian.ru/novostroyki-krasnodarskiy-kray/',
'https://maykop.cian.ru/novostroyki-adygeya/',
'https://volgograd.cian.ru/novostroyki-volgogradskaya-oblast/',
'https://stavropol.cian.ru/novostroyki-stavropolskiy-kray/',
'https://belgorod.cian.ru/novostroyki-belgorodskaya-oblast/',
'https://bryansk.cian.ru/novostroyki-bryanskaya-oblast/',
'https://vladimir.cian.ru/novostroyki-vladimirskaya-oblast/',
'https://voronezh.cian.ru/novostroyki-voronezhskaya-oblast/',
'https://ivanovo.cian.ru/novostroyki-ivanovskaya-oblast/',
'https://kaluga.cian.ru/novostroyki-kaluzhskaya-oblast/',
'https://kursk.cian.ru/novostroyki-kurskaya-oblast/',
'https://lipetsk.cian.ru/novostroyki-lipeckaya-oblast/',
'https://orel.cian.ru/novostroyki-orlovskaya-oblast/',
'https://ryazan.cian.ru/novostroyki-ryazanskaya-oblast/',
'https://smolensk.cian.ru/novostroyki-smolenskaya-oblast/',
'https://tambov.cian.ru/novostroyki-tambovskaya-oblast/',
'https://tver.cian.ru/novostroyki-tverskaya-oblast/',
'https://tula.cian.ru/novostroyki-tulskaya-oblast/',
'https://yaroslavl.cian.ru/novostroyki-yaroslavskaya-oblast/',
'https://vologda.cian.ru/novostroyki-vologodskaya-oblast/',
'https://kaliningrad.cian.ru/novostroyki-kaliningradskaya-oblast/',
'https://pskov.cian.ru/novostroyki-pskovskaya-oblast/',
'https://rostov.cian.ru/novostroyki-rostovskaya-oblast/',
'https://astrahan.cian.ru/novostroyki-astrahanskaya-oblast/',
'https://elista.cian.ru/novostroyki-kalmykiya/',
'https://mahachkala.cian.ru/novostroyki-dagestan/',
'https://nazran.cian.ru/novostroyki-ingushetiya/',
'https://nalchik.cian.ru/novostroyki-kabardino-balkarskaya/',
'https://cherkessk.cian.ru/novostroyki-karachaevo-cherkesskaya/',
'https://vladikavkaz.cian.ru/novostroyki-rso-alaniya/',
'https://groznyy.cian.ru/novostroyki-chechenskaya/',
'https://kostroma.cian.ru/novostroyki-kostromskaya-oblast/',
'https://arhangelsk.cian.ru/novostroyki-arhangelskaya-oblast/',
'https://syktyvkar.cian.ru/novostroyki-komi/',
'https://murmansk.cian.ru/novostroyki-murmanskaya-oblast/',
'https://novgorod.cian.ru/novostroyki-novgorodskaya-oblast/',
'https://naryan-mar.cian.ru/novostroyki-neneckiy-ao/'
'https://cheboksary.cian.ru/novostroyki-chuvashskaya/', 
'https://penza.cian.ru/novostroyki-penzenskaya-oblast/', 
'https://orenburg.cian.ru/novostroyki-orenburgskaya-oblast/', 
'https://saratov.cian.ru/novostroyki-saratovskaya-oblast/', 
'https://ulyanovsk.cian.ru/novostroyki-ulyanovskaya-oblast/', 
'https://perm.cian.ru/novostroyki-permskiy-kray/',
'https://kazan.cian.ru/novostroyki-tatarstan/',
'https://ufa.cian.ru/novostroyki-bashkortostan/',
'https://samara.cian.ru/novostroyki-samarskaya-oblast/',
'https://gorno-altaysk.cian.ru/novostroyki-altay/',
'https://barnaul.cian.ru/novostroyki-altayskiy-kray/',
'https://blagoveschensk.cian.ru/novostroyki-amurskaya-oblast/',
'https://ulan-ude.cian.ru/novostroyki-buryatiya/',
'https://birobidzhan.cian.ru/novostroyki-evreyskaya-ao/',
'https://chita.cian.ru/novostroyki-zabaykalskiy-kray/',
'https://irkutsk.cian.ru/novostroyki-irkutskaya-oblast/',
'https://petropavlovsk-kamchatskiy.cian.ru/novostroyki-kamchatskiy-kray/',
'https://kemerovo.cian.ru/novostroyki-kemerovskaya-oblast/',
'https://kurgan.cian.ru/novostroyki-kurganskaya-oblast/',
'https://omsk.cian.ru/novostroyki-omskaya-oblast/',
'https://vladivostok.cian.ru/novostroyki-primorskiy-kray/',
'https://yakutsk.cian.ru/novostroyki-yakutia/',
'https://yuzhno-sahalinsk.cian.ru/novostroyki-sahalinskaya-oblast/',
'https://yanao.cian.ru/novostroyki/',
'https://chelyabinsk.cian.ru/novostroyki-chelyabinskaya-oblast/',
'https://hmao.cian.ru/novostroyki/',
'https://abakan.cian.ru/novostroyki-hakasiya/',
'https://habarovsk.cian.ru/novostroyki-habarovskiy-kray/',
'https://kyzyl.cian.ru/novostroyki-tyva/',
'https://tomsk.cian.ru/novostroyki-tomskaya-oblast/',
]

def get_pages():
    #URL = input('url: ')
    all_buildings.append(URL)
    response = requests.get(URL, headers = HEADERS)
    soup = bs(response.content, 'lxml')

    global offers
    offers = soup.find('div', {
        'data-name':'OffersHeader'}).find('span').get_text().split(' ')

    global filename
    filename = URL.split('.')
    filename = re.sub('https://', '', filename[0])

    offers = int(offers[0])
    if offers <= 25:
        pass
    else:
        pages = (offers / 25) + 2


        page_link = soup.find('div', {
            'data-name':'Pagination'
        }).find('a').get('href')

        page_link = 'https://' + filename + '.cian.ru' + page_link
        page_link = page_link[:-1]
        for i in range(2, int(pages)):
            all_buildings.append(page_link + str(i))

def parse():
    page = 1
    x = 1
    for URL in all_buildings:
        response = requests.get(URL, headers = HEADERS)
        soup = bs(response.content, 'lxml')
        items = soup.find_all('div', {
            'data-name':'GKCardComponent',
            })
        for item in items:
            building_name = item.find('span', {'data-name':'Text'}).get_text()

            link = item.find('div', {'data-name':'Container',
            'data-mark':'GKCardTitle'}).find('a').get('href')
            response = requests.get(link, headers=HEADERS)
            soup = bs(response.content, 'lxml')
            item = soup.find('div', {'id':'newbuilding-card-desktop-frontend'})
            if item:
                paid = "Бесплатно"
            else:
                paid = "Платно"


            info.append({
                'building name':building_name,
                'link':link,
                'paid':paid,
                'region':filename.title(),
                'date':today,
            })
            print(z, '/', len(lists), '   ', x, '/', offers, ' ')
            x += 1
        page += 1

today = datetime.datetime.today().strftime("%d-%m-%Y")

info = []

if not os.path.isdir(today):
     os.mkdir(today)

for URL in lists:
    try:
        all_buildings = []
        get_pages()
        parse()
        name = f'{filename} {today}.xlsx'
        p.save_as(records=info, dest_file_name=f'{today}/{name}')
        z += 1
        
        gc = gspread.service_account(filename='fluid-gamma-319906-a4ea6dcfcfee.json')
        sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/10k3owGfIX2uh6Q7ygP3nOCxFM1RYur8mt-SzpcV_d9c/')

        worksheet = sh.worksheet("ЦИАН новостройки")

        df = pd.read_excel(f'{today}/{name}')

        worksheet.update([df.columns.values.tolist()] + df.values.tolist())
        time.sleep(15)
    except Exception as e:
        print(e)
        continue