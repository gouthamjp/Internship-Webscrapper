from bs4 import BeautifulSoup
import requests
import time

print('Enter the skill your are looking internship for')
input_intern = input()
url = 'https://internshala.com/internships/keywords-'+input_intern+'?utm_source=hp_internship_keyword_search'
def find_intern():
    
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    internships = soup.find_all('div', class_ = "internship_meta")
    
    for index,inter in enumerate(internships):
        comapny_name = inter.find('a', class_ = "link_display_like_text").text.strip()
        location = inter.find('div', id = "location_names").text.strip()
        details = inter.find('div', class_ = "internship_other_details_container").text.strip().replace('\n','').replace('           ',' ')

        with open(f'updates/{index}.txt', 'w') as f:
            f.write(f'Company Name : {comapny_name}\n')
            f.write(f'Location : {location}\n')
            f.write(f'Deatail : {details} \n')
            f.write('\n')

        print(f'''
            Company Name : {comapny_name} 
            Location : {location}   
            Deatails : {details} 
        ''')
        print(f'File Saved {index}.txt')

if __name__ == '__main__':
    while True:
        find_intern()
        time_wait = 30
        print(f'Next update in {time_wait} minutes')
        time.sleep(time_wait * 60)



