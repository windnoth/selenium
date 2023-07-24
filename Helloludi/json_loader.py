import json

with open("Sites.json", encoding='utf-8', errors='ignore') as f:
    sites = json.load(f)

class Mainsites():
    Main001_site = (sites['Main001_site'],['site'])
    Main002_site = (sites['Main002_site'],['site'])
    Main003_site = (sites['Main003_site'],['site'])
    Main004_site = (sites['Main004_site'],['site'])
    Main005_site = (sites['Main005_site'],['site'])
    Main006_site = (sites['Main006_site'],['site'])
    Main007_site = (sites['Main007_site'],['site'])
    Main008_site = (sites['Main008_site'],['site'])
    Main009_site = (sites['Main009_site'],['site'])
    Main010_site = (sites['Main010_site'],['site'])

class Mysites():
    My001_site = (sites['My001_site'],['site'])
    My002_site = (sites['My002_site'],['site'])
    My003_site = (sites['My003_site'],['site'])
    My004_site = (sites['My004_site'],['site'])
    My005_site = (sites['My005_site'],['site'])
    My006_site = (sites['My006_site'],['site'])
    My007_site = (sites['My007_site'],['site'])
    My008_site = (sites['My008_site'],['site'])
    My009_site = (sites['My009_site'],['site'])
    My010_site = (sites['My010_site'],['site'])
    My010_1_site = (sites['My010-1_site'],['site'])
    My011_site = (sites['My011_site'],['site'])
    My012_site = (sites['My012_site'],['site'])
    My013_site = (sites['My013_site'],['site'])

class Othersites():
    Other001_site = (sites['Other001_site'],['site'])
    Other002_site = (sites['Other002_site'],['site'])
    Other003_site = (sites['Other003_site'],['site'])
    Other004_site = (sites['Other004_site'],['site'])

with open("Config.json", encoding='utf-8', errors='ignore') as f:
    config = json.load(f)

class Config():
    Helloludi_id = (config['Helloludi_id'],['value'])
    Helloludi_pw = (config['Helloludi_pw'],['value'])
    kakao_id = (config['Kakao_id'],['value'])
    kakao_pw = (config['kakao_pw'],['value'])
