import os
import csv
import requests
import json
import os


# # ... (Code précédent inchangé)

# def download_files(ti_folder):
#     # ... (Code précédent inchangé)
#     print("\n")
#     return all_files_downloaded  # Retourner la valeur de all_files_downloaded


def download_files(ti_folder):

    ti_feed = os.path.expanduser(os.path.join(ti_folder, "TI_feeds.csv"))
    db_size = sum(1 for line in open(ti_feed) if line.startswith("https"))
    feed_folder = os.path.expanduser(os.path.join(ti_folder, "feed"))
    all_files_downloaded = True

    if len(os.listdir(feed_folder)) < db_size:
        print("Filling DB")
        with open(ti_feed) as csvfile:
            reader = csv.reader(csvfile)
            for link, *_ in reader:
                if link.startswith("https"):
                    file_name = os.path.join(feed_folder, os.path.basename(link))
                    if not os.path.exists(file_name):
                        response = requests.get(link)
                        if response.status_code == 200:
                            with open(file_name, "wb") as f:
                                f.write(response.content)
                        else:
                            all_files_downloaded = False
                            print(f"Failed to download file from link: {link}")
                            break  # Exit the loop immediately if any download fails
        print("\n")
    return all_files_downloaded

