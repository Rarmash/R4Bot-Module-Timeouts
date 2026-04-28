# R4Bot-Module-Timeouts

Внешний модуль учёта тайм-аутов для [R4Bot](https://github.com/Rarmash/R4Bot).

## Что делает
- отслеживает выдачу тайм-аутов участникам
- увеличивает счётчик тайм-аутов в Firebase
- если установлен модуль `leaderboards`, добавляет вкладку `/leaderboard timeouts`
- использует runtime services из `bot.r4_services`
- не требует отдельного модульного конфига

## Требования
- R4Bot `>= 2.0`
- runtime context с `bot.r4_services`
- сервис `firebase`

## Интеграции
- модуль может зарегистрировать leaderboard-provider
- если `leaderboards` не установлен, это не считается ошибкой и модуль продолжает просто учитывать тайм-ауты

## Структура
- `module.json` — метаданные модуля
- `cog.py` — учёт тайм-аутов и listeners
- `service.py` — регистрация вкладки для модуля лидербордов
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
