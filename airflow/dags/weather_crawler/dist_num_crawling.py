import requests
import json

def get_test(url):
    dist = []
    code = []
    print(url)
    req = requests.get(url)
    req.encoding = 'utf-8'
    rDict = json.loads(req.text)
    print(rDict)
    print(type(rDict[0]))
    for test in rDict:
        dist.append(test.get('value'))
        code.append(test.get('code'))
    root = {}
    
    with open('root_dist.txt', 'w', encoding='euc-kr') as rd:
        for i in range(len(dist)):
            rd.writelines(dist[i]+' : '+code[i]+'\n')
            root[dist[i]] = code[i]
    return root

def get_test2(url, root):
    dist = []
    code = []
    keys = list(root.keys())
    values = list(root.values())
    mdl = {}
    with open('mdl_dist.txt', 'w', encoding='euc-kr') as md:
        for i in range(len(root)):
            req = requests.get(url % (values[i]))
            req.encoding = 'utf-8'
            rDict = json.loads(req.text)
            for test in rDict:
                dist.append(test.get('value'))
                code.append(test.get('code'))
                md.writelines(keys[i]+', '+ test.get('value')+' : '+test.get('code')+'\n')
            mdl['root'] = keys[i]
            mdl[dist[i]] = code[i]
    return mdl

def get_test3(url):
    dists = []
    codes = []
    dists_lf = []
    codes_lf = []
    with open('mdl_dist.txt', 'r') as md:
        text = md.readlines()
        for obj in text:
            dists.append(obj.split(' : ')[0])
            codes.append(obj.split(' : ')[1].split('\n')[0])
    
    with open('lf_dist.txt', 'w', encoding='euc-kr') as ld:
        for i in range(len(codes)):
            req = requests.get(url % (codes[i]))
            req.encoding = 'utf-8'
            rDict = json.loads(req.text)
            for test in rDict:
                dists_lf.append(test.get('value'))
                codes_lf.append(test.get('code'))
                ld.writelines(dists[i]+', '+test.get('value')+' : '+test.get('code') + '\n')
    return
url = 'http://www.kma.go.kr/DFSROOT/POINT/DATA/top.json.txt'
t = get_test(url)
url = 'http://www.kma.go.kr/DFSROOT/POINT/DATA/mdl.%s.json.txt'
t = get_test2(url, t)
url = 'http://www.kma.go.kr/DFSROOT/POINT/DATA/leaf.%s.json.txt'
t = get_test3(url)