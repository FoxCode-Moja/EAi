import os
import requests
import json
from dotenv import load_dotenv
import random

happy = sad = angry = excited = nervous = surprised = calm = confused = proud = lonely = 0

greet = ['what is calender saying today?',"what is happening with you?","Acttuly Hello !","Helppp!!!"]
load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")

import requests
import json
feeler_sys_prp = "Your output MUST be only one word from this list: ['happy', 'sad', 'angry', 'excited', 'nervous', 'surprised', 'calm', 'confused', 'proud', 'lonely']. Do not provide any reasoning or extra text."
def call_openrouter(user_input,module,sys_prp):
    url = "https://openrouter.ai/api/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": module,
        "messages": [
            {
                "role": "system", 
                "content": sys_prp
            },
            {"role": "user", "content": user_input}
        ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        result = response.json()
        clean_text = result['choices'][0]['message']['content'].strip()
        return clean_text
    else:
        return f"Error: {response.status_code}"
    



#Start Runing
print(random.choice(greet) + "...\n")
while True:
    inp = input("┏ (゜ω゜)=👉")

    
    result_command = call_openrouter(inp,"arcee-ai/trinity-mini:free",feeler_sys_prp)
    feel = result_command.strip()






    if feel == 'happy':
        happy += 100
    elif feel == 'sad':
        sad += 100
    elif feel == 'angry':
        angry += 100
    elif feel == 'excited':
        excited += 100
    elif feel == 'nervous':
        nervous += 100
    elif feel == 'surprised':
        surprised += 100
    elif feel == 'calm':
        calm += 100
    elif feel == 'confused':
        confused += 100
    elif feel == 'proud':
        proud += 100
    elif feel == 'lonely':
        lonely += 100

    # Rebuild feelval after updating
    feelval = [
        'happy' + str(happy),
        'sad' + str(sad),
        'angry' + str(angry),
        'excited' + str(excited),
        'nervous' + str(nervous),
        'surprised' + str(surprised),
        'calm' + str(calm),
        'confused' + str(confused),
        'proud' + str(proud),
        'lonely' + str(lonely)
    ]

    print("-"*10,"Feels of Ai","-"*10,"\n")

    print(feelval)
    print("-"*10,"Feel of Ai About You","-"*10,"\n")

    print(result_command)

    print("-"*10,"Output of Ai","-"*10,"\n")
    print(call_openrouter(f"Feels{feelval},User Input{inp}","arcee-ai/trinity-large-preview:free","your ouput syle must be builded on the list of feeling you will find it in start of user input // to put emoji you have ths codes 'existed','sad','angry','excited','nervous','surprised','calm','confused','proud','lonely' on your ouput print them like that :[command] only nothing else (don't type [command + namber] thats forbbiden the only optoin is [command] that's better for you) //+ouput must be more than 100 words").replace('[happy]', '😄').replace('[sad]', '😥').replace('[angry]', '😡').replace('[excited]', '🤩').replace('[nervous]', '😰').replace('[surprised]', '😲').replace('[calm]', '😌').replace('[confused]', '😕').replace('[proud]', '😎').replace('[lonely]', '😔'))
