# Glassdoor Job Listing Scraper

The "Glassdoor Job Listing Scraper" is a Python script designed to automate the process of extracting job listing data from the popular job search platform Glassdoor. It uses the Selenium web automation library to navigate Glassdoor's website, search for job listings based on user-defined criteria, and then extract relevant information from the job postings. This information is subsequently saved in a CSV file for further analysis.

**Skills Utilized:**

- **Web Scraping & Automation:**
  - Selenium for web scraping, automation, and Chrome web driver configuration.
  - Time management for script synchronization.

- **Python Scripting & Data Handling:**
  - Python for data extraction, manipulation, scripting, and error handling.
  - Pandas for data handling, cleaning, and CSV management.

- **Data Extraction, Parsing, Transformation & Basic Analysis:**
  - Extracted and transformed job-related information from Glassdoor.
  - Implemented parsing techniques for HTML elements.
  - Conducted basic data analysis using Pandas.

- **XPath Usage & Element Selection:**
  - Efficient use of XPath expressions for element location and selection.

- **Dynamic Scraping, Pagination & Efficiency:**
  - Developed a dynamic script for scraping multiple pages and navigating pagination.
  - Configured Chrome options for enhanced efficiency, including window size.

- **Interactions & Automation Scripting:**
  - Interacted with webpage elements for navigation and triggered actions.
  - Developed an automated script for systematic data retrieval.

- **File Handling & CSV Export:**
  - Managed file paths for drivers and CSV export.
  - Created and managed DataFrames with Pandas.

These combined skills synergistically contributed to the successful execution of the web scraping project, enabling the retrieval, cleaning, and analysis of valuable job-related insights from Glassdoor.

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

## Data Cleaning Process

- Loaded job data from a CSV file into a Pandas DataFrame.
- Removed duplicate job listings on Glassdoor based on 'job description' to ensure analysis accuracy.
- Omitted rows without salary values to focus on salary-related insights.
- Processed the 'salary estimate' column, handling variations like 'per hour' or 'employer est.'
- Calculated minimum and maximum salary values, creating an average salary column for analysis.
- Derived company ratings from the last three characters of the 'company' column.
- Cleaned company names by removing trailing numerical values.
- Explored job distribution by location and introduced a new 'age' column based on 'company_founded.'
- Identified specified keywords within job descriptions, enhancing analysis flexibility.
- Saved the cleaned data to 'jobs analysis.csv' and tool-related research data to 'tools research.csv.'
- Simplified job titles into broader categories for clarity.
- Classified job titles into seniority levels and determined working environments based on descriptions.
- Explored job distribution across different industries for comprehensive analysis.
