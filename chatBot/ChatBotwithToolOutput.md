
## Memory Less Chat Bot with Tool

## Chat Session Summary

## 🗨️ User: `hi`
**Assistant:**  
> I'm happy to chat with you. Is there something I can help you with or would you like to discuss a particular topic?

**🔧 Model Info:**
- Model: `llama-3.1-8b-instant`
- System Fingerprint: `fp_f7bd09b454`

**📊 Token Usage:**
- Prompt: `344`
- Completion: `27`
- Total: `371`
- Time (s): Queue `6.73`, Prompt `0.07`, Completion `0.04`, Total `0.10`

---

## 🗨️ User: `what is weather today in Banglore?`
**🔧 Tool Call Initiated:**
- Function: `tavily_search_results_json`
- Args: `{ "query": "current weather in Bangalore" }`

**🔧 Tool Response:**
> Today’s Weather in Bengaluru: Partly Cloudy with max temperature of 33°C and min of 20°C.  
> *(Alt. Source: Max 35°C, Min 21°C)*

**Assistant:**  
> The current weather in Bangalore is expected to be Partly Cloudy with a maximum temperature of 33°C and a minimum of 20°C.

**🔧 Model Info:**
- Model: `llama-3.1-8b-instant`
- System Fingerprint: `fp_f7bd09b454`

**📊 Token Usage:**
- Tool Call Message: Prompt `701`, Completion `21`, Total `722`
- Final Answer Message: Prompt `571`, Completion `30`, Total `601`
- Time (s): Tool Prompt `0.04`, Completion `0.03`, Total `0.07`; Final Answer Prompt `0.05`, Completion `0.04`, Total `0.09`

---

## 🗨️ User: `what is my favorite Icecream Flavour?`
**🔧 Tool Call Initiated:**
- Function: `my_IceCream_Flavour`
- Args: `{ "format": "Name" }`

**🔧 Tool Response:**  
> Vanilla

**Assistant:**  
> My favourite ice cream flavor is vanilla.

**🔧 Model Info:**
- Model: `llama-3.1-8b-instant`
- System Fingerprint: `fp_a4265e44d5`

**📊 Token Usage:**
- Tool Call Message: Prompt `352`, Completion `19`, Total `371`
- Final Answer Message: Prompt `383`, Completion `9`, Total `392`
- Time (s): Tool Prompt `0.02`, Completion `0.03`, Total `0.05`; Final Answer Prompt `0.02`, Completion `0.01`, Total `0.04`
