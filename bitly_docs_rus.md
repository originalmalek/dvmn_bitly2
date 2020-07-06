# <a name="Intro"></a> Документация к методам API Bitly на русском

Добро пожаловать в русскую документацию [API Bitly](https://dev.bitly.com/v4_documentation.html)! Если вы хотите использовать Bitly для сокращения, маркировки и распространения ссылок, то вы в нужном месте. Эта статья написана не в целях перевода документации на русский, а для упрощения понимания документации Bitly разработчиками, т.к. страницы документации очень перегружены информацией и даже опытным веб-разработчикам тяжело в ней ориентироваться.

Документация является не полной, переведены только те методы API, которые авторам показались самыми необходимыми. Если вы хотите поучаствовать в переводе — мы всегда будем рады любой помощи.

Документация создана в рамках разработки курсов [dvmn.org](https://dvmn.org/).

# <a name="Contents"></a> Оглавление

- [Введение](#Intro)
- [Оглавление](#Contents)
- [Авторизация](#Authentication)
  + [OAuth 2](#Oauth2)
- [Пользователи](#Users)
  + [Получить свой профиль](#user)
- [Битлинки](#Bitlinks)
  + [Развернуть битлинк](#Expand)
  + [Создать битлинк](#Create)
  + [Получить информацию по битлинкам по группе](#ByGroup)
  + [Получить сумму кликов по битлинку](#GetClicksSummary)
  + [Получить клики по битлинку по датам](#GetClicks)
  + [Обновить битлинк](#Update)
  + [Получить информацию о битлинке](#Retrieve)
  + [Сократить ссылку](#Shorten) 
- [Организации](#Organizations)
- [Группы](#Groups)
- [Кастомные битлинки](#CustomBitlinks)
- [Кампании](#Campaigns)
- [Фирменные коротиие домены](#BSD)
- [Лучшие практики](#BestPractices)

# <a name="Authentication"></a> Авторизация

Перед взаимодействием в API Bitly нужно получить токен. К счастью, для этого не нужно писать код, достаточно следовать инструкциям из документации.

Токен выглядит как строка наподобие следующей: `17c09e20ad155405123ac1977542fecf00231da7`. Bitly предлагает несколько видов токенов, но для методов, указанных в этой документации, хватит `GENERIC ACCESS TOKEN`. Ссылка для генерации токена указана на [странице документации Bitly](https://dev.bitly.com/get_started.html).

## <a name="Oauth2"></a> OAuth 2

Документация Bitly [гласит](https://dev.bitly.com/v4/#section/OAuth-2), что для авторизации с помощью OAuth 2 нужно только добавить к запросу HTTP-заголовок `Authorization: Bearer ВашТокен`.

[Почитать что это такое](https://security.stackexchange.com/a/120244).

# <a name="Users"></a> Пользователи

## <a name="user"></a> Получить свой профиль

Возвращает информацию о вашем профиле

**Адрес**: [/user](https://api-ssl.bitly.com/v4/user)

**Полный адрес**: `https://api-ssl.bitly.com/v4/user`

**Метод**: `GET`

**Формат данных**: JSON. Убедитесь, что передаёте не строку.

**Пример запроса**

```
GET /v4/user HTTP/1.1
Host: api-ssl.bitly.com
```

**Пример успешного ответа**

```json
{
  "created_at": "1970-01-01T00:00:00+0000",
  "modified": "1970-01-01T00:00:00+0000",
  "login": "alina01",
  "emails": [{"email": "example@gmail.com",
  ...
}
```

---

# <a name="Bitlinks"></a> Битлинки

«Битлинки» — это то, как мы называем сокращённые ссылки. Они с доменом `bit.ly` и выглядят, например, так: `bit.ly/ABCDE`.

---

## <a name="Expand"></a> Развернуть битлинк

Возвращает исходную ссылку из укороченной, и сообщит когда она была укорочена.

**Адрес**: [/expand](https://api-ssl.bitly.com/v4/expand)

**Полный адрес**: `https://api-ssl.bitly.com/v4/expand`

**Метод**: `POST`

**Формат данных**: JSON. Убедитесь, что передаёте не строку.

**Тело запроса**:

*bitlink_id* — битлинк, например: `bit.ly/ABCDE`.

**Пример запроса**

```
POST /v4/expand HTTP/1.1
Host: api-ssl.bitly.com
...
Body:
{ "bitlink_id": "bit.ly/2OaMRRO"}
```

**Пример успешного ответа**

```json
{
  "created_at":"2018-10-29T07:33:49+0000",
  "link":"http://bit.ly/2OaMRRO",
  "id":"bit.ly/2OaMRRO",
  "long_url":"http://dvmn.org/modules/"
}
```

---

## <a name="Create"></a> Создать битлинк

Создание укороченной ссылки, т.е. «битлинк». Является расширенной версией метода [Сократить ссылку](#Shorten).

**Адрес**: [/bitlinks](https://api-ssl.bitly.com/v4/bitlinks)

**Полный адрес**: `https://api-ssl.bitly.com/v4/bitlinks`

**Метод**: `POST`

**Формат данных**: JSON. Убедитесь, что передаёте не строку.

**Тело запроса**:

*long_url* (обязательный)- длинная ссылка, которую вы хотите сократить.

*group_guid* — id группы, к которой битлинк будет принадлежать.

_domain_ — на каком домене будет битлинк. По умолчанию это `bit.ly`, но можно его поменять на свой, корпоративный, например.

_title_ — название битлинка.

**Пример запроса**

```
POST /v4/bitlinks HTTP/1.1
Host: api-ssl.bitly.com
...
Body:
{ "long_url": "http://dvmn.org"}
```

**Пример успешного ответа**

```json
{
  "created_at": "1970-01-01T00:00:00+0000",
  "id": "bit.ly/2Diay99",
  "link": "http://bit.ly/2Diay99",
  "custom_bitlinks": [],
  "long_url": "http://dvmn.org/",
  "archived": false,
  "tags": [],
  "deeplinks": [],
  "references": {
    "group": "https://api-ssl.bitly.com/v4/groups/Biatc0ZvtUI"
  }
}
```

---

## <a name="GetClicksSummary"></a> Получить сумму кликов по битлинку

Возвращает сумму кликов по определённому битлинку. Метод сворачивает все данные о кликах в одно поле, `total_clicks`.

**Адрес**: [/bitlinks/{bitlink}/clicks/summary](https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary)

**Полный адрес**: `https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary`

**Метод**: `GET`

**Параметры пути**:

_bitlink_ — Битлинк вида `bit.ly/ABCDE`.

**Параметры запроса**:

_unit_ — Единица измерения времени. По умолчанию `day`, но есть ещё `minute`, `hour`, `week`, `month`.

_units_ — Число "единиц измерения", для которых считать метрики. По умолчанию `-1`. Когда `units` равен `-1`, возвращаются клики за всё время.

_size_ — Число результатов, которое необходимо вернуть.

*unit_reference* — таймстемп стандарта `ISO-8601`, указывающий последнюю точку времени, по которой выводить метрики. По умолчанию устанавливается текущее время (т.е. метрики вернутся за всё время, без ограничений).


**Пример запроса**

```
GET /v4/bitlinks/bit.ly/2Diay99/clicks/summary?unit=day&units=-1 HTTP/1.1
Host: api-ssl.bitly.com
```

**Пример успешного ответа**

```json
{
  "unit_reference": "2018-11-12T12:09:11+0000",
  "total_clicks": 14,
  "units": -1,
  "unit": "day"
}
```

---

## <a name="GetClicks"></a> Получить клики по битлинку по датам

Возвращает клики по определённому битлинку с указанием отрезков времени, в которые они были сделаны.

**Адрес**: [/bitlinks/{bitlink}/clicks](https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks)

**Полный адрес**: `https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks`

**Метод**: `GET`

**Параметры пути**:

_bitlink_ — Битлинк вида `bit.ly/ABCDE`.

**Параметры запроса**:

_unit_ — Единица измерения времени. По умолчанию `day`, но есть ещё `minute`, `hour`, `week`, `month`.

_units_ (обязательный) — Число "единиц измерения", для которых считать метрики. По умолчанию `-1`.

_size_ — Число результатов, которое необходимо вернуть.

*unit_reference* — таймстемп стандарта `ISO-8601`, указывающий последнюю точку времени, по которой выводить метрики. По умолчанию устанавливается текущее время (т.е. метрики вернутся за всё время, без ограничений).

**Пример запроса**

```
GET /v4/bitlinks/bit.ly/2Diay99/clicks?unit=day&units=-1 HTTP/1.1
Host: api-ssl.bitly.com
```

**Пример успешного ответа**

```json
{
  "unit_reference": "2018-11-12T12:16:07+0000",
  "link_clicks": [
    {
      "date": "2018-11-12T00:00:00+0000",
      "clicks": 1
    }
  ],
  "units": -1,
  "unit": "day"
}
```

---

## <a name="Retrieve"></a> Получить информацию о битлинке

Возвращает информацию о битлинке. Заархивирован-ли, кем создан, когда и т.д.

**Адрес**: [/bitlinks/{bitlink}](https://api-ssl.bitly.com/v4/bitlinks/{bitlink})

**Полный адрес**: `https://api-ssl.bitly.com/v4/bitlinks/{bitlink}`

**Метод**: `GET`


**Пример запроса**

```
GET /v4/bitlinks/bit.ly/2Diay99/ HTTP/1.1
Host: api-ssl.bitly.com
```

**Пример успешного ответа**

```json
{
  "created_at": "2018-11-12T12:00:46+0000",
  "id": "bit.ly/2Diay99",
  "link": "http://bit.ly/2Diay99",
  "custom_bitlinks": [],
  "long_url": "http://dvmn.org/",
  "title": "Devman - курс веб-разработки на Python",
  "archived": false,
  "created_by": "o_4eeh3glen0",
  "client_id": "a5e8cebb233c5d07e5c553e917dffb92fec5264d",
  "tags": [],
  "deeplinks": [],
  "references": {
    "group": "https://api-ssl.bitly.com/v4/groups/Biatc0ZvtUI"
  }
}
```

---

## <a name="Shorten"></a> Сократить ссылку

Сократить ссылку и получить битлинк. Является упрощённой версией метода [Создать битлинк](#Create).

**Адрес**: [/shorten](https://api-ssl.bitly.com/v4/shorten)

**Полный адрес**: `https://api-ssl.bitly.com/v4/shorten`

**Метод**: `POST`

**Формат данных**: JSON. Убедитесь, что передаёте не строку.

**Тело запроса**:

*long_url* (обязательный)- длинная ссылка, которую вы хотите сократить.

*group_guid* — id группы, к которой битлинк будет принадлежать.

_domain_ — на каком домене будет битлинк. По умолчанию это `bit.ly`, но можно его поменять на свой, корпоративный, например.

**Пример запроса**

```
POST /v4/shorten HTTP/1.1
Host: api-ssl.bitly.com
...
Body:
{ "long_url": "http://dvmn.org"}
```

**Пример успешного ответа**

```json
{
  "created_at": "1970-01-01T00:00:00+0000",
  "id": "bit.ly/2DeW5e2",
  "link": "http://bit.ly/2DeW5e2",
  "custom_bitlinks": [],
  "long_url": "http://dvmn.org/modules/",
  "archived": false,
  "tags": [],
  "deeplinks": [],
  "references": {
    "group": "https://api-ssl.bitly.com/v4/groups/Biatc0ZvtUI"
  }
}
```

---

[Разделы в разработке. Если вы хотите поучаствовать в переводе — мы всегда будем рады любой помощи.]
# <a name="Organizations"></a> Организации
# <a name="Groups"></a> Группы
# <a name="Campaigns"></a> Кампании
# <a name="BSD"></a> Фирменные короткие домены
# <a name="BestPractices"></a> Лучшие практики
