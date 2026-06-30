# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# def send_warning_email(item_name, items_left):
#     # --- CHANGE THESE 3 LINES ---
#     sender_email = "jassuyeddula@gmail.com" 
#     sender_password = "hulkuhyzupcbrfbz" 
#     receiver_email = "jaswanthyeddula31@gmail.com" 
#     # ----------------------------

#     msg = MIMEMultipart()
#     msg['From'] = sender_email
#     msg['To'] = receiver_email
#     msg['Subject'] = f"⚠️ LOW STOCK ALERT: {item_name}"

#     body = f"""
#     Hello,
    
#     This is an automated alert.
    
#     The stock for '{item_name}' is critically low .
    
#     Current Quantity: {items_left}
    
#     Please restock this item immediately.
#     """
#     msg.attach(MIMEText(body, 'plain'))

#     try:
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls() 
#         server.login(sender_email, sender_password)
#         server.send_message(msg)
#         server.quit()
#         print(f"SUCCESS: Email sent for {item_name}")
#     except Exception as e:
#         print(f"ERROR: Failed to send email. Details: {e}")
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# We added 'supplier_email' as the third parameter here
def send_warning_email(item_name, items_left, supplier_email):
    sender_email = "jassuyeddula@gmail.com"
    # Remember to use your NEW App Password!
    sender_password = "szfwozxiniihjyzt" 
    
    body = f"""
Hello,
This is an automated alert.
The stock for '{item_name}' is critically low.
Current Quantity: {items_left}
Please restock this item immediately.
"""

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = supplier_email  # We use that parameter right here
    msg['Subject'] = f"LOW STOCK ALERT: {item_name}"
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        print(f"SUCCESS: Email sent to {supplier_email} for {item_name}")
    except Exception as e:
        print(f"ERROR: Failed to send email. Details: {e}")