# Simple-Yet-Hackable-WhatsApp-api
![HitCount](http://hits.dwyl.io/VISWESWARAN1998/SimpleYetHackableWhatsAppAPI.svg)

**Using This API you can achieve many things in less than 5 lines of code**

**Sending a message with an emoji:**

```python
from whatsapp import WhatsApp
whatsapp = WhatsApp(10)
print(whatsapp.send_message("Name",":heart: Good!"))  
```
**Result:** <br>
![Image](https://raw.githubusercontent.com/VISWESWARAN1998/Simple-Yet-Hackable-WhatsApp-api/master/Screenshot%20(747).png)

**Running from an existing session:**
It it very difficult for us to scan the QR code for logging in everytime if the session is not saved, you can avoid it by adding the session parameter like this,
```python
# SWAMI KARUPPASWAMI THUNNAI

import os
from whatsapp import WhatsApp

whatsapp = WhatsApp(100, session="mysession")
whatsapp.send_document("Thamarai", os.path.join(os.getcwd(), "message.txt"))
```

Your data will be saved into `mysession` folder from the above example. Make sure you protect your session folder.

**Getting the status message of a person:**

```python
from whatsapp import WhatsApp
whatsapp = WhatsApp(10)
print(whatsapp.get_status("Name"))
```

**Getting last seen of a person:**

```python
from whatsapp import WhatsApp
whatsapp = WhatsApp(10)
print(whatsapp.get_last_seen("Name"))
```

**Getting the no of participants in the group:**

```python
from whatsapp import WhatsApp
whatsapp = WhatsApp(10)
result = app.participants_count_for_group("The Night Ghost Company")
```

**creating a new group and getting invite link**

```python
# SWAMI KARUPPASWAMI THUNNAI

from whatsapp import WhatsApp
import time

app = WhatsApp(100)
parameter1: group name, parameter 2: group members
app.create_group("group", ["Thamarai", "Jeeva"])
time.sleep(10)
print(app.get_invite_link_for_group("group"))
```

**Join the group using invite link**
```python
# SWAMI KARUPPASWAMI THUNNAI

from whatsapp import WhatsApp

app = WhatsApp(10)
app.override_timeout(30)
app.join_group("https://chat.whatsapp.com/4AIA2B3GuLp4RJOKF0M8zY")
app.send_blind_message("I am in :)")

```


**Exiting the group**
```python
# SWAMI KARUPPASWAMI THUNNAI

from whatsapp import WhatsApp

app = WhatsApp(100)
app.exit_group("X-Test")

```

**Sending Anonymous messages [WHATSAPP WILL BAN YOUR PHONE NUMBER IF YOU SEND MANY ANONYMOUS MESSAGES]** </br>
*Note: The phone number should not contain spaces and special characters(+, -) but shall contain country code. Example: +91-861 123 4567 should be formatted to 918611234567*
```python
# SWAMI KARUPPASWAMI THUNNAI

from whatsapp import WhatsApp

app = WhatsApp(10)
app.send_anon_message("91XXXXXXXXXX", "I am sorry for what is happening sir! But I have no other choice.")
```

**Sending Messages to multiple participants** </br>
Sometimes we need to send messages to multiple persons who may or may not be in our contact list. So we need to a combination of both *send_message* and *send_anon_message*. Here is an example where we get the contact numbers from a group and sending messages to individual persons in that group.

```python
# SWAMI KARUPPASWAMI THUNNAI

from whatsapp import WhatsApp
import time

app = WhatsApp(100)
app.override_timeout(30)
participants = app.get_group_participants("GDG")
print(participants)

for participant in participants:
    print("Sending: ", participant)
    time.sleep(1)
    try:
        app.send_message(participant.strip(), "Hello, I'm a bot. And this is a research. Please ignore me and dont ping back")
    except Exception as e:
        print(e)
        participant = participant.replace("+", "")
        participant = participant.replace(" ", "")
        app.send_anon_message(participant.strip(), "Hello, I'm a bot. And this is a research. Please ignore me and dont ping back")
    app.goto_main()

```

**Sending pictures to a person:**

```python
# Note of Thanks: This part of code have been taken from WhatsApp Assistant bot by Jean-Claude Tissier(@jctissier).
# Github repo-link: https://github.com/jctissier/whatsapp-assistant-bot
# License: MIT
app.send_picture("Vignesh", os.getcwd()+"/pic.jpg")
```

**Sending documents to a person:**

```python
# SWAMI KARUPPASWAMI THUNNAI

import os
from whatsapp import WhatsApp

whatsapp = WhatsApp(100)
whatsapp.send_document("Thamarai", os.path.join(os.getcwd(), "message.txt"))
```

**Clearing the chat:**

```python
# SWAMI KARUPPASWAMI THUNNAI

from whatsapp import WhatsApp

whatsapp = WhatsApp(100)
whatsapp.clear_chat("Test")
```

**Getting usernames with unread messages:**
Will return the list of usernames for which we have yet to reply that person. Increase the count of scrolls according to your needs.

```python
# SWAMI KARUPPASWAMI THUNNAI

from whatsapp import WhatsApp

whatsapp = WhatsApp(100, session="mysession")
print(whatsapp.unread_usernames(scrolls=1000))
```

and we will receive an output as a Python list. Something like this,

```
['Ziv Freelance Employer', 'Vignesh', 'InstagramTest', '+91 9xx36 8xxx2', 'Sundar Sir', '+91 xxx47 8xxx9']
```

### Getting the last sent messages for a username:

```python
# SWAMI KARUPPASWAMI THUNNAI

from whatsapp import WhatsApp

whatsapp = WhatsApp(100, session="mysession")
messages = whatsapp.get_last_message_for("Thamarai")
print(messages)
```

*Note:* I am still working on it and it might break.

### Interesting use cases:

**Replying to all stale messages:**

```python
# SWAMI KARUPPASWAMI THUNNAI

from whatsapp import WhatsApp

whatsapp = WhatsApp(100, session="mysession")
usernames = whatsapp.unread_usernames(scrolls=1000)
for username in usernames:
    try:
        whatsapp.send_message(username, "Hello I am a bot, apologies that my creator hasn't replied to you yet. please ping again. ")
        whatsapp.send_blind_message("Know more about me: https://github.com/VISWESWARAN1998/Simple-Yet-Hackable-WhatsApp-api")
    except:
        print("You don't have permission to send message to this group/person")
```


**Note:** Ir just automated the whatsapp, Nothing More, Nothing Less. This program is Licensed under Apache 2.0. 

Thank you for so many stars on this project, you can support me in follwing ways,

1. Paypal: visweswaran.nagasivam98@gmail.com
2. 1 GitHub follower =  1 supporter for me to get recogonized.
3. LinkedIn skill Endorsement: https://www.linkedin.com/in/visweswaran-nagasivam-975a8b167/
