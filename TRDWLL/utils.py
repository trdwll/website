import git

def get_version_checksum():
    try:
        repo = git.Repo(search_parent_directories=True)
        return repo.head.object.hexsha[:7]
    except:
        return ''