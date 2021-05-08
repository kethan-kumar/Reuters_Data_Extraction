from RegularExpression import regular_expression


class CleaningData:

    def clean_news_articles(self, news_articles):
        print("Cleaning news articles ...")
        for key in news_articles.keys():
            if type(news_articles.get(key)) == str and (key != 'DATE' and key != 'created_at'):
                news_articles[key] = regular_expression(news_articles.get(key))

            elif type(news_articles.get(key)) == dict:
                self.clean_news_articles(news_articles.get(key))