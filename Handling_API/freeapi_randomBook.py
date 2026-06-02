import requests

def fetch_random_book():
    url = "https://api.freeapi.app/api/v1/public/books/book/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        book_data = data["data"]["volumeInfo"]
        title = book_data["title"]
        authors = book_data["authors"]
        return title,authors
    else:
        raise Exception("Url not found.")
    
def main():
    try:
        title, authors = fetch_random_book()
        print(f"Book Name: {title}\nAuthors: {authors}")
    except Exception as e:
        print(type(e))
        print(str(e))

if __name__=="__main__":
    main()
#fetches a random book
# Sample example: 
#               Book Name: Programming in C++, 2/e
#               Authors: ['Ashok Kamthane']