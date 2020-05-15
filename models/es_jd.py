
from elasticsearch_dsl import connections, MetaField
from elasticsearch_dsl import Document, Date, Nested, Boolean, \
    analyzer, InnerDoc, Completion, Keyword, Text

connections.create_connection(hosts=['localhost'], timeout=20)


class MedicineType(Document):

    pro_main_cate = Text()
    # pro_nums = Keyword()
    pro_price = Text()
    pro_store = Text()
    pro_details = Text()

    class Index:
        name = 'jd'


if __name__ == '__main__':
    MedicineType.init()