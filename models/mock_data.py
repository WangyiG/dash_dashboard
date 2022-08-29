from faker import Faker
from faker.providers import BaseProvider

faker = Faker(locale='zh_CN')

class Myjson(BaseProvider):


    def mock_line_data(self,n=10):
        data = [
            {
                "Date":faker.date(pattern='%Y-%m'),
                "scales":faker.random_int(min=145,max=1998)
            } for _ in range(n)
        ]
        return data

    def mock_pie_data(self,n=5):
        data  = [
            {
                "type":faker.country(),
                "value":faker.random_int(min=1000,max=2000)
            } for _ in range(n)
        ]
        return data

    def mock_bar_data(self,n=5):
        data = [
            {
                "year":year,
                "value":value,
                "type":type
            } for year,value,type in zip(
                [faker.year() for _ in range(5)]*2,
                [faker.random_int(min=100,max=300) for _ in range(10)],
                ["Lon","Bor"]*5
            )
        ]
        # 堆积图isStack=True数据无需排序,分组图isGroup=True则数据需预先排序
        data.sort(key=lambda x:x['year'])

        return data

    def mock_scatter_data(self,n=5):
        data = [
            {
                "x":x,
                "y":y,
                "size":size,
                "genre":genre
            } for x,y,size,genre in zip(
                [faker.random_int(min=1,max=50) for _ in range(2*n)],
                [faker.random_int(min=2,max=100) for _ in range(2*n)],
                [faker.random_int(min=2,max=100) for _ in range(2*n)],
                ["female","male"]*n
            )
        ]
        return data

    def mock_target_data(self):
        data = [
            {
                'icon':icon,
                'title':title,
                'value':f'{value}w+',
                'unit':unit
            } for icon,title,value,unit in zip(
                ['fc-document','fc-rules','fc-conference-call','fc-statistics'],
                [faker.company_prefix() for _ in range(4)],
                [faker.random_int(min=10,max=100) for _ in range(4)],
                [faker.currency_code() for _ in range(4)],
            )
        ]
        return data
    
faker.add_provider(Myjson)
