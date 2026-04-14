import smtplib
import random

# Generate OTP
otp = str(random.randint(100,200))
print("OTP (for testing):", otp)

# Email details
sender_email = "babusuram64@gmail.com"
password = "hgwrnqnlfrmtbhxc"
receiver_email = input("Enter your email: ")

# Message
message = f"Subject: OTP\n\nYour OTP is: {otp}"

# Send email
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, password)
server.sendmail(sender_email, receiver_email, message)
server.quit()

print("OTP sent!")

# Verify OTP
user_otp = input("Enter OTP: ")

if user_otp == otp:
    print("Verified ✅")
else:
    print("Wrong OTP ❌")
