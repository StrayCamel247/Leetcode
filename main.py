import os
import sys
import logging

logging.basicConfig(level=logging.INFO)
questions_floder = './questions'
_listdir = os.listdir(questions_floder)
_listdir.sort()

# import parse
# 这个包还挺好用的
# # https://pypi.org/project/parse/
# id_x  =parse.search('{:d}.反转字符串.py', ''.join(_listdir))
# print(str(id_x.fixed[0])+'.反转字符串.py')


def _search(name):
    for _ in _listdir:
        if name in _:
            logging.info(os.path.join(questions_floder, _))
            break
    return _


if __name__ == "__main__":
    _search('反转字符串')