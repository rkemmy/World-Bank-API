import urllib.request
import json

from app import Catalog, Metatype

# from app import app
# from instance.config import Config

def get_data():
    data = urllib.request.urlopen("http://api.worldbank.org/v2/datacatalog?format=json")

    d = data.read()

    data_dict = json.loads(d)
    data_log = data_dict["datacatalog"]
    return data_log
print(get_data())

# for data_item in data_log:
#     log_id = data_item["id"]
#     print(log_id)
#     metatype = data_item["metatype"]
    # print(metatype)


# for meta_item in metatype:
#     mt_id = meta_item["id"]
#     mt_value = meta_item["value"]
    # print(mt_id)
    # print(mt_value)

# print(data_log)