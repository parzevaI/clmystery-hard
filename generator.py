from faker import Faker
from tabulate import tabulate


fake = Faker()

# Generate a thousand random searches
searches = []
for _ in range(15000):
    ip_address = fake.ipv4()
    site_url = fake.url()
    access_time = fake.date_time_this_decade()

    searches.append((ip_address, site_url, access_time))


file = open('searches', 'a')
file.write(tabulate(sorted(searches, key=lambda x: x[2])))
file.close()

