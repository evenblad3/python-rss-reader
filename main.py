import requests
import xml.etree.ElementTree as ET
from rich.console import Console

console = Console()

while True:
    rss_feed_url = input("Enter the URL of the feed, q to quit: ")
    if rss_feed_url.startswith("http://") or rss_feed_url.startswith("https://"):
        break
    elif rss_feed_url.lower().startswith("q") or rss_feed_url == "exit":
        exit()
    else:
        console.print("[bold red]Invalid URL!\n[/bold red]")
        continue
    # rss_feed_url = "https://msrc.microsoft.com/blog/categories/microsoft-threat-hunting/feed"

console.print("[green]\nLoading RSS...[/green]\n")

try:
    response = requests.get(rss_feed_url)
    if response.status_code == requests.codes.ok:
        root = ET.fromstring(response.content)
        
        def extract_text(element):
            if element is not None:
                return element.text
            return None
        
        items = root.findall('.//item')
        for item in items:
            title = extract_text(item.find('title'))
            link = extract_text(item.find('link'))
            pubDate = extract_text(item.find('pubDate'))
            description = extract_text(item.find('description'))
            console.print(f"[bold white]{title}[/bold white]")
            console.print(f"[underline blue]{link}[/underline blue]")
            console.print(f"[green]{pubDate}[/green]")
            print(f"{description}")
            print()
        
        
        console.print("\n[green]End of the feed.[/green]\n")
    else:
        console.print("[bold red]Invalid URL![/bold red]")

except Exception as e:
    print(e)
