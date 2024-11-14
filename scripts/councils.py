import requests
from bs4 import BeautifulSoup
import re
import json

def main(id, filename):
    url = f"https://www.newadvent.org/fathers/{id}.htm"
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    canon_objects = []
    pattern = re.compile(r"Canon (\d+)")
    for h2_tag in soup.find_all('h3'):
        match = pattern.match(h2_tag.text.strip())
        if match:
            canon_number = match.group(1)
            p_tag = h2_tag.find_next('p')  
            
            if p_tag:
                for a_tag in p_tag.find_all('a'):
                    a_tag.insert_before("‎")
                    a_tag.insert_after("‎")
                    a_tag.unwrap()
                canon_text = ''.join(p_tag.stripped_strings)

                canon_object = {
                    "number": canon_number,
                    "text": canon_text
                }
                canon_objects.append(canon_object)

    with open(f'../data/councils/{filename}.json', 'w') as json_file:
        json.dump(canon_objects, json_file, indent=4)

main(3805, "anthioch")