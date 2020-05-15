import json

from models.es_jd import MedicineType


def save_to_es():
    medicine = MedicineType()
    # print(self)
    medicine.pro_main_cate = '补肾壮阳'
    medicine.meta.id = '100005577526'
    medicine.pro_price = '322.00'
    medicine.pro_store = '汇仁京东自营旗舰店'
    # lines = json.dumps(dict(self['pro_details']), ensure_ascii=False)
    dict1 = {'产品规格': '0.7g*126片',
                 '剂型': '片剂',
                 '品牌': '汇仁',
                 '批准文号': '国药准字Z20080627',
                 '有效期': '36',
                 '生产企业': '江西汇仁药业股份有限公司',
                 '用法用量': '一日3次，一次3片',
                 '药品商品名': '肾宝片',
                 '药品类型': '中成药',
                 '药品通用名': '肾宝片',
                 '适用症/功能主治': '调和阴阳，温阳补肾，扶正固本用于腰腿酸痛，精神不振，夜尿频多，畏寒怕冷；妇女白带清稀'}
    lines = json.dumps(dict1, ensure_ascii=False)
    medicine.pro_details = lines
    medicine.save()


if __name__ == '__main__':
    save_to_es()