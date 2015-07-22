import json, csv, os

file = open("playground.txt", encoding = "utf-8")
data = open("data.csv", "w", encoding = "utf-8")

writer = csv.writer(data, delimiter = "\t", lineterminator='\n')


def main(file):
    writer.writerow(["class", "title", "clicks", "urls"])
    n = file.read().splitlines()[1:]
    for i in range(len(n)):
        parser(n[i])
    data.close()
    return

def parser(json_object):
    enc = 0
    query = json.loads(json_object)[u'query'].get('qnorm')
    clicks = json.loads(json_object)[u'clicks']
    links = []
    for click in clicks:
        link = click.get("link")
        links.append(link)
    urls = json.loads(json_object)[u'urls']
    for url in urls:
        if ("wikipedia" in url) or ("dic.academic" in url):
            enc = 1
    writer.writerow([enc, query, links, urls])

main(file)
