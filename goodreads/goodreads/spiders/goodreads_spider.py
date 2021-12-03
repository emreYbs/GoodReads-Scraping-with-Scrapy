# https://github.com/emreYbs
# -*- coding: utf-8 -*-


import scrapy


class GoodreadsSpiderItem(scrapy.Item):
    source = scrapy.Field()
    title = scrapy.Field()
    length = scrapy.Field()
    author = scrapy.Field()
    likes = scrapy.Field()
    tags = scrapy.Field()

class GoodreadsSpider(scrapy.Spider):
    name = 'quotes'
    page_number = 2
    page_number_infosec = 2
    page_number_hacking= 2
    page_number_computer_science = 2
    page_number_security = 2
    allowed_domains = ['goodreads.com']
    start_urls = ['https://www.goodreads.com/quotes/tag/infosec', 'https://www.goodreads.com/quotes/tag/hacking', 
    'https://www.goodreads.com/quotes/tag/computer+science', 'https://www.goodreads.com/quotes/tag/security']

    def parse(self, response):
        items = GoodreadsSpiderItem()
        
        if 'computer+science' in response.url:
            source = 'computer+science'
        elif 'hacking' in response.url:
            source = 'hacking'
        elif 'infosec' in response.url:
            source = 'infosec'
        else:
            source = 'security'

        all_div_quotes = response.css('div.quoteDetails')

        for quotes in all_div_quotes:
            quote_title = quotes.css('div.quoteText::text').extract()
            quote_author = quotes.css('div.quoteText span::text').extract()
            quote_likes = quotes.css(
                'div.quoteFooter div.right a.smallText::text').extract()
            quote_tags = quotes.css(
                'div.quoteFooter div.greyText.smallText.left a::text').extract()

            items['source'] = source
            title_trim_newLine = quote_title[0].replace('\n', '')
            title = title_trim_newLine.strip('\"')
            items['title'] = title
            items['length'] = len(quote_title[0])
            author_trim_comma = quote_author[0].replace(',', '')
            author = author_trim_comma.replace('\n', '')
            items['author'] = author
            likes = quote_likes[0].split()
            items['likes'] = likes[0]
            items['tags'] = quote_tags[0]

            yield items

        next_page = 'https://www.goodreads.com/quotes/tag/computer+science' + str(GoodreadsSpider.page_number)
        if GoodreadsSpider.page_number < 101:
        	GoodreadsSpider.page_number += 1
        	yield response.follow(next_page, callback=self.parse)


        next_page_hacking = 'https://www.goodreads.com/quotes/tag/hacking' + str(GoodreadsSpider.page_number_hacking)
        if GoodreadsSpider.page_number_hacking  < 101:
            GoodreadsSpider.page_number_hacking  += 1
            yield response.follow(next_page_hacking , callback=self.parse)


        next_page_infosec = 'https://www.goodreads.com/quotes/tag/infosec' + str(GoodreadsSpider.page_number_infosec)
        if GoodreadsSpider.page_number_infosec < 101:
            GoodreadsSpider.page_number_infosec += 1
            yield response.follow(next_page_infosec, callback=self.parse)


        next_page_security = 'https://www.goodreads.com/quotes/tag/security' + str(GoodreadsSpider.page_number_security)
        if GoodreadsSpider.page_number_security < 101:
            GoodreadsSpider.page_number_security += 1
            yield response.follow(next_page_security, callback=self.parse)
