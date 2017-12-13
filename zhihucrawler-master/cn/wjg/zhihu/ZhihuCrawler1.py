import json
import os

import requests
import time

from Tools.scripts.treesync import raw_input
from bs4 import BeautifulSoup


def get_userInfo(userID):
    print(userID + "111111")
    user_url = 'https://www.zhihu.com/people/' + userID
    headers = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:41.0) Gecko/20100101 Firefox/41.0',
        "Referer": "http://www.zhihu.com/",
        'Host': 'www.zhihu.com',
    }
    response = s.get(user_url, headers=headers)

    # print response
    soup = BeautifulSoup(response.content, 'lxml')
    name = soup.find_all('span', {'class': 'name'})[1].string
    # print 'name: %s' % name
    ID = userID
    # print 'ID: %s' % ID
    location = soup.find('span', {'class': 'location item'})
    if location == None:
        location = 'None'
    else:
        location = location.string
    # print 'location: %s' % location
    business = soup.find('span', {'class': 'business item'})
    if business == None:
        business = 'None'
    else:
        business = business.string
    # print 'business: %s' % business
    gender = soup.find('input', {'checked': 'checked'})
    if gender == None:
        gender = 'None'
    else:
        gender = gender['class'][0]
    # print 'gender: %s' % gender
    employment = soup.find('span', {'class': 'employment item'})
    if employment == None:
        employment = 'None'
    else:
        employment = employment.string
    # print 'employment: %s' % employment
    position = soup.find('span', {'class': 'position item'})
    if position == None:
        position = 'None'
    else:
        position = position.string
    # print 'position: %s' % position
    education = soup.find('span', {'class': 'education item'})
    if education == None:
        education = 'None'
    else:
        education = education.string
    # print 'education: %s' % education
    major = soup.find('span', {'class': 'education-extra item'})
    if major == None:
        major = 'None'
    else:
        major = major.string
    # print 'major: %s' % major

    agree = int(soup.find('span', {'class': 'zm-profile-header-user-agree'}).strong.string)
    # print 'agree: %d' % agree
    thanks = int(soup.find('span', {'class': 'zm-profile-header-user-thanks'}).strong.string)
    # print 'thanks: %d' % thanks
    infolist = soup.find_all('a', {'class': 'item'})
    asks = int(infolist[1].span.string)
    # print 'asks: %d' % asks
    answers = int(infolist[2].span.string)
    # print 'answers: %d' % answers
    posts = int(infolist[3].span.string)
    # print 'posts: %d' % posts
    collections = int(infolist[4].span.string)
    # print 'collections: %d' % collections
    logs = int(infolist[5].span.string)
    # print 'logs: %d' % logs
    followees = int(infolist[len(infolist)-2].strong.string)
    # print 'followees: %d' % followees
    followers = int(infolist[len(infolist)-1].strong.string)
    # print 'followers: %d' % followers
    scantime = int(soup.find_all('span', {'class': 'zg-gray-normal'})[len(soup.find_all('span', {'class': 'zg-gray-normal'}))-1].strong.string)
    # print 'scantime: %d' % scantime

    info = (name, ID, location, business, gender, employment, position,
            education, major, agree, thanks, asks, answers, posts,
            collections, logs, followees, followers, scantime)
    return info

if __name__ == '__main__':
    login()
    userID = 'marcovaldong'
    print(userID)
    info = get_userInfo(userID)
    print ('The information of ' + userID + ' is: ')
    for i in range(len(info)):
        print (info[i])