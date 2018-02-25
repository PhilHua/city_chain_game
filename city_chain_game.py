# coding=utf-8
from pinyin import PinYin
import json
from pandas.io.json import json_normalize
import random
import sys
# Check if a string contains non-chinese character
reload(sys)
sys.setdefaultencoding('utf8')

def check_contain_english(check_str):
    for ch in check_str.decode('utf-8'):
        if ch <= u'\u4e00' or ch >= u'\u9fff':
            return True
    return False

# import city name into pandas Dataframe
with open('ChinaCityList.json') as json_data:
    d = json.load(json_data)
# extract city name into list
city = json_normalize(data=d, record_path=['city', 'county'])
city_name = city.name.tolist()
city_name = [x.encode('utf-8') for x in city_name]
# Build a dictionary in the form of city:pinying
trans = PinYin()
trans.load_word()
to_py = trans.hanzi2pinyin
city_py = [to_py(x) for x in city_name]
city_dict = dict(zip(city_name, city_py))

# city chain game
def city_chain(city):
    if len(city) == 0:
        print '错误：请确认是否输入汉字'
    elif check_contain_english(city):
        print '错误：请确认是否输入了非汉字'
    else:
        candidate = []
        py_city = to_py(city)
        py_last_word = py_city[len(py_city)-1]
        for key, value in city_dict.iteritems():
            if py_last_word == value[0]:
                candidate.append(key)
        #Randomly output a city if possible
        if len(candidate) != 0:
            print candidate[random.randint(0,len(candidate)-1)]
        else:
            print '找不到合适的城市，我输了。'

#test
#city_chain('北京')

if __name__ == '__main__':
    while True:
        city_input = raw_input("请输入城市名: ")
        city_chain(city_input)



