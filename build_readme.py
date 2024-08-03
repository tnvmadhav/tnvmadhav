import pathlib
import feedparser
import re
import requests
from datetime import datetime
import pytz

def rss_to_json(rss_url):
    feed = feedparser.parse(rss_url)
    feed_contents = []
    for entry in feed.entries:
        entry_data = {
            'title': entry.get('title', ''),
            'link': entry.get('link', ''),
            'published': entry.get('published', '')
        }
        feed_contents.append(entry_data)
    return feed_contents


def replace_chunk(content, marker, chunk, inline=False):
    r = re.compile(
        r"<!\-\- {} starts \-\->.*<!\-\- {} ends \-\->".format(marker, marker),
        re.DOTALL,
    )
    if not inline:
        chunk = "\n{}\n".format(chunk)
    chunk = "<!-- {} starts -->{}<!-- {} ends -->".format(marker, chunk, marker)
    return r.sub(chunk, content)


def to_utc(date_str):
    # Define the date format with timezone
    date_format = "%a, %d %b %Y %H:%M:%S %z"
    local_dt = datetime.strptime(date_str, date_format)
    utc_dt = local_dt.astimezone(pytz.utc)
    return utc_dt.isoformat()


if __name__ == "__main__":

    readme = pathlib.Path(__file__).parent.resolve() / "README.md"

    rewritten = readme.open().read()

    blog_json_list = rss_to_json("https://tnvmadhav.me/index.xml")
    feed_json_list = requests.get(
        "https://cpx.tnvmadhav.me/content/tnvmadhav/stream/",
    ).json()["content_list"]

    (
        guide_entries_md_list, blog_entries_md_list,
        til_entries_md_list, feed_entries_md_list,
    ) = [], [], [], []

    for feed_json in feed_json_list:
        feed_entries_md_list.append(
            f"{feed_json['text']} -- {feed_json['updated_at']}"
        )

    for blog_json in blog_json_list:
        blog_match = re.findall(r'https://tnvmadhav.me/blog/', blog_json["link"])
        if blog_match:
            blog_entries_md_list.append(f'[{blog_json["title"]}]({blog_json["link"]}) -- {to_utc(blog_json["published"])}')
        guide_match = re.findall(r'https://tnvmadhav.me/guides', blog_json["link"])
        if guide_match:
            guide_entries_md_list.append(f'[{blog_json["title"]}]({blog_json["link"]}) -- {to_utc(blog_json["published"])}')
        til_match = re.findall(r'https://tnvmadhav.me/til', blog_json["link"])
        if til_match:
            til_entries_md_list.append(f'[{blog_json["title"]}]({blog_json["link"]}) -- {to_utc(blog_json["published"])}')

    guide_entries_md = "\n\n".join(guide_entries_md_list[:5])
    blog_entries_md =  "\n\n".join(blog_entries_md_list[:5])
    til_entries_md = "\n\n".join(til_entries_md_list[:5])
    feed_entries_md = "\n\n".join(feed_entries_md_list[:10])

    blog_entries_md += f"\n\nMore on [MY BLOG POSTS](https://tnvmadhav.me/blog/)"
    guide_entries_md += f"\n\nMore on [MY GUIDES](https://tnvmadhav.me/guides/)"
    til_entries_md += f"\n\nMore on [My TILS](https://tnvmadhav.me/til/)"

    rewritten = replace_chunk(rewritten, "blog", blog_entries_md)
    rewritten = replace_chunk(rewritten, "guide", guide_entries_md)
    rewritten = replace_chunk(rewritten, "til", til_entries_md)
    rewritten = replace_chunk(rewritten, "feed", feed_entries_md)

    readme.open("w").write(rewritten)
