import random
import time
from IPython.display import display, HTML

# Function to generate random ad URLs
def generate_random_ad_url():
    return "https://example.com/ad/" + str(random.randint(1, 100))

# Function to update ads every 30 seconds
def update_ads():
    left_ad_url = generate_random_ad_url()
    right_ad_url = generate_random_ad_url()
    ad_html = f'''
    <div class="ad-column">
        <a href="{left_ad_url}" target="_blank">Left Ad</a>
    </div>
    <div class="ad-column">
        <a href="{right_ad_url}" target="_blank">Right Ad</a>
    </div>
    '''
    display(HTML(ad_html))

# Simulate ad updates
for _ in range(3):  # Run this loop 3 times for demonstration
    update_ads()
    time.sleep(30)  # Wait for 30 seconds before updating ads again

print("Ads updated with random URLs.")
