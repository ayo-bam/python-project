import requests

def get_naira_to_dollar():
    api_url = "https://openexchangerates.org/api/latest.json"
    app_id = "YOUR_APP_ID"  # You need to register for an API key at Open Exchange Rates
    response = requests.get(f"{api_url}?app_id={app_id}")
    data = response.json()
    naira_to_dollar = data["rates"]["NGN"]
    return naira_to_dollar

def get_rate_for_date(date):
    api_url = f"https://openexchangerates.org/api/historical/{date}.json"
    app_id = "YOUR_APP_ID"
    response = requests.get(f"{api_url}?app_id={app_id}")
    data = response.json()
    naira_to_dollar = data["rates"]["NGN"]
    return naira_to_dollar

# Example usage:
print(f"Today's Naira to Dollar rate: {get_naira_to_dollar()}")
print(f"Rate on 2022-01-01: {get_rate_for_date('2022-01-01')}")
