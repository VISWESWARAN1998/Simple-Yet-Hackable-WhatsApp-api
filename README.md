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
result = whatsapp.participants_for_group("group")
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



**Note:** Ir just automated the whatsapp, Nothing More, Nothing Less. This program is Licensed under Apache 2.0. 

Thank you for so many stars on this project, you can support me in follwing ways,

1. Paypal: visweswaran.nagasivam98@gmail.com
2. 1 GitHub follower =  1 supporter for me to get recogonized.
3. LinkedIn skill Endorsement: https://www.linkedin.com/in/visweswaran-nagasivam-975a8b167/
