# Telegram Bot Client Example - Techacademy.az

Bot client, elanın İD nömrəsinə görə avtomobil elanı haqda məlumatları veb saytdan götürür və teleqram kanalda paylaşır.

### Prerequisites

Python3, pip, virtualenv

### Quraşdırılma

1. Repo-nu local kompüterimizə clone edirik:
```
git clone https://github.com/elshadaghazade/techacademy_telegram_bot_example.git
```
2. Daha sonra fayllar olan qovluğa keçərək virtualenv-i set edirik:
```
cd techacademy_telegram_bot_example
virtualenv -p $(which python3) .py3
```

3. Virtualenv set olduqdan sonra onu aktiv edirik:
```
source .py3/bin/activate
```

4. Asılıqları package.txt faylından yükləyirik:
```
pip install -r pacakge.txt
```
5. .env_sample faylının adını dəyişib .env edirik:
```
mv .env_sample .env
```

6. .env faylını özümüzə uyğun dəyişdiririk:
```
ADS_BASE_URL=http://www.auto.az
BOT_URL=https://api.telegram.org/bot
BOT_TOKEN=******
CHANNEL_ID=*****
```

7. main.py faylını run edirik:
```
python main.py
```

Qeyd: virtualenv-i deaktiv etmək üçün deactivate əmrini yazmağınız kifayətdir

## Authors

* **Elshad Agayev** - *Fullstack Developer* - [LinkedIn Profile](https://www.linkedin.com/in/elshadaghazadeh/)
