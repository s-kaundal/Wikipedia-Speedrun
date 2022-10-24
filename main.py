import requests


class MyPage:
    def __init__(self, my_title):
        self.title = my_title
        self.URL = "https://en.wikipedia.org/w/api.php?"
        self.params = {
            "action": "query",
            "format": "json",
            "prop": "links",
            "titles": my_title,
            "pllimit": "max"
        }
        self.response = requests.get(self.URL, self.params)
        self.data = self.response.json()
        self.pages = self.data["query"]["pages"]

    def set_continue_params(self, new_params):
        self.params["plcontinue"] = new_params

    def get_data(self):
        return self.data

    def get_data_continue(self):
        return self.data["continue"]["plcontinue"]

    def set_response(self):
        self.response = requests.get(self.URL, self.params)

    def set_data(self):
        self.data = self.response.json()

    def set_pages(self):
        self.pages = self.data["query"]["pages"]


def get_all_links_page(my_page):
    all_links = []

    def get_one_page_links():
        for key, val in my_page.pages.items():
            for link in val["links"]:
                all_links.append(link["title"])

    def get_all_links():
        while "continue" in my_page.get_data():
            plcontinue = my_page.get_data_continue()
            my_page.set_continue_params(plcontinue)
            my_page.set_response()
            my_page.set_data()
            my_page.set_pages()
            get_one_page_links()

    get_one_page_links()
    get_all_links()
    return all_links


def find_path(start_title, end_title):
    def fn_for_title(title, working_list, visited):
        list_of_titles = get_all_links_page(MyPage(title))
        if list_of_titles.__contains__(end_title):
            visited.append(title)
            print("I went through " + len(visited).__str__() + " links to get to the last article.")
            print(visited)
        elif visited.__contains__(title):
            fn_for_lot(working_list, visited)
        else:
            working_list.extend(list_of_titles)
            visited.append(title)
            fn_for_lot(working_list, visited)

    def fn_for_lot(working_list, visited):
        new_title = working_list.pop(0)
        fn_for_title(new_title, working_list, visited)

    fn_for_title(start_title, [], [])


if __name__ == '__main__':
    num_links = 0
    links = []
    visited_links = []
    first_title = input("Type the wikipedia page to start with.\n")
    last_title = input("Type the Wikipedia page to end with.\n")
    find_path(first_title, last_title)
