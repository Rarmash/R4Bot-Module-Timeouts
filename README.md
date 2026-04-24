# R4Bot-Module-Timeouts

Внешний модуль учёта тайм-аутов для [R4Bot](https://github.com/Rarmash/R4Bot).

## Что делает
- отслеживает выдачу тайм-аутов участникам
- увеличивает счётчик тайм-аутов в Firebase
- использует runtime services из `bot.r4_services`
- не требует отдельного модульного конфига

## Требования
- R4Bot `>= 2.0`
- runtime context с `bot.r4_services`
- сервис `firebase`

## Структура
- `module.json` — метаданные модуля
- `cog.py` — Discord cog
- `requirements.txt` — зависимости для IDE и локальной проверки

## Установка в R4Bot
```powershell
python manage_modules.py install github:Rarmash/R4Bot-Module-Timeouts@master --enable
```

## Разработка
Для нормальной подсветки импортов в IDE и локальной проверки модуля рекомендуется установить зависимости:

```powershell
python -m pip install -r requirements.txt
```
