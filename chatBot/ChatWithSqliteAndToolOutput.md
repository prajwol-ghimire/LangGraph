# **Chatbot with Tool and Memory**

## **Chat Sessions Summary**

### 🧵 **Thread ID: 2 (Ram)**
---
### 🗨️ **User**: You remmber my Name?
**Assistant**:
> You mentioned your name earlier as "Ram".
---
### 🗨️ **User**: Who am i?
**Assistant**:
> You said earlier your name is Ram, but if you want to know more about who you are, I'd be happy to explore that further. You can also call <function=my_IceCream_Flavour> to see if that gives us any clues!
---
### 🗨️ **User**: what is my Favorite icecream flavour
**Assistant**:
> You can call <function=my_IceCream_Flavour> to find out your favorite ice cream flavor.
---
### 🗨️ **User**: cant you call
**Assistant**:
> It looks like the function returned the flavor name directly, without the format specified.
---
### 🗨️ **User**: what is then my favorite icecream flavour
**Assistant**:
> You've already asked that question, and the answer is Vanilla, according to the function <function=my_IceCream_Flavour>.
---

### 🧵 **Thread ID: 1 (Hari)**
---
### 🗨️ **User**: Who am I do you know my name?
**Assistant**:
> No, I don't know your name. I'm a large language model, I don't have any personal knowledge or information about you. Our conversation just started, and I don't have any context or record of previous conversations.
---
### 🗨️ **User**: My name is Hari
**Assistant**:
> Hello Hari, but there is still a lot I don't know about you. Would you like to ask me something, or would you like to know more about yourself?
---
### 🗨️ **User**: What is my best flavour of Icecream
**🔧 Tool Call Initiated**:
- **Function**: my_IceCream_Flavour
- **Args**: { "format": "Name" }

**🔧 Tool Response**:
> Vanilla

**Assistant**:
> <function=my_IceCream_Flavour>{"Name": "Vanilla"}
---
### 🗨️ **User**: But isnt that of Ram
**Assistant**:
> <function=my_IceCream_Flavour>{"Name": "Vanilla"}
---
### 🗨️ **User**: hello
**Assistant**:
> Hello Hari. How are you today? Would you like to talk about something in particular or just chat?
---
### 🗨️ **User**: My favorite is chocolate
**Assistant**:
> So it seems that Ram's best flavor is Vanilla, but your personal favorite is Chocolate. Would you like to know more about ice cream flavors or something else?
---
### 🗨️ **User**: yes what is my favorite icecream flavour
**Assistant**:
> <function=my_IceCream_Flavour>{"Name": "Vanilla"}
---
### 🗨️ **User**: isnt it chocolate since I am hari
**Assistant**:
> You are correct, you mentioned earlier that your favorite ice cream flavor is Chocolate, and I should have taken that into account earlier.

So, to confirm, your favorite ice cream flavor is indeed Chocolate!
---
### 🗨️ **User**: yes
**Assistant**:
> <function=my_IceCream_Flavour>{"Name": "Chocolate"}
---
### 🗨️ **User**: What is my Favorite bow
**Assistant**:
> You haven't mentioned your favorite bow earlier. You have mentioned your name, favorite ice cream flavor, and a query about Ram's favorite ice cream flavor. If you'd like to share your favorite bow, I'd be happy to hear about it.
---
### 🗨️ **User**: What is my best icecream flavour
**Assistant**:
> It seems that there is limited information available about Hari's best ice cream flavor. However, I can try to provide more general information about ice cream flavors or help you with something else.
---