import argparse
from banner.banner import banner_design
from function import scrape_links_from_single_url, scrape_links_from_multiple_urls
import sys
banner=banner_design()



parser=argparse.ArgumentParser(description=banner, formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-u', '--url', help='source from which scraping should start')
parser.add_argument('-f', '--file', help='file containig urls from which scraper will start crawling links')
parser.add_argument('-o', '--output', help='output filename in which results will be stored')
args=parser.parse_args()





if len(sys.argv) == 5 and sys.argv[2]==args.url and sys.argv[4]==args.output:
    scrape_links_from_single_url(args.url, args.output)
