# Glassdoor Job Listing Scraper

The "Glassdoor Job Listing Scraper" is a Python script designed to automate the process of extracting job listing data from the popular job search platform Glassdoor. It uses the Selenium web automation library to navigate Glassdoor's website, search for job listings based on user-defined criteria, and then extract relevant information from the job postings. This information is subsequently saved in a CSV file for further analysis.

## Credit
This script was inspired by and adapted from a tutorial written by Mert Sakarya on Medium titled "Selenium Tutorial: Scraping Glassdoor.com in 10 Minutes." The original tutorial provided valuable insights and code examples for scraping job listings from Glassdoor using Selenium, and it served as a foundational reference for this script.

The tutorial by Mert Sakarya can be found at [link.](https://mersakarya.medium.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905)

The adaptation of the code for this script was done to provide a more comprehensive and user-friendly solution for automating job listing data extraction from Glassdoor while adding additional features and robust error handling.
## How Does the Code Work?

Here's a breakdown of how the code functions and the key steps it performs:

1. **Setup and Configuration:**
   - The script starts by importing necessary libraries such as Selenium, pandas, and time.
   - It configures options for the Chrome web browser, including the browser window size.
   - The path to the ChromeDriver executable is specified to enable automation with the Google Chrome browser.

2. **Navigating to Glassdoor:**
   - The script opens the Google Chrome browser and navigates to Glassdoor's job search page (https://www.glassdoor.com/Job/index.htm).

3. **Input Criteria:**
   - Users can specify their job search criteria, including the keyword (e.g., job title or skill), the number of pages of job listings to scrape, and the desired location.

4. **Data Extraction:**
   - The script initiates a loop to go through multiple pages of job listings, scraping information from each listing.
   - It clicks on each job listing to access more details and extract data.
   - The code handles various scenarios, such as closing signup prompts, expanding job descriptions, and extracting job-related data, including company name, job title, location, job description, and salary estimate.

5. **Saving Data:**
   - Extracted data is stored in lists.
   - The script then creates a pandas DataFrame with the collected data.
   - Finally, it saves this DataFrame as a CSV file, with the filename based on the provided keyword (e.g., "data analyst.csv").

