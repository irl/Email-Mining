import imaplib
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('jaminy1234@gmail.com', 'thayapraba')
mail.list()
mail.select("inbox") # connect to inbox.

result, data = mail.search(None, "ALL")
 
ids = data[0] # data is a list.
id_list = ids.split() # ids is a space separated string
latest_email_id = id_list[-1] # get the latest
 
result, data = mail.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID
 
raw_email = data[0][1] 