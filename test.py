import re
from datetime import datetime
today = datetime.today()
formatted_date = today.strftime("%d/%m/%Y")

text = """08/06/2024 

Аксессуары/ Фото/ Описание ⬇️
@BSAAccessories

Гарантия 14 дней со дня покупки  🛍️

Получите дополнительную гарантию от 📱📱📱:      

 🛡 +3 месяца - 3.000₽
 🛡 +6 месяцев - 6.000₽
 🛡 +12 месяцев - 10.000₽


           📱14 128/ 256 /512

14 128 Blue -56.500🇮🇳
14 128 Blue -55.000🇺🇸
14 128 Midnight-57.500🇮🇳
14 128 Midnight-56.700🇨🇳
14 128 Midnight-55.000🇺🇸
14 128 Starlight-57.500🇮🇳
14 128 Purple-57.500🇮🇳
14 128 Purple -55.800🇨🇳
14 128 Yellow-60.800🇮🇳

14 256 Blue-68.200🇮🇳
14 256 Purple-69.500🇮🇳
14 256 Purple -64.000🇺🇸
14 256 Starlight-70.500🇮🇳
14 256 Red-68.000🇮🇳
14 256 Midnight-68.100🇮🇳
14 256 Midnight-64.000🇺🇸
14 256 Yellow-68.200🇮🇳

14 512 Red-79.500🇪🇭
14 512 Blue-81.400🇪🇭
14 512 Purple -81.400🇪🇭


           📱14 Plus 128/ 256 /512

14 Plus 128 Blue-59.900🇮🇳
14 Plus 128 Blue-57.000🇺🇸
14 plus 128 Midnight-58.300🇮🇳
14 Plus 128 Midnight-57.900🇺🇸
14 Plus 128 Starlight-58.300🇮🇳
14 Plus 128 Starlight-58.000🇺🇸
14 Plus 128 Red-62.000🇪🇭
14 Plus 128 Red-56.900🇺🇸
14 Plus 128 Yellow-61.900🇮🇳
14 Plus 128 Yellow-56.900🇺🇸
14 Plus 128 Purple-62.000🇮🇳
14 Plus 128 Purple-57.900🇺🇸

14 Plus 256 Yellow-71.300🇪🇺
14 Plus 256 Midnight-72.500🇦🇪
14 Plus 256 Starlight -69.900🇮🇳
14 Plus 256 Red-71.300🇪🇺
14 Plus 256 Red-71.300🇭🇰
14 Plus 256 Red-71.000🇺🇸
14 Plus 256 Purple -69.900🇦🇪
14 Plus 256 Blue-73.900🇪🇭
14 Plus 256 Blue -71.000🇺🇸

14 Plus 512 Red-82.300🇪🇭
14 Plus 512 Midnight-83.600🇪🇭
14 Plus 512 Blue-83.500🇮🇳
14 Plus 512 Purple -86.500🇮🇳
14 Plus 512 Purple -76.000🇺🇸
14 Plus 512 Starlight-84.500🇮🇳
14 Plus 512 Yellow-83.000🇮🇳


          📱14 Pro 128/ 256 /512

14 Pro 128  Black -79.000🇭🇰2 sim (демо версия )

14 Pro 256  Purple-86.200🇺🇸
14 Pro 256  Black -85.200🇺🇸

14 Pro 1Tb Black-108.900🇮🇳
14 Pro 1Tb Black-107.400🇺🇸


           📱14 PRO MAX 128/256/512

14 Pro Max 128 Black -90.000🇺🇸
14 Pro Max 128 Black -92.800🇵🇸
14 Pro Max 128 White -93.500🇵🇸
14 Pro Max 128 White -90.000🇺🇸

14 Pro Max 256 Gold -97.500🇦🇪
14 Pro Max 256 Black-99.500🇪🇭
14 Pro Max 256 Purple -94.200🇺🇸
14 Pro Max 256 Black-95.500🇭🇰(демо версия)

14 Pro Max 512 Black-106.900🇺🇸
14 Pro Max 512 Silver -108.000🇮🇳
14 Pro Max 512 Gold -107.800🇪🇺
14 Pro Max 512 Purple -107.800🇮🇳
14 Pro Max 512 Purple -107.800🇺🇸

14 Pro Max 1TB Black-123.000🇭🇰
14 Pro Max 1TB Purple-123.000 🇭🇰
14 Pro Max 1TB Purple-114.000🇺🇸
14 Pro Max 1TB Silver-123.000 🇭🇰
14 Pro Max 1TB Silver-114.000🇺🇸

            Уценённый товар!

14 128 Blue-49.000🇮🇳(актив /пиксель на экране )
14 128 Starlight-48.500🇮🇳(актив/битый пиксель )

14 pro 128 gold-81.000(не актив/ микро царапина на дисплее)

14 pro 256 purple-82.500(замена камеры в ОСЦ/актив)

14 pro max 128 black-83.000( замена дисплея в ОСЦ)

14 Pro Max 256 Black-90.500🇦🇪(Заменен в ОСЦ)


🍎
🇺🇸(Америка)
E SIM,только виртуальная(нет слота под сим ) только 14/15/-е модели iPhone

🇨🇳🇭🇰(Китай,Гонконг) -
Dual SIM,только физические,1 Слот под Sim ,вставляется обе Sim карты  (Е SIM не подключается )

🇰🇼🇯🇵🇨🇦🇮🇳🇸🇬🇪🇺(Дубай,Япония,Канада,Индия,Сингапур,Европа,Бразилия) -1Sim(физическая) +E SI            M(виртуальная)"""


def handle_prices(text) -> str:
    pattern = r'(\w+)\s*-\s*(\d+\.\d+)'

    matches = re.findall(pattern, text)

    
    
    for match in matches:
        new_price = str(int(match[1].replace('.',''))*8)
        new_price = new_price[:-3] + "." +  new_price[-3:]
        # print(f" Extracted number: {match[1]} new price {new_price}")

        #!handle prices
        text = text.replace(match[1],str(new_price))
    
    # print(text)
    return text




def get_anchor(text) -> str:
    result = ''
    d = []
    pattern = r'\b\s*(\d+)\s*/\s*(\d+)\s*/\s*(\d+)\s*\b'

    text = text.split('\n')

    for ind,val in enumerate(text):
        res = re.search(pattern, val) and formatted_date not in val
        if res:
            d.append(ind)
            # print(val,ind)

    for i in text[d[0]:]:
        result = result +  str(i) + '\n'
    
    # print(result)
    return result

r = get_anchor(text)
handle_prices(r)