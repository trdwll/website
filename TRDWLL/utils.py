
def get_formatted_data(query):
    archive = {}

    for obj in query:
        archive.setdefault(obj.published_date.year, []).append(obj)

    return archive