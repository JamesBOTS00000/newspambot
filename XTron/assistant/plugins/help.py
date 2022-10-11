from telethon import events, Button

HELP_PIC = "https://te.legra.ph/file/f07857daaad3426175943.jpg"
Riz_Help = "===== HELP MENU OF XTron ===== \n\n **Basic Commamds:** \n `/ping` \n `/alive` \n\n **Click On Below Buttons for help.**"

@Tron.on(events.NewMessage(pattern="[!/]help"))
async def bot_help(event):
   if event.sender_id in SUDO_USERS or event.sender_id in DEV:
       await Tron.send_file(event.chat_id, 
                                HELP_PIC, 
                                caption=Riz_Help, 
                                buttons=[
           [
           Button.url("✘ OWNER ✘", "https://t.me/Rst_Bots")
           ],
           [
           Button.inline("✘ COMMANDS ✘", data="available")
           ],
           ],
           ) 
                   
dm_msg = f"""
** Dm Commands**

__Usage__: Send Commands In Your Assistant's pm and Follow The Instructions Which Your assistant give you !


**Send Dm Message:** `/dm`

**Start Dm Spam:** `/dmspam`

**Start Dm Raid:** `/dmraid`
"""

joinleave_msg = f"""
**Join Leave Commands**

__Usage__: Send Commands In Your Assistant's pm and Follow The Instructions Which Your assistant give you !


**Join Group/Channel:** `/join`

**Join Private Group/Channel:** `/pjoin`

**Leave Group/Channels:** `/leave`
"""
           
userbot_msg = f"""
**Userbot Commands**

__Usage__: Send Commands In Your Assistant's pm and Follow The Instructions Which Your assistant give you !


**Check Ping/uptime**: `/ping`

**Check Alive Version**: `/alive`

**Restart Bots:** `/restart`

**Add Echo:** `/addecho`

**Remove Echo:** `/rmecho`

**Get stats:** `/stats`

**Members adding:** `/scrape`

**Add Sudo**: `/addsudo` 

**Add Full Sudo**: `/fullsudo`
"""

profile_msg = """
**Profile Cmds**

__Usage__: Send Commands In Your Assistant's pm and Follow The Instructions Which Your assistant give you !


**Change Name:** `/setname`

**Change Pic:** `/setpic`

**Change Bio:** `/setbio`
"""

raid_msg = f"""
** Raid Commands**

__Usage__: Send Commands In Your Assistant's pm and Follow The Instructions Which Your assistant give you !


**Activates Raid:** `/raid`

**Deactivates Raid:** `/delayraid`

**Activates Reply Raid:** `/replyraid`

**Deactivates Reply Raid:** `/dreplyraid`
"""


spam_msg = f"""
** Spam Commands**

__Usage__: Send Commands In Your Assistant's pm and Follow The Instructions Which Your assistant give you !


**Activates Raid:** `/raid`

**Deactivates Raid:** `/delayraid`

**Activates Reply Raid:** `/replyraid`

**Deactivates Reply Raid:** `/dreplyraid`
"""


@Tron.on(events.CallbackQuery(pattern=r"help_back"))
async def help_back(event):
    if event.query.user_id in SUDO_USERS or event.query.user_id in DEV:
        await event.edit(
            Riz_Help,
            buttons=[
               [
               Button.inline("✘ UserBot ✘", data="userbot"),
               Button.inline("✘ Profile ✘", data="profile")
               ],
               [
               Button.inline("✘ Spam ✘", data="spam"),
               Button.inline("✘ Raid ✘", data="raid")
               ],
               [
               Button.inline("✘ Join/Leave ✘", data="joinleave"),
               Button.inline("✘ DM ✘", data="dm")
               ],
               ],
               )
    else:
        Alert = (
                "Noob !! Make Your Own XTron Bot !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)

           
@Tron.on(events.CallbackQuery(pattern=r"available"))
async def raid_msgg(event):
    if event.query.user_id in SUDO_USERS or event.query.user_id in DEV:
        await event.edit("__Click Below Button To Know cmds__",
           buttons=[
               [
               Button.inline("✘ UserBot ✘", data="userbot"),
               Button.inline("✘ Profile ✘", data="profile")
               ],
               [
               Button.inline("✘ Spam ✘", data="spam"),
               Button.inline("✘ Raid ✘", data="raid")
               ],
               [
               Button.inline("✘ Join/Leave ✘", data="joinleave"),
               Button.inline("✘ DM ✘", data="dm")
               ],
               ],
               )
    else:
        Alert = (
                "Noob !! Make Your Own XTron Bot !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)


@Tron.on(events.CallbackQuery(pattern=r"raid"))
async def spam_msgg(event):
    if event.query.user_id in SUDO_USERS or event.query.user_id in DEV:
        await event.edit(
            raid_msg,
            buttons=[
                [
            Button.inline("< Back", data="help_back")
             ], ], )
    else:
        Alert = (
                "Noob !! Make Your Own XTron Bot !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)
  
@Tron.on(events.CallbackQuery(pattern=r"profile"))
async def spam_msgg(event):
    if event.query.user_id in SUDO_USERS or event.query.user_id in DEV:
        await event.edit(
            profile_msg,
            buttons=[
                [
            Button.inline("< Back", data="help_back")
             ], ], )
    else:
        Alert = (
                "Noob !! Make Your Own XTron Bot !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)
        
        
@Tron.on(events.CallbackQuery(pattern=r"dm"))
async def spam_msgg(event):
    if event.query.user_id in SUDO_USERS or event.query.user_id in DEV:
        await event.edit(
            dm_msg,
            buttons=[
                [
            Button.inline("< Back", data="help_back")
             ], ], )
    else:
        Alert = (
                "Noob !! Make Your Own XTron Bot !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)
      

@Tron.on(events.CallbackQuery(pattern=r"joinleave"))
async def raid_msgg(event):
    if event.query.user_id in SUDO_USERS or event.query.user_id in DEV:
        await event.edit(
            joinleave_msg,
            buttons=[
                [
            Button.inline("< Back", data="help_back")
             ], ], )
    else:
        Alert = (
                "Noob !! Make Your Own XTron Bot !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)


@Tron.on(events.CallbackQuery(pattern=r"spam"))
async def raid_msgg(event):
    if event.query.user_id in SUDO_USERS or event.query.user_id in DEV:
        await event.edit(
            spam_msg,
            buttons=[
                [
            Button.inline("< Back", data="help_back")
             ], ], )
    else:
        Alert = (
                "Noob !! Make Your Own XTron Bot !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)


@Tron.on(events.CallbackQuery(pattern=r"userbot"))
async def userbot_msgg(event):
    if event.query.user_id in SUDO_USERS or event.query.user_id in DEV:
        await event.edit(
            userbot_msg,
            buttons=[
                [
            Button.inline("< Back", data="help_back")
                ],
                ],
                )
    else:
        Alert = (
                "Noob !! Make Your Own XTron Bot !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)
