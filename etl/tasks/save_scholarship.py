from etl.config import elastic


def save_scholarship(item: dict):
    item = item.copy()
    elastic.create(index='scholarships', id=item.pop('id'), body=item)
