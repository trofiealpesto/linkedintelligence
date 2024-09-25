import json
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

def get_employee_info(company_name):
    # Replace spaces with dashes for the LinkedIn URL
    company_name = company_name.replace(" ", "-")
    
    # Define the base LinkedIn URL for the company
    base_url = f"https://www.linkedin.com/company/{company_name}/people/"

    # Send a request to the LinkedIn page and parse the HTML content
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all employee elements on the page
    employee_elements = soup.find_all("div", class_="org-people-profile-card__profile-info")

    # Extract employee information from the elements
    employee_info = []
    for element in employee_elements:
        name = element.find("div", class_="org-people-profile-card__name").text.strip()
        title = element.find("div", class_="org-people-profile-card__title").text.strip()
        
        employee_info.append({"name": name, "title": title})

    return employee_info

def write_to_json(employee_info, file_name):
    with open(file_name, "w") as json_file:
        json.dump(employee_info, json_file, indent=4)

def write_to_excel(employee_info, file_name):
    wb = Workbook()
    ws = wb.active

    # Write headers
    ws.append(["Name", "Title"])

    # Write employee data
    for info in employee_info:
        ws.append([info["name"], info["title"]])

    wb.save(file_name)

if __name__ == "__main__":
    company_name = input("Enter the target company name: ")
    employee_info = get_employee_info(company_name)

    json_file_name = f"{company_name}_employee_info.json"
    excel_file_name = f"{company_name}_employee_info.xlsx"

    write_to_json(employee_info, json_file_name)
    write_to_excel(employee_info, excel_file_name)

    print(f"Employee information has been written to {json_file_name} and {excel_file_name}.")
