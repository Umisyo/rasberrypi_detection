from icrawler.builtin import GoogleImageCrawler

crawler = GoogleImageCrawler(storage={"root_dir": "images"})
search_words = ["セキセイインコ", "セキセイインコ 青", "セキセイインコ 水色", "セキセイインコ 黒"]

crawler.crawl(keyword="セキセイインコ 青", max_num=10)
