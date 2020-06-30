from elasticsearch.helpers import scan

from etl.config import elastic


def read_raw_scholarhips(spider):
    def run_task():
        for hit in scan(elastic, query={'query': {'term': {'spider.name': spider.value}}}):
            item = hit['_source'].copy()

            item['id'] = hit['_id']  # Attach id to item

            yield item

    return run_task
