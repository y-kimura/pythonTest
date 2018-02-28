from django.core.management.base import BaseCommand, CommandError
from batches.models import Kawase

import urllib.request as request
import datetime
import json


class Command(BaseCommand):

    """ Main """
    def handle(self, *args, **options):
        # Web APIにアクセス
        API = "http://api.aoikujira.com/kawase/get.php?code=USD&format=json"
        json_str = request.urlopen(API).read().decode("utf-8")
        data = json.loads(json_str)
        print("1USD=" + data["JPY"] + "JPY")

        updateDate = datetime.datetime.strptime(data["update"], "%Y-%m-%d %H:%M:%S")
        print(updateDate)

        kawase = Kawase(update=updateDate, jpy=data["JPY"])
        kawase.save()

        # # 保存ファイル名を決定
        # t = datetime.date.today()
        # fname = "./test/" + t.strftime("%Y-%m-%d") + ".json"
        # with open(fname, "w", encoding="utf-8") as f:
        #     f.write(json_str)