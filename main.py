from sklearn import svm
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import json


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADER'] = "Content-Type"

@app.route('/', methods=["POST"])
def processData():
    msg = request.form['message'].split(',')
    links = msg[1:-1]
    domain = msg[0]

    data = [
        [5,5,5,5,5],
        [1,1,1,1,1],
        [2,3,4,2,2],
        [5,4,5,5,4],
        [5,1,5,4,4],
        [5,5,2,5,2],
        [5,1,5,1,4]
    ]

    s = ['safe', 'unsafe','unsafe', 'safe', 'safe', 'unsafe', 'unsafe']

    rec_model = svm.SVC()
    rec_model.fit(data, s)

    badLinks = []
    for link in links:
        values = [bitly(link), redirect(link), blog(link), ood(link, domain), endDomain(link)]
        print(values)
        link_safety = rec_model.predict([values])
        data.append(values)
        s.append(link_safety[0])
        print(link,link_safety[0])
        if link_safety[0] == 'unsafe':
            badLinks.append(link)


    # link_safety = rec_model.predict([[5,2,5,2,5]])
    # data.append([5,2,5,2,5])
    # s.append(link_safety[0])
    
    return json.dumps(badLinks)

def redirect(link: str):
    if link.count("redirect") > 1:
        return 1
    if "redirect" in link:
        return 2
    return 5

def bitly(link: str):
    if "bit.ly" in link:
        return 1
    return 5

#www.coolmath.com

#www.wics.uci.edu

def ood(link: str, dom: str):
    name = dom.split('.')[1]
    if name in link:
        return 5
    return 1

# https://www.coolmath.com/games/math/cool/myfavorites
# https://www.wikipedia.org/
# https://www.savethekoala.com/about-koalas/interesting-facts

def endDomain(link: str):
    ending = link.split('.')
    p1 = None
    p2 = None
    try:
        p1 = ending[-1]
    except:
        pass
    try:
        p2 = ending[-2]
    except:
        pass

    ans1 = None
    ans2 = None
    if p1 is not None:
        ans1 = checkEndings(p1[:3])
    if p2 is not None:
        ans2 = checkEndings(p2[:3])

    if ans1 is not None:
        return ans1
    if ans2 is not None:
        return ans2
    return 3


def checkEndings(s):
    if s is None:
        return
    if s == 'gov':
        return 5
    if s == 'edu' or s == 'com' or s == 'org':
        return 4
    if s == 'net':
        return 2
    if s[0:2] == 'io' or s[0:2] == 'bz':
        return 1
        

def blog(link:str):
    if 'blog' in link:
        return 2
    else:
        return 5

if __name__ == '__main__':
    app.run()


# app.run(host='127.0.0.1')