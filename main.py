import time
from plyer import notification

def Water():
    while True:
        notification.notify(
            title = " Now Water Time !",
            message = " 15.5 cups (3.7 liters) of fluids a day for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
            
            app_icon ="C:\\Users\\sheta\\OneDrive\\Desktop\\Practice Programe\\Drinking Water Notification\\drink-bottle.ico",
            timeout=(15)
        )
        time.sleep(15*15)

if __name__ == '__main__':
    Water()