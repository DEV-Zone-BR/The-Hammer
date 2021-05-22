from bs4 import BeautifulSoup
import requests
from typing import Union


def get_data(url: str) -> Union[bool, BeautifulSoup]:
    try:
        page = requests.get(url)
        if not page.status_code == 200:
            return False
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup
    except requests.exceptions.ConnectionError:
        return False


def get_all_vacanicies(end: int = 5, page: int = 1) -> Union[bool, set[str], list]:
    vacanicies_filtered = {"vanicies": []}
    try:
        soup = get_data(f"https://www.pyjobs.com.br/jobs/?page={page}")
        if not soup:
            return False

        item_filtered = soup.find_all(class_="vaga")
        for current in range(end+1):
            new_vacancies = {}
            current_vacancies = (item_filtered[current])
            p_in_page = current_vacancies.find_all("p")
            a_in_page = current_vacancies.find("a")
            new_vacancies["page"] = page
            new_vacancies["vacancie_number"] = current
            new_vacancies["status"] = p_in_page[0].get_text()
            new_vacancies["empresa"] = p_in_page[1].get_text()[9:]
            new_vacancies["title"] = current_vacancies.find("h3").get_text()
            new_vacancies["level"] = p_in_page[2].get_text().replace(" ", "").split("\n")[1]
            new_vacancies["local"] = p_in_page[3].get_text().replace(" ", "").split("\n")[1]
            new_vacancies["more_information"] = 'https://www.pyjobs.com.br' + a_in_page['href']
            current_soup = get_data(new_vacancies["more_information"])
            if not current_soup:
                return {"It was not possible to make the request, please try again later !."}

            new_vacancies["technologies"] = [badge.get_text() for badge in current_soup.find_all(class_="badge")]
            vacanicies_filtered["vanicies"].append(new_vacancies)
        return vacanicies_filtered["vanicies"]

    except IndexError:
        return False


if __name__ == '__main__':
    print(get_all_vacanicies(5, 3))