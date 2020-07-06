from whatsapp import WhatsApp
msg = """	*laughing*  :-) 
	neutral_face :-| _stuck_out_tongue_  :-p
	~heart~  <3  simple_smile :-) 
	*worried* :-( (n) 
	thumbsup (y) wink ;-) """
wapp = WhatsApp(100, session='my')
wapp.send_message('Aahnik Personal', msg)
