import pandas as pd
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from get_proxies import get_proxies
from get_name import get_name
import requests
import os.path
from os import path

def scraper(url, year):

    name = get_name(url)
    name = f'./storage/{name}{year}.csv'
    print(f"File exists: {name}: " + str(path.exists(name)))

    if path.exists(name):
        return name

    
    # df = pd.DataFrame([])
    # df.to_csv('./storage/1.csv', index=False)

    ua = UserAgent()

    stories_data = []

    core_url = url

    for month in range(1, 13):

        month = str(month)

        if len(month) == 1:
            month = f'0{month}'

        date = f'{month}/{year}'
        url = f'{core_url}/archive/{year}/{month}'
        print(url)

        headers = {'User-Agent': ua.random}
        
        page = requests.get(url, headers = headers)
        soup = BeautifulSoup(page.text, 'html.parser')

        stories = soup.find_all('div', class_='streamItem streamItem--postPreview js-streamItem')
        for story in stories:
            each_story = []

            author_box = story.find('div', class_='postMetaInline u-floatLeft u-sm-maxWidthFullWidth')
            author_url = author_box.find('a')['href']

            try:
                reading_time = author_box.find('span', class_='readingTime')['title']
            except:
                continue

            title = story.find('h3').text if story.find('h3') else '-'

            subtitle = story.find('h4').text if story.find('h4') else '-'

            if story.find('button', class_='button button--chromeless u-baseColor--buttonNormal'
                                            ' js-multirecommendCountButton u-disablePointerEvents'):

                claps = story.find('button', class_='button button--chromeless u-baseColor--buttonNormal'
                                                    ' js-multirecommendCountButton u-disablePointerEvents').text
            else:
                claps = 0

            if story.find('a', class_='button button--chromeless u-baseColor--buttonNormal'):
                responses = story.find('a', class_='button button--chromeless u-baseColor--buttonNormal').text
            else:
                responses = '0 responses'

            story_url = story.find('a', class_='button button--smaller button--chromeless u-baseColor--buttonNormal')[
                'href']

            reading_time = reading_time.split()[0]
            responses = responses.split()[0]

            story_page = requests.get(story_url)
            story_soup = BeautifulSoup(story_page.text, 'html.parser')

            sections = story_soup.find_all('section')
            story_paragraphs = []
            section_titles = []
            for section in sections:
                paragraphs = section.find_all('p')
                for paragraph in paragraphs:
                    story_paragraphs.append(paragraph.text)

                subs = section.find_all('h1')
                for sub in subs:
                    section_titles.append(sub.text)

            number_sections = len(section_titles)
            number_paragraphs = len(story_paragraphs)

            each_story.append(date)
            each_story.append(title)
            each_story.append(subtitle)
            each_story.append(claps)
            each_story.append(responses)
            each_story.append(author_url)
            each_story.append(story_url)
            each_story.append(reading_time)
            each_story.append(number_sections)
            each_story.append(section_titles)
            each_story.append(number_paragraphs)
            each_story.append(story_paragraphs)

            stories_data.append(each_story)

        print(f'{len(stories)} stories scraped on {date}.')

    columns = ['date', 'title', 'subtitle', 'claps', 'responses', 'author_url', 'story_url',
               'reading_time (mins)', 'number_sections', 'section_titles', 'number_paragraphs', 'paragraphs']

    df = pd.DataFrame(stories_data, columns=columns)

    df.to_csv(name, index=False)
    return name