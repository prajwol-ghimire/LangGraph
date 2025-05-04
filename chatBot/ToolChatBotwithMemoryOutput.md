
# **Chatbot with Tool and Memory**

## **Chat Session Summary**

---

### 🗨️ **User**: `Hi`  
**Assistant**:  
> It's great to meet you! How can I assist you today? Would you like to discuss something specific, or should we chat casually?

---

### 🗨️ **User**: `My name is Ram`  
**Assistant**:  
> Nice to meet you, Ram! What brings you here today? Is there something specific you'd like to talk about, or just having a casual chat?

---

### 🗨️ **User**: `What are you doing?`  
**Assistant**:  
> I'm here to assist you with anything you need! Whether it's answering questions, providing suggestions, or helping with tasks, I'm ready for whatever you need. What would you like to do today?

---

### 🗨️ **User**: `What is Ram's favorite Ice cream flavour?`  
**🔧 Tool Call Initiated**:  
- **Function**: `my_IceCream_Flavour`  
- **Args**: `{ "format": "Name" }`  

**🔧 Tool Response**:  
> Vanilla

**Assistant**:  
> It seems like Ram's favorite ice cream flavor is Vanilla.

**🔧 Model Info**:  
- **Model**: `llama-3.1-8b-instant`  