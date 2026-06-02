import requests

def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        name = user_data["name"]["first"]+" "+ user_data["name"]["last"]
        country = user_data["location"]["state"]+", "+ user_data["location"]["country"]
        return username,name,country
    else:
        raise Exception("User Not Found.")
    

def main():
    try:
        username, name, country = fetch_random_user()
        print(f"UserName: {username}\nName: {name}\nCountry: {country}")
    except Exception as e:
        print(type(e))
        print(e)

if __name__=="__main__":
    main()

# provide a random user
# sample example: UserName: ticklishbutterfly645
#                 Name: Ella Morrison
#                 Country: Kerry,Ireland