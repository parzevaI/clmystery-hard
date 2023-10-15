from faker import Faker
from tabulate import tabulate
import random as rm

# NEED TO REGENERATE THE SEARCHES FILE SO IT CONTAINS A WHOLE BUNCH OF THE EMAIL 
# PROVIDER SITE SO THE PLAYER HAS TO CHECK THE TIME IT WAS SENT

fake = Faker()

# Generate random search history data
ip_addresses = [fake.ipv4() for _ in range(200)]
urls = [fake.url() for _ in range(200)] # + ["https://google.com/mail"]

# List it
searches = [(
    rm.choice(ip_addresses),
    rm.choice(urls),
    fake.date_time_this_year(),
) for _ in range(13000)]

# Put output in file
file = open('searches', 'a')
file.write(tabulate(sorted(searches, key=lambda x: x[2])))
file.close()
