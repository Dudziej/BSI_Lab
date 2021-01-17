from multiprocessing import Pool
import requests
from bs4 import BeautifulSoup


class Myargs:
    def __init__(self, page, WebUrl):
        self.page = page
        self.WebUrl = WebUrl



def findit(myargs):
    results = []
    if(myargs.page>0):
        url = myargs.WebUrl
        code = requests.get(url)
        plain = code.text
        s = BeautifulSoup(plain, "html.parser")
        for link in s.findAll('a', {'class':'bc-title-link'}):
            tet = link.get('title')
            results.append(tet)
            tet_2 = link.get('href')
            results.append(myargs.WebUrl + tet_2)
    return results


def main():
    with Pool(processes=10) as pool:
        results = [pool.map_async(findit, [Myargs(1,"https://www.makeuseof.com/tag/linkli-st-create-list-of-links/"),
                                           Myargs(1,"https://www.makeuseof.com/tag/linkli-st-create-list-of-links/"),
                                           Myargs(1,"https://www.makeuseof.com/tag/linkli-st-create-list-of-links/"),
                                           Myargs(1,"https://www.makeuseof.com/tag/linkli-st-create-list-of-links/"),
                                           Myargs(1,"https://www.makeuseof.com/tag/linkli-st-create-list-of-links/"),
                                           Myargs(1,"https://www.makeuseof.com/tag/linkli-st-create-list-of-links/"),
                                           Myargs(1,"https://www.makeuseof.com/tag/linkli-st-create-list-of-links/"),
                                           Myargs(1,"https://www.makeuseof.com/tag/linkli-st-create-list-of-links/"),
                                           Myargs(1,"https://www.makeuseof.com/tag/linkli-st-create-list-of-links/"),
                                           Myargs(1,"https://www.makeuseof.com/tag/linkli-st-create-list-of-links/")])]
        for res in results:
            for page in res.get(timeout=60):
                print("-----------------Next Page-----------------")
                for link in page:
                    print(link)
    return 0

if __name__ == '__main__':
    main()
