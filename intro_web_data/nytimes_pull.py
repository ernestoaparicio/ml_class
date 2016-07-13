import urllib
import json

def main(api_key, category, label):
    print "category %s, label %s." % (category, label)
    content = []
    for i in range(0,5):
        # print "http://api.nytimes.com/svc/search/v2/articlesearch.json?fq=news_desk:('%s')&api-key=%s&page=%s" % (category, api_key, i)
        h = urllib.urlopen("http://api.nytimes.com/svc/search/v2/articlesearch.json?fq=news_desk:(\"%s\")&api-key=%s&page=%s" % (category, api_key, i))
        try:
            result = json.load(h)
            docs = result['response']['docs']

            for doc in docs:
                content.append(doc['lead_paragraph'])
                
        except ValueError:
            print "Malformed JSON: %s." % (data)
            continue #In the rare cases that JSON refuses to parse

    f = open(label, 'w')
    for line in content:
        try:
            f.write('%s\n' % line)
        except UnicodeEncodeError:
            pass
            
    f.close()

if __name__ == '__main__':
    #labels = ['adventure sports', 'arts & leisure','arts','automobiles', 'blogs','books','booming','business day', 'business', 'cars','culture','dining','fashion','financial','food','society','sports','style','technology']
    labels = ['arts','automobiles','blogs','books','booming','business','cars','culture','dining','fashion','financial','food','society','sports','style','technology']


    for label in labels:
        main("99c84481ba94487e9210f1fee86bc915", label.capitalize(),label)


