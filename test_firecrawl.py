from firecrawl import FirecrawlApp
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()  # take environment variables from .env.
API_KEY = os.getenv("FC_API_KEY")

app = FirecrawlApp(api_key=API_KEY)

# # Crawl a website:
# crawl_status = app.crawl_url(
#   'https://en.wikipedia.org/wiki/FOXA1', 
#   params={
#     'limit': 100, 
#     'scrapeOptions': {'formats': ['markdown']}
#   },
#   poll_interval=30
# )
# print(crawl_status)

# Scrape a website:
scrape_result = app.scrape_url('https://en.wikipedia.org/wiki/FOXA1', params={'formats': ['markdown']})

markdown_text = scrape_result['markdown']

# Save scrape result to markdown file
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_filename = f"scrape_result_{timestamp}.md"
with open(output_filename, 'w', encoding='utf-8') as f:
    f.write(markdown_text)
print(f"Saved scrape result to {output_filename}")