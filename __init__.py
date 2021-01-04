from autoscraper.auto_scraper import AutoScraper

url = 'https://clutch.co/agencies/digital-design'


# Scraping the names of the digital design companies
wanted_list_names = ["Design In DC"]


scraper = AutoScraper()
result_names = scraper.build(url, wanted_list_names)
print(result_names)



# Scraping the prices for each project / charge per project 
wanted_list_price = ["$10,000"]


scraper = AutoScraper()
result_prices = scraper.build(url, wanted_list_price)
print(result_prices)


# Scraping the Hourly Rate
wanted_list_HR = ["$100 - $149 / hr"]


scraper = AutoScraper()
result_HR = scraper.build(url, wanted_list_HR)
print(result_HR)



# Scraping the Size 
wanted_list_size = ["2 - 9"]


scraper = AutoScraper()
result_size = scraper.build(url, wanted_list_size)
print(result_size)

# Scraping the location 
wanted_list_location = ["Washington, DC"]


scraper = AutoScraper()
result_location = scraper.build(url, wanted_list_location)
print(result_location)

# Scraping the Main Focus 
wanted_list_focus = ["50% Web Design"]


scraper = AutoScraper()
result_focus = scraper.build(url, wanted_list_focus)
print(result_focus)


