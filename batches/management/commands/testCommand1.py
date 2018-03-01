from django.core.management.base import BaseCommand, CommandError
from batches.models import BitTest

import urllib.request as request
import datetime
import json

import ccxt


class Command(BaseCommand):
    """ Main """

    def handle(self, *args, **options):
        exchange_list = ['bitflyer', 'quoinex', 'zaif']
        ask_exchange = ''
        ask_price = 99999999
        bid_exchange = ''
        bid_price = 0

        for exchange_id in exchange_list:
            exchange = eval('ccxt.' + exchange_id + '()')
            orderbook = exchange.fetch_order_book('BTC/JPY')
            bid = orderbook['bids'][0][0] if len(orderbook['bids']) > 0 else None
            ask = orderbook['asks'][0][0] if len(orderbook['asks']) > 0 else None
            if ask < ask_price:
                ask_exchange = exchange_id
                ask_price = ask
            if bid > bid_price:
                bid_exchange = exchange_id
                bid_price = bid

        if ask_exchange != '':
            bitTest = BitTest(bidExchangeName=bid_exchange, bidPrice=bid_price, askExchangeName=ask_exchange, askPrice=ask_price, createDate=datetime.datetime.now())
            bitTest.save()
