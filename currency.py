import streamlit as st
import requests  # ✅ Fixed import

st.title("Currency Converter")

# Input fields for currency conversion
from_currency = st.text_input("Enter the currency you'd like to convert from:", "USD").upper()
to_currency = st.text_input("Enter the currency you'd like to convert to:", "EUR").upper()
amount = st.number_input("Enter the amount of money:", value=1.0)

# Convert button
if st.button("Convert"):
    try:
        # API request to get exchange rates
        response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{from_currency}")
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        data = response.json()

        # Check if the target currency exists in the API response
        if to_currency in data['rates']:
            converted_amount = amount * data['rates'][to_currency]
            st.success(f"💰 {amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")
        else:
            st.error("❌ Invalid 'to' currency code.")

    except requests.exceptions.RequestException as e:
        st.error(f"❌ Error fetching exchange rates: {e}")
    except KeyError:
        st.error("❌ Invalid 'from' currency code or API error.")
    except ValueError:
        st.error("❌ Invalid input. Please enter a valid number for the amount.")
    except Exception as e:
        st.error(f"❌ An unexpected error occurred: {e}")

# import requests 
# from_currency = str(input("Enter in the currency you'd like to convert to:")) .upper()

# to_currency = str( 
#     input("Enter in the currency you'd like to convert  to:")) .upper()

# amount = float(input("Enter in the  amount of money: "))
# response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{from_currency}")
# print(response.status_code)


# print(f"{amount}  {from_currency}is {response .json()['rates'][to_currency]} {to_currency}") 