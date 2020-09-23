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


def _search(name=''):
    name = name.split(' ')
    res = 0
    for _ in _listdir:
        if isinstance(name, list):
            for n in name:
                if n in _:
                    # logging.info(os.path.join(questions_floder, _))
                    floder = questions_floder+'/'+_
                    question_name = _.split('.')[-2]
                    print('- [{name}]({url})'.format(name=question_name,url=floder))
                    res +=1
        if isinstance(name, str) and name in _:
            # print(os.path.join(questions_floder, _))
            floder = questions_floder+'/'+_
            question_name = _.split('.')[-2]
            print('- [{name}]({url})'.format(name=question_name,url=floder))
            res +=1
    return res


if __name__ == "__main__":
    names = sys.argv[1:]
    for n in names:
        logging.info('查找{name}问题...'.format(name=n))
        res = _search(n)
        if not res:logging.warn('没找到{name}问题'.format(name=n))
        print()
    # def test(k):
    #     tmp = k
    #     res = [0 for _ in range(5)]
    #     res2 = [str(_)+tmp for _ in res]


    # # print(res, res2)
    # test(01)
