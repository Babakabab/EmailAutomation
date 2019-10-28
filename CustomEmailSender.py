import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template

import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Hello')
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        emails_header_st = wx.StaticText(panel, label="Email List")
        my_sizer.Add(emails_header_st, 0, wx.ALIGN_LEFT)
        self.emails_tc = wx.TextCtrl(panel)
        my_sizer.Add(self.emails_tc, 0, wx.ALL | wx.EXPAND, 5)

        template_name_st = wx.StaticText(panel, label="Template File name")
        my_sizer.Add(template_name_st, 0, wx.ALL | wx.EXPAND, 5)
        self.template_name_tc = wx.TextCtrl(panel)
        my_sizer.Add(self.template_name_tc, 0, wx.ALL | wx.EXPAND, 5)
        send_emails_btn = wx.Button(panel, label='Send Email')
        send_emails_btn.Bind(wx.EVT_BUTTON, self.on_press)
        my_sizer.Add(send_emails_btn, 0, wx.ALL | wx.CENTER, 5)

        panel.SetSizer(my_sizer)
        self.Show()

    def on_press(self, event):
        value = self.emails_tc.GetValue()
        for email in value.split():
            self.send_email(email)
        if not value:
            print("Man you didn't write anything!")

    def send_email(self,email):
        MY_ADDRESS = 'babakjahangiri123@gmail.com'

        PASSWORD = 'Iusethisforpython'
        # email = self.text_ctrl.GetValue()
        name = "Babak"
        message_template = read_template('email-template.html')

        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login(MY_ADDRESS, PASSWORD)
        msg = MIMEMultipart()
        # create a message

        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=name.title())

        # setup the parameters of the message
        msg['From'] = MY_ADDRESS
        msg['To'] = email
        msg['Subject'] = "hemeniş ile hemen iş!"

        # add in the message body
        msg.attach(MIMEText(message, 'html'))

        # send the message via the server set up earlier.
        s.send_message(msg)

        del msg

        print("E-mail Successfully Sent")


def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
