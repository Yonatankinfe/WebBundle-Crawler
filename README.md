# WebBundle-Crawler
🌐📦 Website scraper that bundles external CSS/JS into a single self-contained HTML file.
---

## Description  
A Python utility that converts web pages into portable HTML files by inlining all external stylesheets and scripts. Ideal for archiving, offline viewing, or analyzing website structure.

```python
# Key Features
- CSS/JavaScript external resource inlining
- Automatic URL resolution with urllib
- BeautifulSoup HTML parsing
- Response error handling
- Whitespace-formatted output
- Single-file output generation
---
```

## README.md

# 📂 WebBundle-Crawler

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Dependencies](https://img.shields.io/badge/dependencies-beautifulsoup4%20|%20requests-orange)


Website packaging tool for creating self-contained HTML documents.

## 🚀 Overview
![Workflow Diagram](https://via.placeholder.com/800x400.png?text=Scraping+Workflow)

1. **Input Processing** - Accepts website URL
2. **Resource Harvesting**:
   - Downloads linked CSS files
   - Fetches external JavaScript
3. **Asset Merging** - Inlines resources into HTML
4. **Output Generation** - Creates portable index.html

## 🛠️ Installation
```bash
git clone https://github.com/yourusername/WebBundle-Crawler.git
cd WebBundle-Crawler
pip install -r requirements.txt
```

## 📋 Requirements
```text
beautifulsoup4==4.12.3
requests==2.31.0
```

## 🖥️ Usage
```bash
python web_bundler.py
```
Sample workflow:
```text
Enter the website URL: https://example.com
Website scraped and saved as index.html with formatted CSS and JavaScript
```

## ⚙️ Technical Details

### Core Functions
```python
def scrape_website():
    # URL validation and request handling
    # BeautifulSoup DOM manipulation
    # CSS/JS resource inlining
    # File output management
```

### Resource Handling
```python
# CSS processing
css_url = urljoin(url, link['href'])
formatted_css = '\n'.join(line.strip() for line in css_response.text.splitlines())

# JavaScript handling
js_response = requests.get(js_url)
formatted_js = '\n'.join(line.strip() for line in js_response.text.splitlines())
```

## 💡 Customization Guide

### Modify Output Formatting
```python
# Change CSS formatting
formatted_css = css_response.text.strip()  # Keep original formatting

# Alter save location
with open("output/custom.html", "w") as file:
```

### Add Asset Types
```python
# Example: Inline images
for img in soup.find_all('img'):
    img_url = urljoin(url, img['src'])
    # Download and base64 encode
```

## ⚠️ Important Notes
1. Respect robots.txt and website scraping policies
2. May not handle dynamically loaded content (SPA sites)
3. Some CDN resources might block direct downloads
4. Output file size can grow large with many resources

## 🌟 Future Roadmap
- [ ] Support for WebP/Audio/Video assets
- [ ] Configurable formatting options
- [ ] CLI arguments for output path/name
- [ ] Cookie/Session support for authenticated sites
- [ ] Rate limiting and politeness controls

## 🤝 Contributing
1. Fork the repository
2. Create feature branch (`git checkout -b feature/improvement`)
3. Test changes thoroughly
4. Submit pull request with documentation updates

## 📜 License
MIT License - See [LICENSE](LICENSE) for details

> **Note**  
> Always obtain proper authorization before scraping websites. Use responsibly.
```