def monitor_uptime(url, recipients=None, gmail_user=None, gmail_pass=None):
    """
    Monitor a url to see if it is online. If it is does not return a 200 code, 
    then (optionally) send an email out through GMail.
    
    Example::
        monitor_uptime("http://www.google.com/", 
                    ["to_address@example.com", "3334445555@txt.att.net"], 
                    "example@gmail.com", 
                    "my_gmail_password")
    """
    from datetime import datetime, timedelta
    import httplib
    from urlparse import urlparse
    
    color_print("\nChecking if %s is online" % url, 'green')
    
    # Connect to the url and get it's status and other details.
    site = urlparse(url)
    conn = httplib.HTTPConnection(site[1])
    conn.request("HEAD", site[2])
    status = conn.getresponse()
    status_code = status.status
    
    # Get the clean URL (without protocol)
    full_url = site.geturl()
    clean_url = site.netloc + site.path
    
    # If the request was anything but a 200/302 code (meaning the site is up), 
    # log and report the downtime.
    if status_code != 200 and status_code != 302:
        
        color_print("\nSite is down with a %s error code\n" % status_code, 'red')
        
        # If they have set up email sending, send out a message.
        if recipients and gmail_user and gmail_pass:
            
            # Construct the subject and message.
            subject = "Server is down!"
            msg_text = """%(site)s is down with status code %(code)s!""" % {
                'site': full_url,
                'code': status_code,
            }
            
            # Send the message to all the recipients.
            recipients = recipients if not isinstance(recipients, basestring) else [recipients]
            for to_address in recipients:
                mail(gmail_user, gmail_pass, to_address, subject, msg_text)
            color_print("\nNotification sent!\n", 'green')
            
        # Return False so that we can do something if the site is down.
        return False
    
    # If the status_code is 200, then the site is up
    color_print("\nSite is online (status 200)!\n", 'green')
    
    # Return true if 
    return True
