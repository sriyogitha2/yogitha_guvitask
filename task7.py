#1)Using the URL https://restcountries.com/v3.1/all write a Python program which will do the following :-
1.) Using the OOPS concept for the following task.
2.) Use the Class Constructor for taking input the above mentioned URL for the task.
3. Create a Method that will Fetch all the JSON data from the URL mentioned above.
4.) Create a Method that will display the name of countries, currencies & currency symbols.
5.) Create a Method that will display all those countries which have DOLLAR as its currency.
6. Create a Method that will display all those countries which have EURO as its currency.


# Import the requests library
import requests

# Create a class named MyJSON 
class MyJSON:
    
    # This is the constructor method that runs when an object is created
    def __init__(self, url):
        self.url = url  # Save the URL that is passed when the object is created
        self.data = self.fetch_api_data()  # Fetch the data from the API and store it in 'self.data'

    # This method checks the API's status code to confirm if the request was successful
    def api_status_code(self):
        response = requests.get(self.url)  # Send a GET request to the URL
        return response.status_code  # Return the status code (e.g., 200 for success)

    # This method fetches the data from the API if the request is successful (status code 200)
    def fetch_api_data(self):
        if self.api_status_code() == 200:  # Check if the status code is 200 (successful request)
            return requests.get(self.url).json()  # Fetch the data from the API and return it as JSON
        else:
            return "ERROR - 404"  # If the request failed, return an error message

    # This method displays the name of countries along with their currencies and currency symbols
    def display_countries_and_currencies(self):
        if self.api_status_code() == 200:  # Check if the API request was successful
            for country in self.data:  # Loop through each country in the fetched data
                # Get the country name or set to "N/A" if not available
                country_name = country.get("name", {}).get("common", "N/A")
                
                # Get the currencies of the country (if available)
                currencies = country.get("currencies", {})
                
                # If the country has currencies, process them
                if currencies:
                    for currency_code, currency_info in currencies.items():  # Loop through the currencies
                        # Get the currency name and symbol, or set to "N/A" if not available
                        currency_name = currency_info.get("name", "N/A")
                        currency_symbol = currency_info.get("symbol", "N/A")
                        # Print the country name, currency name, and currency symbol
                        print(f"{country_name} , {currency_name} , {currency_symbol}")
                else:
                    # If no currency information is found for the country, print this
                    print(f"{country_name} , No currency info,N/A")

    # This method displays countries that use "Dollar" as their currency
    def display_countries_using_dollar(self):
        if self.api_status_code() == 200:  # Check if the API request was successful
            for country in self.data:  # Loop through each country in the fetched data
                currencies = country.get("currencies", {})  # Get the currency information of the country
                
                for currency_code, currency_info in currencies.items():  # Loop through each currency
                    # Get the currency name in lowercase for easy comparison
                    currency_name = currency_info.get("name", "").lower()
                    
                    # If the currency name contains "dollar", print the country name
                    if "dollar" in currency_name:
                        country_name = country.get("name", {}).get("common", "N/A")  # Get the country name
                        # Print the country name that uses Dollar as currency
                        print(f"{country_name}")

    # This method displays countries that use "Euro" as their currency
    def display_countries_using_euro(self):
        if self.api_status_code() == 200:  # Check if the API request was successful
            for country in self.data:  # Loop through each country in the fetched data
                currencies = country.get("currencies", {})  # Get the currency information of the country
                
                for currency_code, currency_info in currencies.items():  # Loop through each currency
                    # Get the currency name in lowercase for easy comparison
                    currency_name = currency_info.get("name", "").lower()
                    
                    # If the currency name contains "euro", print the country name
                    if "euro" in currency_name:
                        country_name = country.get("name", {}).get("common", "N/A")  # Get the country name
                        # Print the country name that uses Euro as currency
                        print(f"{country_name}")



# Create an object of the MyJSON class with the URL as an argument
json_object = MyJSON("https://restcountries.com/v3.1/all")

# Print the API status code to check if the request was successful (should print 200 if successful)
print(json_object.api_status_code())

# Print the raw JSON data fetched from the API
print(json_object.fetch_api_data())

# Call the display_countries_and_currencies method to display countries and their currencies
json_object.display_countries_and_currencies()

# Call the display_countries_using_dollar method to display countries that use "Dollar" as their currency
json_object.display_countries_using_dollar()

# Call the display_countries_using_euro method to display countries that use "Euro" as their currency
json_object.display_countries_using_euro()
________________________________


#2)Visit the URL https://www.openbrewerydb.org/ write a Python script which will do the following :-
1.) List the names of all breweries present in the states of Alaska, Maine and New York.
2.) What is the count of breweries in each of the states mentioned above?
3.) Count the number of types of breweries present in individual cities of the state mentioned above
4.) Count and list how many breweries have websites in the states of Alaska, Maine and New York.


import requests  # Import the requests library 

# Define the Myjson class that interacts with the Open Brewery DB API
class Myjson:
    def __init__(self, url):  # Constructor to initialize the URL of the API
        self.url = url  # Store the API URL

    def api_status_code(self):  # Method to check the status code of the API
        response = requests.get(self.url)  # Make a GET request to the URL
        return response.status_code  # Return the HTTP status code of the response

    def fetch_api_data(self):  # Method to fetch data from the API (without pagination)
        if self.api_status_code() == 200:  # Check if the API is available (status code 200)
            return requests.get(self.url).json()  # Fetch the data and return it as JSON
        else:
            return "ERROR - 404"  # If the API is not available, return an error message

    def fetch_api_data(self, page=1):  # Method to fetch data with pagination (default page=1)
        params = {'page': page}  # Set up pagination by passing the page number as a parameter
        if self.api_status_code() == 200:  # Check if the API is available (status code 200)
            response = requests.get(self.url, params=params)  # Make a GET request with pagination
            return response.json()  # Return the data as JSON
        else:
            return "Error - 404"  # If the API is not available, return an error message

    def count_breweries_by_state(self):  # Method to count the number of breweries by state
        if self.api_status_code() == 200:  # Check if the API is available (status code 200)
            breweries = self.fetch_api_data()  # Fetch the brewery data (first page by default)
            state_count = {}  # Initialize an empty dictionary to store the count of breweries by state
            for data in breweries:  # Loop through each brewery in the data
                state = data.get('state')  # Get the state of the current brewery
                if state in state_count:  # If the state is already in the dictionary
                    state_count[state] += 1  # Increment the count for that state
                else:
                    state_count[state] = 1  # Otherwise, initialize the count for that state
            return state_count  # Return the dictionary with the count of breweries by state
        else:
            return "ERROR - 404"  # If the API is not available, return an error message

    def count_breweries_with_website_on_state(self, states):  # Method to count breweries with websites in specific states
        if self.api_status_code() == 200:  # Check if the API is available (status code 200)
            breweries = self.fetch_api_data()  # Fetch the brewery data (first page by default)
            count = 0  # Initialize a counter for breweries with websites
            for brewery in breweries:  # Loop through each brewery in the data
                state = brewery.get('state')  # Get the state of the current brewery
                website = brewery.get('website_url')  # Get the website URL of the current brewery
                if state in states and website:  # If the state is in the specified list and the brewery has a website
                    count += 1  # Increment the counter for breweries with websites
            return count  # Return the total count of breweries with websites in the specified states
        else:
            return "ERROR - 404"  # If the API is not available, return an error message

    def list_brewery_name_by_state(self, states):  # Method to list the names of breweries in specific states
        if self.api_status_code() == 200:  # Check if the API is available (status code 200)
            brewery_name = []  # Initialize an empty list to store brewery names
            for page in range(1, 11):  # Loop through the first 10 pages of data (pagination)
                breweries = self.fetch_api_data(page)  # Fetch the brewery data for the current page
                if not breweries:  # If no breweries are returned (end of the data)
                    break  # Exit the loop
                for brewery in breweries:  # Loop through each brewery in the data
                    state = brewery.get('state')  # Get the state of the current brewery
                    if state in states:  # If the state is in the specified list
                        brewery_name.append(brewery.get('name'))  # Add the brewery's name to the list
            return brewery_name  # Return the list of brewery names in the specified states
        else:
            return "ERROR - 404"  # If the API is not available, return an error message

# Instantiate the Myjson class with the Open Brewery DB URL
json_obj = Myjson("https://api.openbrewerydb.org/breweries")

# Output the status code of the API (e.g., 200 for success)
print(json_obj.api_status_code())

# Fetch and output the data from the API (first page by default)
print(json_obj.fetch_api_data())

# Output the count of breweries by state
print(json_obj.count_breweries_by_state())

# Output the count of breweries with websites in Alaska, Maine, and New York
print(json_obj.count_breweries_with_website_on_state(['Alaska', 'Maine', 'New York']))

# List and output the names of breweries in Alaska, Maine, and New York
print(json_obj.list_brewery_name_by_state(['Alaska', 'Maine', 'New York']))
