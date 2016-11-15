# parlamentare2016.bec.ro scraper

####Initial setup:
- Go to the *right* folder 
- Create a virtual environment: `$ virtualenv venv`
- Activate the virtual environment: `$ source venv/bin/activate`
- Install the requirements: `$ pip install -r requirements.txt`

###Scrape it like you know it:
- Run the main script with: `python bec_scraper.py` and magic will happen  
- text_extractor dumps the UTF8 and ascii texts in two separate folders
- create_csv does a partial csv generation from the ascii texts

### TODO
- Use java -jar pdfbox-app-2.0.3.jar ExtractText pdfs/some.pdf output.txt 
