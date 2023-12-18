import logging
from datetime import datetime, timedelta
""" Переменнная i считает сколько часов осталось от текущей
    даты до воскресенья """


d = datetime.now()
td = timedelta(hours=1)
for i in range(24*7):
    if d.weekday() == 6:
        break
    else:
        d = d + td

logging.basicConfig(filename='project.log.', filemode='a', encoding='utf-8', level=logging.NOTSET)
logger = logging.getLogger(__name__)
logger.info('Цикл будет продолжаться , пока не совпадёт с 6')