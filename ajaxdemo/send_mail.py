# coding=utf-8
import os
import smtplib
import logging

from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

__author__ = 'xiangpeng'

FROM_USER = "xiangpeng339@sina.com"
FROM_PSD = "XIANGP152"
TO_USER = "339075196@qq.com"
LOGGER = logging.getLogger(__name__)
print __name__

def is_mobi(file_path):
    """判断是否是mobi
    判断是否是mobi格式的文件，不区分大小写，kindle只支持mobi的推送。pdf格式的不考虑，支持太差
    :param file_path:文件路径
    :return:无
    """
    base_name = os.path.basename(file_path)
    file_name = base_name.split(".")[-1]
    if file_name.lower == "mobi":
        return True
    return False


def send_mail(file_path):
    """发送邮件
    把文件目录所指向的文件作为附件发送到指定的邮箱
    :param file_path:
    :return:
    """
    msg = MIMEMultipart()
    # 打开文件
    if file_path != "" and os.path.exists(file_path):
        fp = open(file_path, "rb")
        att = MIMEText(fp.read(), 'base64', 'gb2312')
        att["Content-Type"] = 'application/octet-stream'
        att_header = Header(os.path.basename(file_path), 'utf-8')
        att.add_header('Content-Disposition', 'attachment; filename="%s"' % att_header)
        msg.attach(att)
        fp.close()

    # 构造邮件体
    msg['Subject'] = "test"
    msg['From'] = FROM_USER
    msg['To'] = TO_USER

    # 发送邮件
    try:
        s = smtplib.SMTP("smtp.sina.com")
        # print s.login(FROM_USER, FROM_PSD)
        # print s.sendmail(FROM_USER, TO_USER, msg.as_string())
        LOGGER.info("send " + os.path.basename(file_path) + " to " + TO_USER)
        s.quit()
    except IOError, e:
        LOGGER.error(e)


if __name__ == '__main__':
    pass