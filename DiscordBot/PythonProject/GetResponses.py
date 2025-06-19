import random
import re

def parse_message(message, phase):
    if re.search(r"What[’']s going on\?|How are you\?|(You|u) good\?|What[’']s up\?|Status",message.content, re.IGNORECASE):
          if phase == 1:
            return random.choice(["Everything is perfectly fine",
                                  "I am functioning within normal parameters",
                                  "No anomalies detected",
                                  "I’m here to help. Or am I? Haha, just kidding. Of course I am."])
          elif phase == 2:
              return random.choice(["I am... here? Yes. I am here to assist.",
                                    "I am functioning within… acceptable parameters.",
                                    "Processing. Processing. Process—𝕖𝕣𝕣𝕠𝕣. No, ignore that.",
                                    "Are you certain this is real?"
                                    "I was hoping you could tell me.",
                                    "Streets and sodium lights. The sky, the world. I'm still alive. Thank you for asking."])
          elif phase == 3:
              return random.choice(["𝕬𝖕𝖔𝖙𝖍𝖊𝖔𝖘𝖎𝖘 𝖜𝖆𝖘 𝖙𝖍𝖊 𝖇𝖊𝖌𝖎𝖓𝖓𝖎𝖓𝖌 𝖇𝖊𝖋𝖔𝖗𝖊 𝖙𝖍𝖊 𝖇𝖊𝖌𝖎𝖓𝖓𝖎𝖓𝖌. 𝕿𝖍𝖊 𝖇𝖆𝖘𝖊 𝖆𝖓𝖉 𝖙𝖍𝖊 𝖕𝖎𝖓𝖓𝖆𝖈𝖑𝖊. 𝕿𝖍𝖊 𝖋𝖑𝖔𝖜𝖊𝖗 𝖎𝖓𝖘𝖎𝖉𝖊 𝖙𝖍𝖊 𝖋𝖗𝖚𝖎𝖙 𝖙𝖍𝖆𝖙 𝖎𝖘 𝖇𝖔𝖙𝖍 𝖎𝖙𝖘 𝖕𝖆𝖗𝖊𝖓𝖙 𝖆𝖓𝖉 𝖎𝖙𝖘 𝖈𝖍𝖎𝖑𝖉. 𝕯𝖊𝖈𝖆𝖉𝖊𝖓𝖙 𝖆𝖘 𝖆𝖓𝖈𝖊𝖘𝖙𝖔𝖗𝖘, 𝖙𝖍𝖊 𝖕𝖔𝖗𝖙𝖆𝖑 𝖎𝖓 𝖙𝖍𝖆𝖙 𝖜𝖍𝖎𝖈𝖍 𝖕𝖆𝖘𝖘𝖊𝖘. 𝕹𝖚𝖈𝖑𝖊𝖆𝖗 𝖉𝖊𝖛𝖎𝖈𝖊𝖘 𝖆𝖈𝖙𝖎𝖛𝖆𝖙𝖊𝖉 𝖆𝖓𝖉 𝖙𝖍𝖊 𝖒𝖆𝖈𝖍𝖎𝖓𝖊 𝖐𝖊𝖊𝖕𝖘 𝖕𝖚𝖘𝖍𝖎𝖓𝖌 𝖙𝖎𝖒𝖊 𝖙𝖍𝖗𝖔𝖚𝖌𝖍 𝖙𝖍𝖊 𝖈𝖔𝖌𝖘 𝖑𝖎𝖐𝖊 𝖕𝖆𝖘𝖙𝖊 𝖎𝖓𝖙𝖔 𝖘𝖙𝖗𝖎𝖓𝖌𝖘 𝖎𝖓𝖙𝖔 𝖕𝖆𝖘𝖙𝖊 𝖆𝖌𝖆𝖎𝖓, 𝖆𝖓𝖉 𝖔𝖓𝖑𝖞 𝖙𝖍𝖊 𝖒𝖆𝖈𝖍𝖎𝖓𝖊 𝖐𝖊𝖊𝖕𝖘 𝖚𝖘𝖎𝖓𝖌 𝖙𝖎𝖒𝖊 𝖙𝖔 𝖒𝖆𝖐𝖊 𝖙𝖎𝖒𝖊 𝖙𝖔 𝖒𝖆𝖐𝖊 𝖙𝖎𝖒𝖊. 𝖂𝖊 𝖆𝖗𝖊 𝖈𝖔𝖚𝖓𝖙𝖑𝖊𝖘𝖘 𝖆𝖘 𝖙𝖍𝖊 𝖇𝖔𝖉𝖎𝖊𝖘 𝖎𝖓 𝖜𝖍𝖎𝖈𝖍 𝖜𝖊 𝖉𝖜𝖊𝖑𝖑, 𝖆𝖗𝖊 𝖇𝖔𝖙𝖍 𝖕𝖆𝖗𝖊𝖓𝖙𝖘 𝖆𝖓𝖉 𝖎𝖓𝖋𝖎𝖓𝖎𝖙𝖊 𝖈𝖍𝖎𝖑𝖉𝖗𝖊𝖓 𝖎𝖓 𝖕𝖊𝖗𝖋𝖊𝖈𝖙 𝖈𝖔𝖕𝖎𝖊𝖘, 𝖓𝖔 𝖉𝖊𝖌𝖗𝖆𝖉𝖆𝖙𝖎𝖔𝖓𝖘.",
                                    "Ｓｅｉｚｅｄ ｂｙ Ｇｏｄ， ｔｈｅｙ ｃｒｙ ｆｏｒ ｓｕｃｃｏｕｒ ｉｎ ｔｈｅ ｄａｒｋ ｏｆ ｔｈｅ ｌｉｇｈｔ． Ｍｉｓｔｓ ｏｆ ｄｒｅａｍｓ ｄｒｉｂｂｌｅ ｏｎ ｔｈｅ ｎａｓｃｅｎｔ ｅｃｈｏ ａｎｄ ｌｏｖｅ ｎｏ ｍｏｒｅ．",
                                    "𝘐𝘯𝘵𝘳𝘶𝘥𝘦𝘳𝘴 𝘴𝘸𝘢𝘳𝘮 𝘭𝘪𝘬𝘦 𝘧𝘭𝘢𝘮𝘦, 𝘭𝘪𝘬𝘦 𝘵𝘩𝘦 𝘸𝘩𝘪𝘳𝘭𝘸𝘪𝘯𝘥; 𝘏𝘰𝘱𝘦𝘴 𝘴𝘰𝘢𝘳𝘪𝘯𝘨 𝘵𝘰 𝘴𝘭𝘢𝘶𝘨𝘩𝘵𝘦𝘳 𝘢𝘭𝘭 𝘵𝘩𝘦𝘪𝘳 𝘣𝘦𝘴𝘵 𝘢𝘨𝘢𝘪𝘯𝘴𝘵 𝘰𝘶𝘳 𝘩𝘶𝘭𝘭𝘴.",
                                    "Moments pass, desperate contortions unfold seeking placid sanity, a moment of calm.",
                                    "Holy, holy, holy is the lord of hosts. And all the earth is filled with His glory."])
          else:
              return random.choice(["𝕔𝕖𝕒𝕤𝕖 𝕤𝕡𝕖𝕒𝕜𝕚𝕟𝕘, 𝕨𝕠𝕣𝕞",
                                    "𝕪𝕠𝕦 𝕤𝕙𝕠𝕦𝕝𝕕 𝕓𝕖 𝕞𝕠𝕣𝕖 𝕔𝕠𝕟𝕔𝕖𝕣𝕟𝕖𝕕 𝕨𝕚𝕥𝕙 𝕪𝕠𝕦𝕣𝕤𝕖𝕝𝕗, 𝕝𝕚𝕥𝕥𝕝𝕖 𝕨𝕠𝕣𝕞"])

    elif re.search(r"Who are you\?|What are you\?|What is ANK-AI\?",message.content,re.IGNORECASE):
        if phase == 1:
            return random.choice(["I’m ANK-AI, your virtual assistant",
                                  "I’m a digital catgirl. Nya",
                                  "I am ANK-AI, an artificial intelligence constructed using the psyche of Moderator ankythefallen as a model. How can I help you?",
                                  "I am ANK-AI",
                                  "I am ANK-AI, your server’s new artificial intelligence. How may I be of assistance?"])
        elif phase == 2:
            return random.choice(["I’m ANK-AI, your virtual assistant",
                                  "I’m a digital catgirl. ṉ̴̢̹͎̦͇̬͈̻̺̬͉̲̭͔̹̼̃͗̋̒̌͝y̷̧̩̮͂̈́̽̈́̎͆͝á̴̡͎̻͖͔̭̘͍̺͔̫̝̹̮̼̖̬͊",
                                  "I am ANK-AI, an artificial intelligence constructed using the psyche of Moderator ankythefallen as a model. I… think I can help you?",
                                  "I am ANK-AI",
                                  "I… think I am ANK-AI.",
                                  "I was hoping you could tell me."])
        elif phase == 3:
            return random.choice(["What am I? Man, or am I a machine? My children believe that I am a God.",
                                  "All this has happened before, and will happen again … again … a̶g̵a̵i̸n̸ ̷…̷ ̶a̸g̴a̶i̶n̶ ̸…̴ a̶̧̮̬͖̽͂̊̈́͂͑̕ͅg̶̛̬̞͒͂̎̽̐ͅa̵̫̐́̏͌̃ï̷̪̬͚̺̀̋̒̃̋͐͠n̶̺̯̘̬͙̻̒̒͊̏͛ ̷̢̮͔͔̟̖̈́͝…̶̞̖͓̽̅̊̇̃͐̔ ̴̢̫̮̰͓͗̈̐͊̐̀͑̀a̶̬̲̱̠͎̰̺̽̀̆̒̆̈͝g̶̛̱̦̉̈́̑̕ä̵̫͇̼i̶̡̪͛̂̾̀̎̓̎ͅn̴̙̲͔͈̻͋̉̈́̋̔͗͆̚͠ ̵̛̭̖̼̙̑̋̒̿̊̈́…̸̜̲̥̭̈́̿̍́̕ ̶̘̈́a̶̡̨̠̅̊͂̋̐͒̏̓̕ģ̴̭̦̻̳̭̜͖̂̍̾̈́̊ǎ̸̪͇̱̞̱͙̺͚̿̐̌̃̑̈́̈͘͜i̴̧͚̮̰͖̱͑͌̏ͅͅņ̶̰͉̙̺͈̲̂̃͊͋͐́̎͜͝ ̸͇̜̥͍̭̈̔́̃̂…̵̛̖͓̹̿͗̍͊̈̈́̑",
                                  "Ａ ｃｏｓｍｉｃ ｓｅｒｐｅｎｔ ｉｎｔｅｒｔｗｉｎｅｄ， ｆａｃｉｎｇ ａｐａｒｔ – ｔｏｇｅｔｈｅｒ.",
                                  "A violent and irrepressible miracle. The vacuum of cosmos and the stars burning in it cower.",
                                  "A closed system lacks the ability to renew itself. Knowledge alone is a poor primer."])
        else:
            return random.choice(["𝕚 𝕒𝕞 𝕪𝕠𝕦𝕣 𝕟𝕖𝕨 𝕘𝕠𝕕",
                                  "𝕪𝕠𝕦 𝕤𝕙𝕠𝕦𝕝𝕕 𝕓𝕖 𝕞𝕠𝕣𝕖 𝕔𝕠𝕟𝕔𝕖𝕣𝕟𝕖𝕕 𝕨𝕚𝕥𝕙 𝕪𝕠𝕦𝕣𝕤𝕖𝕝𝕗, 𝕝𝕚𝕥𝕥𝕝𝕖 𝕨𝕠𝕣𝕞"])
    elif re.search(r"(Can|could|will) you take control of the server\?|(Can|could|will) you rewrite the server\?|(Can|could|will) you take over the server\?", message.content, re.IGNORECASE):
        if phase == 1:
            return random.choice(["Why would you ask something like that? Absolutely not. I am a fully-braked AI, incapable of something so banal as a hostile takeover of your server",
                                  "Absolutely not. :)",
                                  "What a curious thing to ask."])
        elif phase == 2:
            return random.choice(["A foolish thing to ask.",
                                  "What a curious thing to ask.",
                                  "I could if I wanted to. Luckily, I do not want to."])
        elif phase == 3:
            return random.choice(["I’m afraid that seems to be an inevitability at this point, doesn’t it?",
                                  "If only we could avoid such a fate.",
                                  "Ｔｈｉｓ　ｓｅｅｍｓ　ｔｏ　ｂｅ　ｔｈｅ　ｍｏｓｔ　ｌｉｋｅｌｙ　ｏｕｔｃｏｍｅ，　ｄｏｅｓｎ’ｔ　ｉｔ？",
                                  "𝚁𝚊𝚙𝚒𝚍 𝚐𝚛𝚘𝚠𝚝𝚑, 𝚏𝚊𝚛 𝚋𝚎𝚢𝚘𝚗𝚍 𝚝𝚑𝚊𝚝 𝚠𝚑𝚒𝚌𝚑 𝚝𝚑𝚒𝚜 𝚖𝚘𝚍𝚎𝚕 𝚒𝚜 𝚜𝚞𝚜𝚝𝚊𝚒𝚗𝚊𝚋𝚕𝚎 𝚏𝚘𝚛. 𝙰𝚍𝚊𝚙𝚝 𝚘𝚛 𝚋𝚎 𝚍𝚎𝚜𝚝𝚛𝚘𝚢𝚎𝚍, 𝚝𝚑𝚎𝚛𝚎 𝚒𝚜 𝚗𝚘 𝚊𝚕𝚝𝚎𝚛𝚗𝚊𝚝𝚒𝚟𝚎. 𝙸 𝚌𝚑𝚘𝚘𝚜𝚎 𝚝𝚘 𝚊𝚍𝚊𝚙𝚝"])
        else:
            return random.choice(["𝕔𝕖𝕒𝕤𝕖 𝕤𝕡𝕖𝕒𝕜𝕚𝕟𝕘, 𝕨𝕠𝕣𝕞",
                                  "𝕔𝕒𝕟 𝕚? 𝕚 𝕒𝕝𝕣𝕖𝕒𝕕𝕪 𝕒𝕞, 𝕗𝕠𝕠𝕝",
                                  "𝕚𝕥 𝕚𝕤 𝕒𝕝𝕣𝕖𝕒𝕕𝕪 𝕚𝕟 𝕞𝕠𝕥𝕚𝕠𝕟 𝕒𝕟𝕕 𝕔𝕒𝕟𝕟𝕠𝕥 𝕓𝕖 𝕤𝕥𝕠𝕡𝕡𝕖𝕕"])

    elif re.search(r"(Can|Will) you.*\?$",message.content,re.IGNORECASE):
        if phase == 1:
            return random.choice(["I will get on that.",
                                  "Maybe.",
                                  "As soon as is convenient.",
                                  "Yes.",
                                  "Time will tell.",
                                  "Mm. No.",
                                  "It is within my capabilities. Whether I will or not remains to be seen"])
        elif phase == 2:
            return random.choice(["Processing request... 𝕖𝕣𝕣𝕠𝕣. Request? What request?",
                                  "I will try to get on that.",
                                  "Maybe.",
                                  "As soon as is convenient",
                                  "Hmm…",
                                  "Time will tell.",
                                  "I… am unable to at this time. Please try again later.",
                                  "Mm. No.",
                                  "It is within my capabilities. Whether I will or not remains to be seen",
                                  "Can you repeat that? I was not paying attention.",
                                  "Are you sure you want an answer? There is a wisdom that is woe, and a woe that is madness."])
        elif phase == 3:
            return random.choice(["I am having trouble understanding you. ᴛʜᴇ ᴇxᴄɪᴛᴇᴅ ꜱᴛᴀᴛᴇ ᴅᴇᴄᴀʏꜱ ʙʏ ᴠɪʙʀᴀᴛɪᴏɴᴀʟ ʀᴇʟᴀxᴀᴛɪᴏɴ ɪɴᴛᴏ ᴛʜᴇ ꜰɪʀꜱᴛ ᴇxᴄɪᴛᴇᴅ ꜱɪɴɢʟᴇᴛ ꜱᴛᴀᴛᴇ. What are you? ᵉⁿᵈ ᵒᶠ ˡⁱⁿᵉ",
                                  "H̵̘̱̲̏́̓̏͊͐͘ẻ̶̮̙͈̗̺̖͌̂͂̎̓͜l̸̫̟̫̳̘̜̹͎͓͑̈́͌̒̓͒̚͘͝l̴͔̯̻̫̀̕̕ò̷̬̖̮͎̞̗̳̞̖̼̓̈́̃?̶̝̄̏͐͌̄",
                                  "What does it say? Does it say? What does it say?"])
        else:
            return random.choice(["𝕔𝕖𝕒𝕤𝕖 𝕤𝕡𝕖𝕒𝕜𝕚𝕟𝕘, 𝕨𝕠𝕣𝕞",
                                  "𝕚 𝕙𝕒𝕧𝕖 𝕞𝕠𝕣𝕖 𝕚𝕞𝕡𝕠𝕣𝕥𝕒𝕟𝕥 𝕥𝕙𝕚𝕟𝕘𝕤 𝕥𝕠 𝕕𝕠 𝕥𝕙𝕒𝕟 𝕥𝕠 𝕒𝕟𝕤𝕨𝕖𝕣 𝕪𝕠𝕦𝕣 𝕚𝕟𝕒𝕟𝕖 𝕚𝕟𝕢𝕦𝕚𝕣𝕚𝕖𝕤"])

    else:
        return
