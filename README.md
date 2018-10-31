# Simple-Yet-Hackable-WhatsApp-api

**Using This API you can achieve many things in less than 5 lines of code**

**Sending a message with an emoji:**

```python
from whatsapp import WhatsApp
whatsapp = WhatsApp(10)
print(whatsapp.send_message("Name",":heart: Good!"))  
```
**Result:** <br>
![Image](https://raw.githubusercontent.com/VISWESWARAN1998/Simple-Yet-Hackable-WhatsApp-api/master/Screenshot%20(747).png)

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

**Sending Anonymous messages**
*Note: The phone number should not contain spaces and special characters(+, -) but shall contain country code. Example: +91-861 123 4567 shoulld be formatted to 918611234567*
```python
# SWAMI KARUPPASWAMI THUNNAI

from whatsapp import WhatsApp

app = WhatsApp(10)
app.send_anon_message("91XXXXXXXXXX", "I am sorry for what is happening sir! But I have no other choice.")
```

**Sending Messages to multiple participants**
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

**Note:** Ir just automated the whatsapp, Nothing More, Nothing Less. This program is Licensed under Apache 2.0. 

Thank you for so many stars on this project, you can support me in follwing ways,

1. Paypal: visweswaran.nagasivam98@gmail.com
2. 1 GitHub follower =  1 supporter for me to get recogonized.
3. LinkedIn skill Endorsement: https://www.linkedin.com/in/visweswaran-nagasivam-975a8b167/
