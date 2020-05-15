from aip import AipOcr
import requests

# 定义常量
APP_ID = '19819142'
API_KEY = '1xom0eaZrlBAye5cdeSmLvkX'
SECRET_KEY = 'GV0Of7p75EjuwMuDOk1MQmAVKyBzqkG6'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


# 定义识别获取图片的内容
def get_cate(url):
    content_list = []
    image = requests.get(url)
    """ 调用通用文字识别（高精度版） """
    result = client.basicAccurate(image.content)

    lists = result['words_result']  # 列表
    for list in lists:
        # words = re.match('.*?([\u4e00-\u9fa5]+).*', list['words'])
        words = list['words'].strip('♀').strip('G')
        content_list.append(words)
    return content_list

if __name__ == '__main__':
    print(get_cate('http://img10.360buyimg.com/imgzone/jfs/t5596/92/58483080/31860/baac5b29/59153660N0d6b588d.jpg'))