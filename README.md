This project is a part of challenges (10 days challenge) that i took as an ethical hacker.

Day 6

Project 5

![scraper](https://user-images.githubusercontent.com/83413793/116855912-d4d6bc00-ac17-11eb-90c3-5561cc91dd99.png)

Scraper:

Scraper scrape endpoints from specific webpage. You can pass a webpage or a file containing multiple webpages links to scrape from . 

Installation:

                   git clone https://github.com/operationfalcon/Scraper.git
                   
                   cd Scraper
                   
                   pip3 install -r requirements.txt
                   
Usage :

![scraperusage](https://user-images.githubusercontent.com/83413793/116856365-adccba00-ac18-11eb-818f-17e3a64c2b5b.png)

                   python3 scraper.py -h
                   
                   python3 scraper.py -u <url> -o <output filename>
                   
Troubleshooting :

            If you are getting http connection error then do for loop to bypass the http connection error from request library
            
            or you can use custom proxy
