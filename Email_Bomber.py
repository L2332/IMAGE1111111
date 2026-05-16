#!/usr/bin/env python3

import smtplib
import time
import random
import sys
import os
import glob
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from colorama import Fore, Style, init

init(autoreset=True)

# ==================== YOUR CREDENTIALS ====================
SENDER_EMAIL = "tyranroot@gmail.com"
SENDER_PASSWORD = "ytnu gkoi gwvr vqqb"
# ============================================================

# ==================== IMAGE SETTINGS ====================
# Set this to a folder containing .jpg/.png images to attach
# Set to "" or None to disable image sending
IMAGE_FOLDER = "IMAGE_FOLDER"  # <-- CHANGE THIS to your image folder path
# ============================================================

# ==================== MESSAGE BODIES ====================
MESSAGE_BODIES = [
    "⚠️ Security Alert: Unauthorized access detected.🙂",
    "🔐 Your account has been compromised. Change password immediately.😄",
    "💀 This is a security test. No action needed. Testing fuck You🤣",
    "🎯 Important: Your login credentials were found in a data breach.",
    "🌑 Your data has been secured. Thank you for your cooperation.",
    "🔥 Our systems detected unusual activity from your IP.",
    "📡 This is an automated security notification.",
    "⚡ Action required: Verify your email address.",
    "🕷️ A new device logged into your account.",
    "🎭 Your privacy is important to us. Please review our policy.",
    "🔓 Security update: Two-factor authentication now available.",
    "📀 Your account has been flagged for review.",
    "⚙️ System maintenance scheduled for tonight.",
    "🎪 Welcome to our security awareness program.",
    "🔮 CHEATER KANG KUPAL KA HA! YARE SAKEN MGA ACCOUNT MO! PATI INFO MO.",
    "✅ CHEATER KANG KUPAL KA HA! YARE SAKEN MGA ACCOUNT MO! PATI INFO MO.",
    "📧 CHEATER KANG KUPAL KA HA! YARE SAKEN MGA ACCOUNT MO! PATI INFO MO.",
    "🔒 CHEATER KANG KUPAL KA HA! YARE SAKEN MGA ACCOUNT MO! PATI INFO MO.",
    "⚠️ CHEATER KANG KUPAL KA HA! YARE SAKEN MGA ACCOUNT MO! PATI INFO MO.",
    "🛡️ CHEATER KANG KUPAL KA HA! YARE SAKEN MGA ACCOUNT MO! PATI INFO MO. 😎.",
    "CHEATER KANG KUPAL KA HA! YARE SAKEN MGA ACCOUNT MO! PATI INFO MO.",
]

SUBJECTS = [
    "Security Alert",
    "Account Notification",
    "Important Security Update",
    "System Report",
    "Action Required",
    "Security Breach Alert",
    "Account Activity Report",
    "Security Test",
    "Notification from Security Team",
    "Alert: Unusual Activity",
    "CHEATER ALERT",
    "PICTURE NI BEBE NYA",
]


def load_image_list():
    """Load list of image files from the configured folder"""
    if not IMAGE_FOLDER:
        return []
    
    if not os.path.isdir(IMAGE_FOLDER):
        print(f"{Fore.YELLOW}[!] Image folder '{IMAGE_FOLDER}' not found. Images disabled.{Style.RESET_ALL}")
        return []
    
    # Supported image extensions
    extensions = ['*.jpg', '*.jpeg', '*.png', '*.gif', '*.bmp', '*.webp']
    images = []
    for ext in extensions:
        images.extend(glob.glob(os.path.join(IMAGE_FOLDER, ext)))
        images.extend(glob.glob(os.path.join(IMAGE_FOLDER, ext.upper())))
    
    if not images:
        print(f"{Fore.YELLOW}[!] No images found in '{IMAGE_FOLDER}'. Images disabled.{Style.RESET_ALL}")
        return []
    
    print(f"{Fore.GREEN}[✓] Loaded {len(images)} images from '{IMAGE_FOLDER}'{Style.RESET_ALL}")
    return images


def attach_image(msg, image_path):
    """Attach an image to the email"""
    try:
        with open(image_path, 'rb') as f:
            img_data = f.read()
        
        # Determine image type from extension
        ext = os.path.splitext(image_path)[1].lower()
        mime_type = {
            '.jpg': 'jpeg', '.jpeg': 'jpeg',
            '.png': 'png',
            '.gif': 'gif',
            '.bmp': 'bmp',
            '.webp': 'webp',
        }.get(ext, 'jpeg')
        
        image = MIMEImage(img_data, _subtype=mime_type)
        image.add_header('Content-Disposition', 'attachment',
                         filename=os.path.basename(image_path))
        msg.attach(image)
        return True
    except Exception as e:
        return False


def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')


def banner():
    clear_screen()
    print(f"""{Fore.MAGENTA}{Style.BRIGHT}
                                                                    
                ███╗   ██╗ ██████╗ ██╗  ██╗██╗   ██╗
                ████╗  ██║██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝
                ██╔██╗ ██║██║   ██║ ╚███╔╝  ╚████╔╝ 
                ██║╚██╗██║██║   ██║ ██╔██╗   ╚██╔╝  
                ██║ ╚████║╚██████╔╝██╔╝ ██╗   ██║   
                ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝        
                    
                  Ethical Email Testing | N0XY                    
                                                                     
{Style.RESET_ALL}""")
    print(f"{Fore.YELLOW}{Style.BRIGHT}[!] Use only on YOUR OWN email!{Style.RESET_ALL}")
    print(f"{Fore.CYAN}[✓] Rate Limit: Auto-protected | Delay: 3-5 sec{Style.RESET_ALL}\n")


def send_email(server, recipient, subject, body, image_list=None):
    """Send a single email with optional image attachment"""
    try:
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = recipient
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))
        
        # Attach random image if available
        if image_list:
            image_path = random.choice(image_list)
            attach_image(msg, image_path)
        
        server.sendmail(SENDER_EMAIL, recipient, msg.as_string())
        return True
    except Exception as e:
        return False


def main():
    banner()
    
    # Load images
    image_list = load_image_list()
    images_enabled = len(image_list) > 0
    if images_enabled:
        print(f"{Fore.CYAN}[+] Image attachment: ENABLED ({len(image_list)} images){Style.RESET_ALL}")
    else:
        print(f"{Fore.YELLOW}[+] Image attachment: DISABLED (no images found){Style.RESET_ALL}")
    
    print(f"{Fore.CYAN}{Style.BRIGHT}[+] Gmail SMTP Ready{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[✓] Logged in as: {SENDER_EMAIL}{Style.RESET_ALL}")
    
    print(f"\n{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
    
    recipient = input(f"{Fore.CYAN}[>] Target email: {Style.RESET_ALL}").strip()
    
    print(f"{Fore.YELLOW}[!] Daily Gmail limit: 50-500 emails{Style.RESET_ALL}")
    count = int(input(f"{Fore.CYAN}[>] Number of emails: {Style.RESET_ALL}").strip())
    
    if count > 500:
        print(f"{Fore.YELLOW}[!] Gmail limit is 500 per day. Reducing to 500.{Style.RESET_ALL}")
        count = 500
    elif count > 50:
        print(f"{Fore.YELLOW}[⚠] Over 50 may trigger rate limit. Continue anyway? (y/n): {Style.RESET_ALL}", end="")
        if input().lower() != 'y':
            print(f"{Fore.GREEN}[+] Cancelled.{Style.RESET_ALL}")
            return
    
    print(f"\n{Fore.RED}{Style.BRIGHT}[!] Sending {count} emails to {recipient}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}[*] Auto-delay: 3-5 seconds (avoid rate limit){Style.RESET_ALL}\n")
    
    confirm = input(f"{Fore.RED}[?] This is YOUR OWN email? (yes/no): {Style.RESET_ALL}")
    if confirm.lower() != 'yes':
        print(f"{Fore.GREEN}[+] Cancelled.{Style.RESET_ALL}")
        return
    
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        print(f"{Fore.GREEN}[✓] SMTP Connected{Style.RESET_ALL}\n")
    except Exception as e:
        print(f"{Fore.RED}[✗] Connection failed: {e}{Style.RESET_ALL}")
        return
    
    success = 0
    failed = 0
    rate_limit_hit = False
    
    for i in range(1, count + 1):
        subject = random.choice(SUBJECTS)
        body = random.choice(MESSAGE_BODIES)
        
        if send_email(server, recipient, f"{subject} [ID: {i}]", body, image_list if images_enabled else None):
            success += 1
            img_status = f" + img" if images_enabled else ""
            print(f"{Fore.GREEN}[✓] Email {i}/{count} sent{img_status}{Style.RESET_ALL}")
        else:
            failed += 1
            print(f"{Fore.RED}[✗] Email {i}/{count} failed{Style.RESET_ALL}")
            
            if failed > 3:
                print(f"{Fore.YELLOW}[⚠] Rate limit detected! Stopping to avoid ban.{Style.RESET_ALL}")
                rate_limit_hit = True
                break
        
        # Dynamic delay
        delay = 5 if i > 40 else 3
        time.sleep(delay)
    
    server.quit()
    
    print(f"\n{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[✓] COMPLETED: {success} sent, {failed} failed{Style.RESET_ALL}")
    
    if rate_limit_hit:
        print(f"{Fore.YELLOW}[⚠] Rate limit reached. Wait 24 hours before next test.{Style.RESET_ALL}")
    else:
        print(f"{Fore.GREEN}[✓] All emails sent successfully!{Style.RESET_ALL}")
    
    print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[!] Stopped{Style.RESET_ALL}")