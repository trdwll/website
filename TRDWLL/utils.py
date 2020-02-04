import git

def get_version_checksum():
    try:
        repo = git.Repo(search_parent_directories=True)
        return repo.head.object.hexsha[:7]
    except:
        return ''

def get_formatted_data(query):
    archive = {}

    for obj in query:
        archive.setdefault(obj.published_date.year, []).append(obj)

    return archive