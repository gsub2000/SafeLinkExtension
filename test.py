from sklearn import svm
from urllib.parse import urlparse

link = "https://www.coolmath.com/0-teacher-success-area-prealgebra-algebra-precalculus"
domain_name = urlparse(link).netloc
scheme = urlparse(link).scheme
path = urlparse(link).path

print(domain_name)
print(scheme)
print(path)

print(len('https://www.coolmath.com/0-teacher-success-area-prealgebra-algebra-precalculus'))


def processData():
    msg = ["https://www.coolmath.com/#main-content",
    "https://www.coolmathgames.com/",
    "https://www.coolmath.com/",
    "https://www.coolmath.com/prealgebra",
    "https://www.coolmath.com/algebra",
    "https://www.coolmath.com/precalculus-review-calculus-intro",
    "https://www.coolmath.com/0-cool-math-games-and-problems",
    "https://www.coolmath.com/reference/online-math-dictionary",
    "https://www.coolmath.com/math-anxiety-survival-guide",
    "https://www.coolmath4kids.com/",
    "https://www.coolmath.com/reference/geometry-trigonometry-reference",
    "https://www.coolmath.com/0-teacher-success-area-prealgebra-algebra-precalculus",
    "https://www.coolmathgames.com/",
    "https://www.coolmath.com/prealgebra",
    "https://www.coolmath.com/prealgebra/00-factors-primes",
    "https://www.coolmath.com/prealgebra/02-decimals",
    "https://www.coolmath.com/algebra",
    "https://www.coolmath.com/algebra/01-exponents",
    "https://www.coolmath.com/algebra/08-lines",
    "https://www.coolmath.com/algebra/15-functions",
    "https://www.coolmath.com/precalculus-review-calculus-intro",
    "https://www.coolmath.com/precalculus-review-calculus-intro/precalculus-trigonometry/28-the-unit-circle-01",
    'https://www.coolmath.com/#',
    'https://www.coolmath4kids.com/',
    'https://www.coolmathgames.com/',
    'http://www.coolmath4teachers.com/',
    'http://www.coolmath4parents.com/',
    'https://www.coolmathgames.com/0-make-24-0',
    'https://www.coolmathgames.com/0-math-clash',
    "https://mail.redirect.com/hello/cool/about",
    "https://bit.ly/hkjhjkhjkh/ghfffgf.about.html"

    ]
    links = msg
    domain = "www.coolmath.com"

    data = [
        [5,5,5,5,5,5,5],
        [1,1,1,1,1,1,1],
        [1,1,1,1,1,5,5],
        [2,3,4,2,2,3,3],
        [5,4,5,5,4,3,3],
        [5,1,5,4,4,3,3],
        [5,5,2,5,2,3,3],
        [5,1,5,1,4,3,3],
        [5,5,5,2,3,1,5]
    ]

    s = ['safe', 'unsafe','unsafe','unsafe', 'safe', 'safe', 'unsafe', 'unsafe','unsafe']

    rec_model = svm.SVC()
    rec_model.fit(data, s)

    badLinks = []
    for link in links:
        values = [bitly(link), redirect(link), blog(link), ood(link, domain), endDomain(link), length(link), countDigits(link)]
        print(values)
        link_safety = rec_model.predict([values])
        data.append(values)
        s.append(link_safety[0])
        print(link,link_safety[0])
        if link_safety[0] == 'unsafe':
            badLinks.append(link)
        #if domain is the same but ending is different


    # link_safety = rec_model.predict([[5,2,5,2,5]])
    # data.append([5,2,5,2,5])
    # s.append(link_safety[0])
    
    return badLinks

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
    ending = urlparse(link).netloc[:-3]
    if checkEndings(ending) is not None:
        return checkEndings(ending)
    else:
        return 3

def checkEndings(s):
    if s == 'gov':
        return 5
    if s == 'edu' or s == 'com' or s == 'org':
        return 4
    if s == 'net':
        return 2
    if s == '.io' or s == '.bz':
        return 1
        

def blog(link:str):
    if 'blog' in link:
        return 2
    else:
        return 5

def countDigits(link):
    count = 0
    for ch in link:
        if ch.isdigit():
            count += 1
    if count > 50:
        return 1
    elif count > 30:
        return 3
    else:
        return 5

def length(link):
    count = len(link)
    if count > 100:
        return 1
    elif count > 80:
        return 3
    else:
        return 5

# print(length('http://www.get5rich.com/home/id=7283473897972374234/how_to_get_f4m0us839423948394/about.html'))

print(processData())