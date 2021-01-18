'''
Author: Maciej Dudzik s18496
----------------------------
Web Crawler - sometimes called a spider or spiderbot and often shortened to crawler,
 is an Internet bot that systematically browses the World Wide Web, typically for the purpose of Web indexing
  (web spidering).
Web search engines and some other websites use Web crawling or spidering software to update their web content or indices
 of other sites' web content.
 Web crawlers copy pages for processing by a search engine, which indexes the downloaded pages so that users can search
 more efficiently.
 ---------------------------
 Beautiful Soup - Python library for pulling data out of HTML and XML files.
'''
from multiprocessing import Pool
import requests
from bs4 import BeautifulSoup


class Myargs:
    def __init__(self, page, WebUrl):
        self.page = page
        self.WebUrl = WebUrl


def findit(myargs):
    results = []
    if myargs.page > 0:
        url = myargs.WebUrl
        code = requests.get(url)
        plain = code.text
        s = BeautifulSoup(plain, "html.parser")
        for link in s.findAll('a', {'class': 'bc-title-link'}):
            tet = link.get('title')
            results.append(tet)
            tet_2 = link.get('href')
            results.append(myargs.WebUrl + tet_2)
    return results


def main():
    with Pool(processes=10) as pool:
        results = [pool.map_async(findit, [Myargs(1, "https://www.makeuseof.com/tag/linkli-st-create-list-of-links/"),
                                           Myargs(1, "https://www.makeuseof.com/tag/linkli-st-create-list-of-links/"),
                                           Myargs(1, "https://www.makeuseof.com/tag/linkli-st-create-list-of-links/"),
                                           Myargs(1, "https://www.makeuseof.com/tag/linkli-st-create-list-of-links/"),
                                           Myargs(1, "https://www.makeuseof.com/tag/linkli-st-create-list-of-links/"),
                                           Myargs(1, "https://www.makeuseof.com/tag/linkli-st-create-list-of-links/"),
                                           Myargs(1, "https://www.makeuseof.com/tag/linkli-st-create-list-of-links/"),
                                           Myargs(1, "https://www.makeuseof.com/tag/linkli-st-create-list-of-links/"),
                                           Myargs(1, "https://www.makeuseof.com/tag/linkli-st-create-list-of-links/"),
                                           Myargs(1, "https://www.makeuseof.com/tag/linkli-st-create-list-of-links/")])]
        for res in results:
            for page in res.get(timeout=60):
                print("-----------------Next Page-----------------")
                for link in page:
                    print(link)
    return 0


if __name__ == '__main__':
    main()
