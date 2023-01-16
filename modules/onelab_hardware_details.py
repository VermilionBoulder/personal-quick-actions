import json
import re
import webbrowser
from multiprocessing import Pool

import pyperclip
import requests


def _open_onelab_page(module_id):
    if re.match(r"^([\w\-.]{4,})$", module_id):
        full_unique_id_string = requests.get(f"https://onelab.eecloud.dynamic.nsn-net.net/index.php?m=Inventory&a"
                                             f"=ajaxQueryInv&query={module_id}")
        try:
            unique_id = json.loads(full_unique_id_string.text.strip("[]"))["detail"]
        except KeyError:
            return
        webbrowser.open_new_tab("https://onelab.eecloud.dynamic.nsn-net.net/index.php?m=Inventory&"
                                "a=view&uniqid={}&category={}&sub_category={}".format(unique_id["uniqid"],
                                                                                      unique_id["category"],
                                                                                      unique_id["sub_category"]))


def _create_pools():
    pool = Pool()
    copied_module_ids = [module_id.strip(',.;:') for module_id in pyperclip.paste().split()]
    pool.map(_open_onelab_page, copied_module_ids)


def open_onelab_pages():
    _create_pools()


if __name__ == "__main__":
    _create_pools()
