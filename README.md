# LinkedIntelligence

LinkedIntelligence is a Python-based tool that scrapes employee information from a target company's LinkedIn page. It extracts employee names and job titles, and then writes the scraped data to both JSON and Excel files for easy access and analysis.

## Features

- Scrapes employee names and job titles from a target company's LinkedIn page
- Writes the scraped data to both JSON and Excel files
- Easy to use and customize

## Installation

1. Clone the repository:
```
git clone https://github.com/yourusername/LinkedIntelligence.git
```

2. Install the required Python libraries:
```
pip install beautifulsoup4 requests openpyxl
```

## Usage

1. Navigate to the LinkedIntelligence directory:
```
cd LinkedIntelligence
```

2. Run the script:
```
python linkedintelligence.py
```

3. Enter the target company name when prompted:
```
Enter the target company name: ExampleCompany
```

4. The script will scrape employee information and write it to both JSON and Excel files:
```
Employee information has been written to ExampleCompany_employee_info.json and ExampleCompany_employee_info.xlsx.
```

## Disclaimer

This tool is for educational purposes only. Web scraping may be against the terms of service of some websites, and you should always check the website's robots.txt file to ensure you're allowed to scrape its content.

## Contributing

Feel free to contribute to this project by submitting pull requests or opening issues.
