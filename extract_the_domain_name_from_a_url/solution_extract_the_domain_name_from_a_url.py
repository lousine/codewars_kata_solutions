def domain_name(url):
    """
    Extracts the domain name from a URL without using additional imports.

    :param url: A string representing the URL.
    :type url: str
    :return: The extracted domain name as a string.
    :rtype: str or None
    """
    url = url.replace("http://","").replace("https://","")
    url = url.replace("www.","")

    parts = url.split(".")

    if len(parts) >1:
        return parts[0]
    else:
        return None

def domain_name_short(url):
    """ Short solution to the same kata. """
    return url.split("//")[-1].split("www.")[-1].split(".")[0]
