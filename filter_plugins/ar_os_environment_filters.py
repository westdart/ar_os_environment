def is_git_url(url):
    if url.startswith('http'):
        return True
    elif url.startswith('https'):
        return True
    elif url.startswith('git'):
        return True
    elif url.startswith('ssh'):
        return True

    return False


def is_not_git_url(url):
    return not is_git_url(url)


class FilterModule(object):
    '''
    custom jinja2 filters for working with collections
    '''

    def filters(self):
        return {
            'is_git_url': is_git_url,
            'is_not_git_url': is_not_git_url
        }
