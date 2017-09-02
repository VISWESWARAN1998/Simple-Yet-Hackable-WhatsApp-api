# Simple-Yet-Hackable-WhatsApp-api

**Using This API you can achieve many things in less than 5 lines of code**

**Sending a message with an emoji:**

```python
from whatsapp import WhatsApp
whatsapp = WhatsApp(10)
print(whatsapp.send_message("Name",":heart: Good!"))  
```
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

