import json_parse
import creat_xlsx
import request
#import requests


#feature to add
    #search ability with input
    #changeble fake identity(with UI)
    #image only downloader
    #tweet text filtered with keyword
    #include more information about user
    #infinite scroll adaptation
    #twitter adavance search feature
    #UI


def main():
    results = json_parse.parse(request.json_package)
    creat_xlsx.creat_xlsx(results)


if __name__ == "__main__":
    main()

