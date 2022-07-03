# coding:utf-8
"""
Name : run.py
Author  : Mark
Contect : hongming666@outlook.com
Time    : 2022/6/10 10:32
Desc:
"""
import sys
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
from utils import get_config
def run():
    name = sys.argv[1]
    custom_settings = get_config(name)
    # 获取爬虫名称
    spider = custom_settings.get('spider', 'universal')
    project_settings = get_project_settings()
    settings = dict(project_settings.copy())
    # 合并配置
    settings.update(custom_settings.get('settings'))
    process = CrawlerProcess(settings)
    # 启动配置
    process.crawl(spider, **{'name':name})
    process.start()


if __name__ == '__main__':
    run()
