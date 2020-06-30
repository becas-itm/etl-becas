from etl.scholarship import FillStatus


def is_complete(item):
    fields = ['description', 'academicLevel', 'country', 'fundingType', 'language']

    for field in fields:
        if field not in item:
            return False

    return True


def calc_fill_status(item):
    item['fillStatus'] = FillStatus.COMPLETE.value if is_complete(
        item) else FillStatus.INCOMPLETE.value
    return item
