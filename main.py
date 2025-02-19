# Python file for scraping any dom website

#used for only education purposes 
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scrape_website():
    url = input("Enter the website URL: ")
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the website: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract and format CSS
    for link in soup.find_all('link', {'rel': 'stylesheet'}):
        css_url = urljoin(url, link['href'])
        try:
            css_response = requests.get(css_url)
            css_response.raise_for_status()
            formatted_css = '\n'.join(line.strip() for line in css_response.text.splitlines())
            style_tag = soup.new_tag("style")
            style_tag.string = formatted_css
            soup.head.append(style_tag)
            link.decompose()
        except requests.exceptions.RequestException:
            continue

    # Extract and format JavaScript
    for script in soup.find_all('script', {'src': True}):
        js_url = urljoin(url, script['src'])
        try:
            js_response = requests.get(js_url)
            js_response.raise_for_status()
            formatted_js = '\n'.join(line.strip() for line in js_response.text.splitlines())
            new_script = soup.new_tag("script")
            new_script.string = formatted_js
            soup.body.append(new_script)
            script.decompose()
        except requests.exceptions.RequestException:
            continue

    # Save to index.html
    with open("index.html", "w", encoding="utf-8") as file:
        file.write(str(soup.prettify()))

    print("Website scraped and saved as index.html with formatted CSS and JavaScript")

if __name__ == "__main__":
    scrape_website()