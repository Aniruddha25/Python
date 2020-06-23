import bs4
import requests  
  
#Creating the requests  
  
res = requests.get("https://en.wikipedia.org/wiki/Machine_learning")  
print("The object type:",type(res))  
  
# Convert the request object to the Beautiful Soup Object  
soup = bs4.BeautifulSoup(res.text,'html5lib')  
print("The object type:",type(soup))
soup.select('.mw-headline')  
for i in soup.select('.mw-headline'):  
     print(i.text,end = ',')  

url="https://www.javatpoint.com/"  
  
# Make a GET request to fetch the raw HTML content  
html_content = requests.get(url).text  
  
# Parse the html content  
soup = BeautifulSoup(html_content, "html5lib")  
print(soup.prettify()) # print the parsed data of html  
for link in soup.find_all("a"):  
    print("Inner Text is: {}".format(link.text)) 
    print("Title is: {}".format(link.get("title")))  
    print("href is: {}".format(link.get("href")))  
