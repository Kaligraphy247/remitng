from bs4 import BeautifulSoup as bs
from dotenv import load_dotenv
import os, time, datetime
import requests
import schedule

load_dotenv()
SOUP_DIR = os.environ.get("SOUP_DIR")
SOUP_URL = os.environ.get("SOUP_URL")
# print("Soup Dir: ", SOUP_DIR, "\nSoup Url: ", SOUP_URL) # debug

# functions
def cache_soup_name_datetime(filename: str) -> None:
    """Generates a filename appended with a
    datetime to sort the latest soup_file
    """
    now = datetime.datetime.now()
    date_time = now.strftime("%m-%d-%Y-%H-%M-%S")
    new_filename = f"{filename}-{date_time}.html"
    # print(new_filename) # debug
    return new_filename


# print(cache_soup_name_datetime(filename=f"{SOUP_DIR}/text.html"))
def cache_source_soup(url: str):
    """Creates a local copy of the source-soup to\n
    prevent downtime or just have a backup during source's downtime.
    """
    main_soup = requests.get(url).text
    cached_soup = cache_soup_name_datetime(f"{SOUP_DIR}/new_soup")
    with open(cached_soup, "w", encoding="utf-8") as f:
        cached_soup = f.write(main_soup)


# cache_source_soup(url=SOUP_URL)



def get_current_soup(dir: str) -> str:
    """Gets the current soup from target soup url"""
    current_soup = os.listdir(dir)
    temp_dir_list = []
    for soup in current_soup:
        part_a = soup.split("p-")
        part_b = part_a[1]
        part_b = part_b.split(".html")[0]
        temp_dir_list.append(part_b)
    # print(max(temp_dir_list))
    for i in current_soup:
        if i.__contains__(max(temp_dir_list)):
            result = i
            # print("this is m: ", i)
    return f"{SOUP_DIR}/{result}"

# print(get_current_soup(SOUP_DIR))


def delete_old_cached_soup():
    """Deletes old soup files"""
    current_soup = os.listdir(SOUP_DIR)
    c = get_current_soup(dir=SOUP_DIR)
    c = os.stat(c).st_atime
    for file in current_soup:
        file = f"{SOUP_DIR}/{file}"
        file_atime = os.stat(file).st_atime
        if file_atime < c:
            print("old - ", file)  # debug
            os.remove(file)
        else:
            return "Nothing to clear at this time"


def run_soup():
    """Does all the needfull tasks"""
    four_days = 86400 * 4
    schedule.every().day.at("09:30").do(cache_source_soup, url=SOUP_URL)
    # schedule.every(5).seconds.do(cache_soup_name_datetime, "newsoup")
    schedule.every(four_days).seconds.do(delete_old_cached_soup) 

    while True:
        schedule.run_pending()
        time.sleep(1)



print("Site is running, no issues so far")
cached_soup = get_current_soup(dir=SOUP_DIR)

with open(cached_soup, "r", encoding="utf-8") as f:
    doc_file = bs(f, "html.parser")

# # print(doc_file)
tags = doc_file.find_all("table")
# USD black market prices
current_date_usd = tags[1].find_all("td")[4]
selling_rate_usd = tags[1].find_all("td")[6]
buying_rate_usd  = tags[1].find_all("td")[7]
print(current_date_usd.string, selling_rate_usd.string, buying_rate_usd.string)

# EUR black market prices
current_date_eur = tags[1].find_all("td")[12].string
selling_rate_eur = tags[1].find_all("td")[14].string
buying_rate_eur  = tags[1].find_all("td")[15].string
print(current_date_eur.string, selling_rate_eur.string, buying_rate_eur.string)


# if __name__ == "__main__":
#     run_soup()
