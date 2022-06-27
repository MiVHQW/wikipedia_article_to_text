import bs4
import requests
import re

class Article:
    def __init__(self,url:str):
        self.url = url
    def get_response_html(self):
        response_text = requests.get(self.url).text
        return response_text
    def get_parsed_response(self):
        response_text = self.get_response_html()
        parsed_response = bs4.BeautifulSoup(response_text,features="lxml")
        return parsed_response
    def get_parsed_text(self):
        parsed_response_text = self.get_parsed_response().text
        return parsed_response_text
    def get_parsed_paragraphs(self):
        parsed_response = self.get_parsed_response().find_all("p")
        paragraphs = []
        for p in parsed_response:
            paragraphs.append(p.text)
        return paragraphs
    def remove_citation_marks(self,string:str):
        citation_mark_pattern = r"\[\d+\]"
        return re.sub(citation_mark_pattern,"",string)
    def pretty_print_parsed_paragraphs(self):
        paragraphs = self.get_parsed_paragraphs()
        string = """"""
        for p in paragraphs:
            p = self.remove_citation_marks(p)
            string += f"{p}\n"
        return string

if __name__ == "__main__":
    my_site = Article("https://de.wikipedia.org/wiki/Zamonien")

    result = my_site.pretty_print_parsed_paragraphs()

    print(result)
