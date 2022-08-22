# parser-avito
Скрипт для парсинга запчастей для автомобилей с Авито

[![GitHub issues](https://img.shields.io/github/issues/Foxius/parser-avito?style=plastic)](https://github.com/Foxius/parser-avito/issues) [![GitHub stars](https://img.shields.io/github/stars/Foxius/parser-avito)](https://github.com/Foxius/parser-avito/stargazers) [![GitHub forks](https://img.shields.io/github/forks/Foxius/parser-avito)](https://github.com/Foxius/parser-avito/network)


*Описание:* Данный скрипт позволяет парсить детали автомобилей с авито по фильтру. Он получает производителя, номер детали, цену, описание и ссылку на объявление. Затем он записывает данные в .xlsx файл

## Как работает скрипт

запуск скрипт

парсинг первых 15 страниц

пауза 45 секунд

парсинг далее по кругу до 100 страницы

P.S. К сожалению, больше 15 не рекомендуется парсить без остановки, иначе ip забанят
