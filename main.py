import requests
from bs4 import BeautifulSoup


link_list = []

def find_rank(keyword, website, search_query):

    rank, rank_list = 1, ""

    # Base search url of google
    url = "https://www.google.com/search?q="

    # Replaces whitespace with "+" in keyword
    keyword = keyword.replace(" ", "+")

    # Base url is updated with the keyword to be
    # searched in given number of search results.
    url = url + keyword + "&num=" + str(search_query)

    # requests.get(url) returns a response that is saved
    # in a reponse object called page.
    page = requests.get(url)

    # page.text gives us access to the web data in text
    # format, we pass it as an argument to BeautifulSoup
    # along with the html.parser which will create a
    # parsed tree in soup.
    soup = BeautifulSoup(page.text, 'html.parser')

    # soup.find_all finds the div, all having the same
    # class "ZINbbc xpd O9g5cc uUPGi" that is stored
    # in result_div
    result_div = soup.find_all('div', attrs={'class': 'ZINbbc xpd O9g5cc uUPGi'})

    # Iterate result_div and check for the given website
    # inside <a> tag adding the rank to the
    # rank_list if found.
    for div in result_div:
        try:

            # Finds <a> tag and checks if the url is present,
            # if present then check with the provided
            # website in main()
            link = div.find("a", href=True)

            link_list.append(link)

        except:
            pass
    return (rank_list, "Website Missing")[rank_list == ""]

find_rank("next best offer", )

print(link_list)