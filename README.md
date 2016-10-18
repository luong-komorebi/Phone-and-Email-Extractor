## Phone and Email Extractor

This is a small python script to extract email and phone number from Clipboard.  
So far it only supports phone number in the United States.

### Purpose

Fun and Practice Python Skill.  

### Usage 

Either use the makefile or run ```pip install -r requirements.txt```   
Then copy some texts to the clipboard using Control + C or RightMouse->Copy  
Run ```python phoneAndEmail.py``` and you will get the results

### Example

Text copied:   
``` 
Contact Us
No Starch Press, Inc.
245 8th Street
San Francisco, CA 94103 USA
Phone: 800.420.7240 or +1 415.863.9900 (9 a.m. to 5 p.m., M-F, PST)
Fax: +1 415.863.9950
Reach Us by Email
General inquiries: info@nostarch.com
Media requests: media@nostarch.com
Academic requests: academic@nostarch.com (Please see this page for academic review requests)
Help with your order: info@nostarch.com
Reach Us on Social Media
Twitter
Facebook
```

Text returned: 
![](http://i.imgur.com/Oq8hCBK.png)
