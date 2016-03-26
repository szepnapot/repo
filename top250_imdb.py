from bs4 import BeautifulSoup as bs
import requests
import re
import time

page = 0

while True:
    url = 'http://www.listchallenges.com/imdb-top-250-movies-of-all-time-1202015'
    if page > 6:
        print "\nFinished with the list!"
        break
    elif page >= 1:
        print "\n GETTING PAGE", page
        url += "/checklist/" + str(page)
        print url

    r = requests.get(url)
    soup = bs(r.text, "html.parser")

    titles = [movies.text for movies in soup.findAll('div', attrs={'class': 'item-name'})]
    regex = "^.+\(.{4}\)"
    to_write = open("movies.txt", "r+")
    for movie_titles in titles:
        m_v = re.findall(regex, movie_titles)
        if m_v:
            m_v = str(m_v)
            title_year = m_v[3:-9], m_v[-7:-3]
            lines = [line.rstrip('\n') for line in open('movielist.txt')]
            if title_year[0] in lines:
                print title_year[0], "already in list."
            else:
                print "Hey a new one!", "{:>10}".format(title_year[0])
                movielist = open('movielist.txt', "a")
                movielist.write(title_year[0] + '\n')
                search = {'type': 'movie', 'plot': 'short', 'r': 'json', 't': title_year[0], 'y': title_year[1]}
                r = requests.get('http://www.omdbapi.com/?', params=search)
                json = r.json()
                try:
                    exist = json["Title"]
                except KeyError:
                    continue
                else:
                    end = "\n"
                    try:
                        to_write.write(end + "Title:" + json["Title"] + end + "Year:" + json['Year'] + end +
                                        "Rated:" + json['Rated'] + end + "Released:" + json['Released'] + end +
                                        "Runtime:" + json['Runtime'] + end + "Genre:" + json['Genre'] + end +
                                        "IMDb Rating:" + json["imdbRating"] + end + "Metascore:" + json["Metascore"] +
                                        end + "IMDb-id:" + json['imdbID'] + end)
                    except UnicodeEncodeError:
                        continue
                    else:
                        print json["Title"] + " added."
                        time.sleep(0.05)
    page += 1



