import requests
from bs4 import BeautifulSoup
import re

def get_website_details(url):
    # Send a GET request to the website
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content
        soup = BeautifulSoup(content, 'html.parser')

        #  list of latest social media domains
        # can add more to have the more searching domaim
        social_media_domains = [
            'facebook\.com',
            'linkedin\.com',
            'twitter\.com',
            'instagram\.com'
            # Add more social media domains here
        ]

        # regular expression pattern for social media links
        social_pattern = r'(https?://(www\.)?(' + '|'.join(social_media_domains) + ')/[^\s/$.?#].[^\s]*)'

        # Find social media links using the constructed pattern
        social_links = [match[0] for match in re.findall(social_pattern, content.decode())]

          # email addresses using regular expressions
        email_addresses = re.findall(r'\S+@(gmail\.com|yahoo\.com|hotmail\.com)', content.decode())

        # To find Find Indian contact numbers
        # we can add further regular expression of the contries contact number
        # this will have the more expansion of the search area

        contact_numbers = re.findall(r'(\+91\s?\d{10})', content.decode())  # Indian phone number format

        return social_links, email_addresses, contact_numbers
    else:
        return [], [], []


user_input = input("Enter the website URL: ")
social_links, email_addresses, contact_numbers = get_website_details(user_input)


print("Social links -")
for link in social_links:
    print(link)

print("\nEmail/s -")
for email in email_addresses:
    print(email)

print("\nContact:")
for contact in contact_numbers:
    print(contact)
