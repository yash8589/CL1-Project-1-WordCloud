from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

urls = ["https://en.wikipedia.org/wiki/English_Wikipedia","https://en.wikipedia.org/wiki/Astrobiology","https://en.wikipedia.org/wiki/Rare_Earth_hypothesis","https://en.wikipedia.org/wiki/Giant-impact_hypothesis",
        "https://en.wikipedia.org/wiki/History_of_Earth","https://en.wikipedia.org/wiki/Ozone_layer","https://en.wikipedia.org/wiki/Great_Oxidation_Event","https://en.wikipedia.org/wiki/Origin_of_the_Moon",
        "https://en.wikipedia.org/wiki/Geology_of_the_Moon","https://en.wikipedia.org/wiki/Geological_history_of_Earth","https://en.wikipedia.org/wiki/Future_of_Earth","https://en.wikipedia.org/wiki/Plate_reconstruction",
        "https://en.wikipedia.org/wiki/Plate_tectonics","https://en.wikipedia.org/wiki/Atmospheric_circulation","https://en.wikipedia.org/wiki/Geodynamics","https://en.wikipedia.org/wiki/Molecular_biology","https://en.wikipedia.org/wiki/Biophysics","https://en.wikipedia.org/wiki/Biochemistry",
        "https://en.wikipedia.org/wiki/Chemistry","https://en.wikipedia.org/wiki/Astronomy","https://en.wikipedia.org/wiki/Sun","https://en.wikipedia.org/wiki/Black_hole","https://en.wikipedia.org/wiki/Electromagnetic_radiation","https://en.wikipedia.org/wiki/Star",
        "https://en.wikipedia.org/wiki/Civilization","https://en.wikipedia.org/wiki/Giza_pyramid_complex","https://en.wikipedia.org/wiki/New_Kingdom_of_Egypt","https://en.wikipedia.org/wiki/Great_Wall_of_China",
        "https://en.wikipedia.org/wiki/Machu_Picchu","https://en.wikipedia.org/wiki/Peru","https://en.wikipedia.org/wiki/El_Castillo,_Chichen_Itza","https://en.wikipedia.org/wiki/Chichen_Itza",
        "https://en.wikipedia.org/wiki/Tikal","https://en.wikipedia.org/wiki/Notre-Dame_de_Paris","https://en.wikipedia.org/wiki/France","https://en.wikipedia.org/wiki/England","https://en.wikipedia.org/wiki/India",
        "https://en.wikipedia.org/wiki/Christendom","https://en.wikipedia.org/wiki/Western_culture","https://en.wikipedia.org/wiki/Greco-Roman_world","https://en.wikipedia.org/wiki/Classical_antiquity",
        "https://en.wikipedia.org/wiki/Americas","https://en.wikipedia.org/wiki/China","https://en.wikipedia.org/wiki/United_States","https://en.wikipedia.org/wiki/Brazil","https://en.wikipedia.org/wiki/Bangladesh",
        "https://en.wikipedia.org/wiki/Japan","https://en.wikipedia.org/wiki/Mexico","https://en.wikipedia.org/wiki/Philippines","https://en.wikipedia.org/wiki/Vietnam","https://en.wikipedia.org/wiki/Germany",
        "https://en.wikipedia.org/wiki/Spain","https://en.wikipedia.org/wiki/Argentina","https://en.wikipedia.org/wiki/Canada","https://en.wikipedia.org/wiki/Poland","https://en.wikipedia.org/wiki/Malaysia",
        "https://en.wikipedia.org/wiki/Nepal","https://en.wikipedia.org/wiki/Madagascar","https://en.wikipedia.org/wiki/North_Korea","https://en.wikipedia.org/wiki/Cuba","https://en.wikipedia.org/wiki/Europe",
        "https://en.wikipedia.org/wiki/Czech_Republic","https://en.wikipedia.org/wiki/Asia","https://en.wikipedia.org/wiki/Australia","https://en.wikipedia.org/wiki/Antarctica","https://en.wikipedia.org/wiki/Arctic",
        "https://en.wikipedia.org/wiki/Hungary","https://en.wikipedia.org/wiki/United_Arab_Emirates","https://en.wikipedia.org/wiki/Austria","https://en.wikipedia.org/wiki/Switzerland","https://en.wikipedia.org/wiki/Hong_Kong","https://en.wikipedia.org/wiki/Lebanon",
        "https://en.wikipedia.org/wiki/Denmark","https://en.wikipedia.org/wiki/Singapore","https://en.wikipedia.org/wiki/Central_African_Republic","https://en.wikipedia.org/wiki/Finland","https://en.wikipedia.org/wiki/Slovakia","https://en.wikipedia.org/wiki/Norway"]
        
for url in urls:
    file = urlopen(url)
    source = file.read()

    soup = BeautifulSoup(source,'html.parser')
    soup

    paras = []
    for para in soup.find_all('p'):
        paras.append(str(para.text))

    # Extract text from para headers
    heads = []
    for head in soup.find_all('span', attrs={'mw-headline'}):
        heads.append(str(head.text))

    # Interleave paras & headers
    text = [val for pair in zip(paras, heads) for val in pair]
    text = ' '.join(text)

    # Drop footnote superscripts in brackets
    text = re.sub(r"\[.*?\]+", '', text)

    # Replace '\n' (a new line) with '' and end the string at $1000.
    text = text.replace('\n', '')[:-11]
    print(text)