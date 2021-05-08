from src.persistence.MongoDB_DAO import MongoDB_DAO
from src.business_logic.ReutersNewsArticles import ReutersNewsArticles

if __name__ == '__main__':
    news_articles = ['reut2-009.sgm', 'reut2-014.sgm']
    mongoDb = MongoDB_DAO("ReuterDb")
    for filename in news_articles:
        print("Cleaning news articles ...")
        reuters = ReutersNewsArticles(filename)
        documents = reuters.scan_article()
        mongoDb.save_multiple_records(documents, filename)