import requests
import sys


class URLocator():
    def __init__(self, url):

        self.link = url
        # Get HTTP Headers for information
        self.r = requests.get(url)

    # Find size in bytes from HTTP Header Content-Length
    def size(self):
        i = self.r.headers
        # Check if file size is provided
        if 'Content-Length' in i.keys():
            return i['Content-Length'] + " bytes"
        else:
            # The header containing the size information doesn't exist, inform user
            return 'File size not provided'

    # Find file type
    def f_type(self):
        i = self.r.headers['Content-Type']
        return i

    # Suggest file name
    def name(self):
        i = self.link.split("/")[-1]
        if "." in i:
            i = i.split(".")[0]

        else:
            pass
        return i


if __name__ == '__main__':
    machine = URLocator(input())
    print(machine.f_type())
    print(machine.size())
    print(machine.name())
