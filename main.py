# Install python-docx library to read docx files
#pip install python-docx

# Install PyPDF2 library to read pdf files
#pip install PyPDF2

# Install pyautogen library to enable LLM applications based on multi-agent conversations
#pip install pyautogen

# Install telethon library to create the userbot that sends an invitation message
#pip install telethon


import extract_text_from_file as etff
import GPT_cmd as GC
import send_msg_telegram as smt

# Extract text from CV example
CV_file_path = 'example_CV1.docx'
CV_text = etff.extract_text_from_docx(CV_file_path)

# Extract command text for ChatGPT to generate an individual invitation
invite_GPT_file_path = 'invite_cmd_ChatGPT.docx'
invite_GPT = etff.extract_text_from_docx(invite_GPT_file_path)

# Extract command text for ChatGPT to detect telegram address
detect_tg_GPT_file_path = 'detect_tg_cmd_ChatGPT.docx'
detect_tg_GPT = etff.extract_text_from_docx(detect_tg_GPT_file_path)


# Status message
print()
print("-----Request to generate a letter-----")

# Command ChatGPT to generate an individual invitation
invite_txt = GC.GPT_cmd_fcn(invite_GPT+CV_text)

# Print the individual invitation to the console
print(invite_txt)

# Status message
print()
print("-----Request to detect Telegram address-----")

# Command ChatGPT to generate an individual invitation
tg_address_CV = GC.GPT_cmd_fcn(detect_tg_GPT+CV_text)

# Status message
print()
print("-----Sending the message to candidate's telegram-----")

# Print the Telegram address to the console
print(tg_address_CV)

# Send the individual invitation to the candidate via Telegram
smt.send_msg_telegram(tg_address_CV, invite_txt)

# Status message
print()
print("-----Completed-----")