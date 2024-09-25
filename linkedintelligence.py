import json
import asyncio
from requests_html import AsyncHTMLSession
from bs4 import BeautifulSoup
from openpyxl import Workbook

async def get_employee_info(session, company_name):
    # Replace spaces with dashes for the LinkedIn URL
    company_name = company_name.replace(" ", "-")

    # Define the base LinkedIn URL for the company
    base_url = f"https://www.linkedin.com/company/{company_name}/people/"

    # Send a request to the LinkedIn page and parse the HTML content
    response = await session.get(base_url)
    await response.html.arender()
    soup = BeautifulSoup(response.html.html, "html.parser")

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

async def main():
    # Set up an AsyncHTMLSession for making requests
    session = AsyncHTMLSession()

    # LinkedIn login credentials
    login_url = "https://www.linkedin.com/login"
    username = input("Enter your LinkedIn email: ")
    password = input("Enter your LinkedIn password: ")

    # Authenticate with LinkedIn
    await session.get(login_url)
    login_form = await session.post(login_url, data={"session_key": username, "session_password": password})

    # Check if authentication was successful
    if "login" not in login_form.url:
        print("Logged in successfully!")
    else:
        print("Failed to log in. Please check your credentials.")
        return

    company_name = input("Enter the target company name as it appears in the LinkedIn URL: ")
    employee_info = await get_employee_info(session, company_name)

    json_file_name = f"{company_name}_employee_info.json"
    excel_file_name = f"{company_name}_employee_info.xlsx"

    write_to_json(employee_info, json_file_name)
    write_to_excel(employee_info, excel_file_name)

    print(f"Employee information has been written to {json_file_name} and {excel_file_name}.")

if __name__ == "__main__":
    asyncio.run(main())
