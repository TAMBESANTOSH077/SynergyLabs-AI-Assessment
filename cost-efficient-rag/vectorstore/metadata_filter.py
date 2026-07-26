def build_filter(category=None, file_type=None):

    where = {}

    if category:
        where["category"] = category

    if file_type:
        where["file_type"] = file_type

    return where