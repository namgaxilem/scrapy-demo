from datetime import datetime

def uri_params(params, spider):      
    return {**params, 
            "spider_name": spider.name,
            "now_year": datetime.now().year, 
            "now_month": datetime.now().month, 
            "now_date": datetime.now().day}