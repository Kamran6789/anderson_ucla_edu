from datetime import datetime

import pyairtable
import scrapy
from scrapy.crawler import CrawlerProcess


class AndersonUclaWinnersSpider(scrapy.Spider):
    name = "anderson_ucla_winners"
    start_urls = ["https://www.anderson.ucla.edu/knapp-venture-competition"]

    def parse(self, response):
        items = {}
        items['competition'] = response.css('.local-nav-btn ::text')[0].extract()
        items['lastupdate'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        items["year"] = response.css('.title-block ::text')[7].extract().replace('Winners', '')
        items['winner business'] = response.css('h4+ p strong::text')[0].extract()
        items['winner participants'] = response.css('p+ p::text')[3].extract().replace(';', ',').replace('\xa0',
                                                                                                         '').replace(
            '\n\t\t\t', '') + response.css('p+ p::text')[4].extract().replace('\n\t\t\t', '').replace(';', ',') + ' ' + \
                                       response.css('p+ p::text')[5].extract().replace('\n\t\t\t', '').replace(';', '')
        items['2nd place business'] = response.css('h4+ p strong::text')[1].extract()
        items['2nd place participants'] = response.css('p+ p::text')[6].extract().replace('\xa0', '').replace(';',
                                                                                                              ',').replace(
            '\n\t\t\t', '') + ' ' + response.css('p+ p::text')[7].extract().replace('\n\t\t\t', '').replace(';', ',')
        items['3rd place business'] = response.css('h4+ p strong::text')[2].extract()
        items['3rd place participants'] = response.css('p+ p::text')[8].extract().replace(':', '').replace('\xa0',
                                                                                                           '').replace(
            ';', ',').replace('\n\t\t\t', '') + ' ' + response.css('p+ p::text')[9].extract().replace('\n\t\t\t',
                                                                                                      '').replace(';',
                                                                                                                  ',')

        remaining_pages_links = response.css('.menu__link--level-1::attr(href)')[3].extract()

        table.create(items)
        yield items

        yield response.follow(remaining_pages_links, callback=self.parse_remaining_pages)

    def parse_remaining_pages(self, response):
        yield from extract_info_2020(response)
        yield from extract_info_2019(response)
        yield from extract_info_2018(response)
        yield from extract_info_2017(response)
        yield from extract_info_2016(response)
        yield from extract_info_2015(response)
        yield from extract_info_2014(response)


def extract_info_2020(response):
    items = {}
    items['competition'] = response.css('.local-nav-btn ::text')[0].extract()
    items['lastupdate'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    items["year"] = response.css('.title-block ::text')[7].extract().replace('Winners', '')
    items['lastupdate'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    items['year'] = '2020'
    items['winner business'] = response.css('p br+ strong::text , p+ strong ::text')[0].extract()
    items['2nd place business'] = response.css('p br+ strong::text , p+ strong ::text')[1].extract()
    items['3rd place business'] = response.css('p br+ strong::text , p+ strong ::text')[2].extract()
    items['winner participants'] = ''.join(response.css(
        ' div+ span::text, tr:nth-child(1) td > div::text, .alt-rows-lightgrey-border div+ div::text')[
                                               2].getall()).strip()
    items['2nd place participants'] = ''.join(response.css(
        ' div+ span::text, tr:nth-child(1) td > div::text, .alt-rows-lightgrey-border div+ div::text')[
                                                  3].getall()).strip()
    items['3rd place participants'] = ''.join(response.css(
        ' div+ span::text, tr:nth-child(1) td > div::text, .alt-rows-lightgrey-border div+ div::text')[
                                                  4].extract()).strip()
    table.create(items)
    yield items


def extract_info_2019(response):
    items = {}
    items['competition'] = response.css('.local-nav-btn ::text')[0].extract()
    items['lastupdate'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    items["year"] = response.css('.title-block ::text')[7].extract().replace('Winners', '')
    items['lastupdate'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    items['year'] = '2019'
    items['winner business'] = response.css('.e2ma-p-div+ .e2ma-p-div strong:nth-child(1)::text')[0].extract()
    items['2nd place business'] = response.css('.e2ma-p-div+ .e2ma-p-div strong:nth-child(1)::text')[1].extract()
    items['3rd place business'] = response.css('.e2ma-p-div+ .e2ma-p-div strong:nth-child(1)::text')[2].extract()
    items['winner participants'] = ''.join(
        response.css('.e2ma-p-div+ .e2ma-p-div .e2ma-style').css('span::text')[1].getall()).strip()
    items['2nd place participants'] = ''.join(
        response.css('.e2ma-p-div+ .e2ma-p-div .e2ma-style').css('span::text')[4:-17].getall()).strip()
    items['3rd place participants'] = ''.join(
        response.css('.e2ma-p-div+ .e2ma-p-div .e2ma-style').css('span::text')[11].getall()).strip()

    table.create(items)
    yield items


def extract_info_2018(response):
    items = {}
    items['competition'] = response.css('.local-nav-btn ::text')[0].extract()
    items['lastupdate'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    items["year"] = response.css('.title-block ::text')[7].extract().replace('Winners', '')
    items['lastupdate'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    items['year'] = '2018'
    items['winner business'] = response.css('.row-background-none .component-column-3 h5::text')[0].extract()
    items['2nd place business'] = response.css('.row-background-none .component-column-3 h5::text')[1].extract()
    items['3rd place business'] = response.css('.row-background-none .component-column-3 h5::text')[2].extract()
    items['winner participants'] = ''.join(
        response.css('h6+ p::text')[0].getall()).strip()
    items['2nd place participants'] = ''.join(
        response.css('h6+ p::text')[1].getall()).strip()
    items['3rd place participants'] = ''.join(
        response.css('h6+ p::text')[2].getall()).strip()
    table.create(items)
    yield items


def extract_info_2017(response):
    items = {}
    items['competition'] = response.css('.local-nav-btn ::text')[0].extract()
    items['lastupdate'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    items["year"] = response.css('.title-block ::text')[7].extract().replace('Winners', '')
    items['lastupdate'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    items['year'] = '2017'
    items['winner business'] = response.css('.row .col .pb-0 h5 ::text')[0].extract()
    items['2nd place business'] = response.css('.row .col .pb-0 h5 ::text')[1].extract()
    items['3rd place business'] = response.css('.row .col .pb-0 h5 ::text')[2].extract()
    items['winner participants'] = ''.join(
        response.css('h6+ p::text')[6].getall()).strip()
    items['2nd place participants'] = ''.join(
        response.css('h6+ p::text')[7].getall()).strip()
    items['3rd place participants'] = ''.join(
        response.css('h6+ p::text')[8].getall()).strip()
    table.create(items)
    yield items


def extract_info_2016(response):
    items = {}
    items['competition'] = response.css('.local-nav-btn ::text')[0].extract()
    items['lastupdate'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    items["year"] = response.css('.title-block ::text')[7].extract().replace('Winners', '')
    items['lastupdate'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    items['year'] = '2016'
    items['winner business'] = response.css('.row .fadeIn h5 ::text')[0].extract()
    items['2nd place business'] = response.css('.row .fadeIn h5 ::text')[1].extract()
    items['3rd place business'] = response.css('.row .fadeIn h5 ::text')[2].extract()
    items['winner participants'] = ''.join(
        response.css('h6+ p::text')[12].getall()).strip()
    items['2nd place participants'] = ''.join(
        response.css('h6+ p::text')[13].getall()).strip()
    items['3rd place participants'] = ''.join(
        response.css('h6+ p::text')[14].getall()).strip()
    table.create(items)
    yield items


def extract_info_2015(response):
    items = {}
    items['competition'] = response.css('.local-nav-btn ::text')[0].extract()
    items['lastupdate'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    items["year"] = response.css('.title-block ::text')[7].extract().replace('Winners', '')
    items['lastupdate'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    items['year'] = '2015'
    items['winner business'] = response.css('.row .fadeIn h5 ::text')[5].extract()
    items['2nd place business'] = response.css('.row .fadeIn h5 ::text')[6].extract()
    items['3rd place business'] = response.css('.row .fadeIn h5 ::text')[7].extract()
    items['winner participants'] = ''.join(
        response.css('h6+ p::text')[17].getall()).strip()
    items['2nd place participants'] = ''.join(
        response.css('h6+ p::text')[18].getall()).strip()
    items['3rd place participants'] = ''.join(
        response.css('h6+ p::text')[19].getall()).strip()
    table.create(items)
    yield items


def extract_info_2014(response):
    items = {}
    items['competition'] = response.css('.local-nav-btn ::text')[0].extract()
    items['lastupdate'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    items["year"] = response.css('.title-block ::text')[7].extract().replace('Winners', '')
    items['lastupdate'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    items['year'] = '2014'
    items['winner business'] = response.css('.row .fadeIn p ::attr(alt)')[0].extract()
    items['2nd place business'] = response.css('.row .fadeIn p ::attr(alt)')[1].extract()
    items['3rd place business'] = response.css('.row .fadeIn p ::attr(alt)')[2].extract()
    table.create(items)
    yield items


if __name__ == '__main__':
    api = pyairtable.Api('api-key')
    base = api.base('key')
    table = [v for v in base.tables() if v.name == 'Main Table'][0]
    process = CrawlerProcess()
    process.crawl(AndersonUclaWinnersSpider)
    process.start()
