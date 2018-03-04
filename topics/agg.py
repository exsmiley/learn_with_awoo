import requests
from bs4 import BeautifulSoup
import pickle
import json
import tqdm


base_url = 'https://www.isidewith.com'


def get_all_links():
    r = requests.get('https://www.isidewith.com/polls')

    soup = BeautifulSoup(r.text, "html5lib")
    h2tags = soup.find_all('h2')

    data = {}

    for h2tag in tqdm.tqdm(h2tags, total=len(h2tags)):
        issue = h2tag.text
        data[issue] = {}

        polls = h2tag.find_next_sibling("div").find_all('div', class_='poll')

        # first one is outer div
        for poll in tqdm.tqdm(polls, total=len(polls)):
            try:
                link = poll.find('a', href=True)['href']
                topic = poll.find('p').text
                question = poll.find('p', class_='question').text
                yes = int(poll.find('div', class_='yes').text.split()[0])
                no = int(poll.find('div', class_='no').text.split()[0])
                votes = int(poll.find('div', class_='count').text.split()[0].replace(',', ''))

                # scrape description of topic
                inner = BeautifulSoup(requests.get(base_url + link).text, 'html5lib')
                desc = inner.find('div', class_='pollResultsBy', id='learn_more').find('div').text.strip()
                
                data[issue][topic] = {
                    'topic': topic, 'question': question,
                    'yes': yes, 'no': no,
                    'votes': votes, 'link': link,
                    'desc': desc
                }
            except:
                print link, 'failed'
                pass

    with open('raw_data.json', 'w') as outfile:
        json.dump(data, outfile)

def load_data():
    with open('raw_data.json') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':

    data = load_data()

    things = 0
    derp = {}

    for k, v in data.iteritems():
        things += len(v)
        derp[k] = len(v)

        print k, len(v)



