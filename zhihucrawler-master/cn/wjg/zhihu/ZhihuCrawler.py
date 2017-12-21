import json
import os

import requests
import time

from Tools.scripts.treesync import raw_input
from bs4 import BeautifulSoup


def login():
    url = 'http://www.zhihu.com'
    loginURL = "http://www.zhihu.com/login/email"

    headers = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:41.0) Gecko/20100101 Firefox/41.0',
        "Referer": "http://www.zhihu.com/",
        'Host': 'www.zhihu.com',
    }

    data = {
        "email": "swingmr@163.com",
        "password": "wjg15080665949",
        "rememberme": "true",
    }
    global s
    s = requests.session()
    global xsrf
    if os.path.exists('cookiefile'):
        with open('cookiefile') as f:
            cookie = json.load(f)
        s.cookies.update(cookie)
        req1 = s.get(url, headers=headers)
        soup = BeautifulSoup(req1.text, "html.parser")
        xsrf = soup.find("input", {"name": "_xsrf", "type": "hidden"}).get("value")
        # 建立一个zhihu.html文件,用于验证是否登陆成功
        with open('zhihu.html', 'w') as f:
            f.write(req1.content)
    else:
        req = s.get(url, headers=headers)
        print (req)

        soup = BeautifulSoup(req.text, "html.parser")
        xsrf = soup.find("input", {"name": "_xsrf", "type": "hidden"}).get("value")

        data["_xsrf"] = xsrf

        timestamp = int(time.time() * 1000)
        captchaURL = 'http://www.zhihu.com/captcha.gif?=' + str(timestamp)
        print (captchaURL)

        with open('zhihucaptcha.gif', 'wb') as f:
            captchaREQ = s.get(captchaURL, headers=headers)
            f.write(captchaREQ.content)
        loginCaptcha = raw_input('input captcha:\n').strip()
        data["captcha"] = loginCaptcha
        loginREQ = s.post(loginURL, headers=headers, data=data)
        # print(loginREQ)
        # if not loginREQ.json()['r']:
        #     print (s.cookies.get_dict())
        #     with open('cookiefile', 'wb') as f:
        #         json.dump(s.cookies.get_dict(), f)
        # else:
        #     print ('login fail')


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
    name = soup.find_all('title')[0].string
    #soup.extract("b").find_all("p")[0]
    print(name);
    # print 'name: %s' % name
    ID = userID
    # print 'ID: %s' % ID
    location = soup.find('span', {'class': 'location item'})
    if location == None:
        location = 'None'
    else:
        location = location.string
    #print 'location: %s' % location
    business = soup.find('span', {'class': 'business item'})
    if business == None:
        business = 'None'
    else:
        business = business.string
    #print ('business: %s' % business)
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