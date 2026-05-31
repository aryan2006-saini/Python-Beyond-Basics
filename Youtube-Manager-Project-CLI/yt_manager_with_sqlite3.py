import sqlite3

# make the connection
conn = sqlite3.connect('Youtube-Manager-Project-CLI\\yt_videos.db')
cursor = conn.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS videos(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute("INSERT INTO videos(name, time) VALUES (?,?)", (name, time))
    conn.commit()

def update_detail(id, new_name, new_time):
    cursor.execute("UPDATE videos SET name=?,time=? WHERE id = ?", (new_name, new_time,id))
    conn.commit()

def delete_video(id):
    cursor.execute("DELETE FROM videos WHERE id=?",(id,))
    conn.commit()


def main():
    while True:
        print("\n Youtube Manager app with DB | choose an option ")
        print("1. List all youtube videos: ")
        print("2. Add a youtube video: ")
        print("3. Update a youtube video details: ")
        print("4. Delete a youtube video: ")
        print("5. Exit the app: ")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_videos()
            case '2':
                name = input("Enter the video name: ")
                time = input("Enter the video duration: ")
                add_video(name,time)
            case '3':
                id = input("Enter video ID: ")
                name = input("Enter updated name: ")
                time = input("Enter the new duration: ")
                update_detail(id,name, time)
            case '4':
                id = input("Enter video ID to delete: ")
                delete_video(id)
            case '5':
                break
            case _:
                print("Invalid Option.")

    conn.close()


if __name__=="__main__":
    main()