import re

from CleaningData import CleaningData


class ReutersNewsArticles:

    def __init__(self, filename):
        print("Reuters object initialization ...")
        self.tags = ['DATE', 'TOPICS', 'PLACES', 'PEOPLE', 'ORGS', 'EXCHANGES', 'COMPANIES', 'UNKNOWN', 'TITLE',
                           'DATELINE', 'BODY']
        self.tag_regex = "<[a-zA-Z]+>"
        file_object = open("reuter_articles/" + filename, "r")
        print("Reading data from reuters file ...")
        self.reuters_uncleaned_data = file_object.read()
        self.reuters_uncleaned_data = self.reuters_uncleaned_data.replace('\n', '')
        self.end_tag = re.findall('</[A-Z]+>', self.reuters_uncleaned_data)

        for tag_name in self.end_tag:
            if tag_name != "</D>": self.reuters_uncleaned_data = re.sub(tag_name, tag_name + '\n', self.reuters_uncleaned_data)

    def scan_article(self):
        print("Scanning articles for extracting data ...")
        documents_list = []
        news_article_dictionary = {}

        for statement in self.reuters_uncleaned_data.split('\n'):
            tag_found = re.search(r'<[A-Z]+.>.*</[A-Z]+>', statement)
            if tag_found:
                matched_tag = re.search(self.tag_regex, tag_found.string)
                if matched_tag:
                    key = re.sub("[<>]", "", matched_tag.group())
                    if key in self.tags:
                        value = re.sub("</?[a-zA-Z]+>", "", tag_found.group())
                        news_article_dictionary[key] = value

            if statement.find("</REUTERS") != -1:
                document = dict(news_article_dictionary)
                if len(news_article_dictionary.keys()) > 0:
                    documents_list.append(document)
                news_article_dictionary = {}

        print("Cleaning Data...")
        dictionary_cleaning = CleaningData()
        for doc in documents_list:
            dictionary_cleaning.clean_news_articles(doc)
        return documents_list
