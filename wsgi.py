# _*_ coding:utf-8 _*_
# Project Name: watchlist
# File Name: wsgi
# Author： rockche
# Date:  2020/12/10  4:20 下午
# Description :
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from watchlist import app