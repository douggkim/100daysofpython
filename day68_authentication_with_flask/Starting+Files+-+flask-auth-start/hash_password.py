from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_login import UserMixin


class HashPassword():
    def __init__(self, db_directory: str):
        db = sqlite3.connect("db_directory")
        self.engine = create_engine(f"sqlite+pysqlite:///:memory:{db_directory}", echo=True, future=True)
        self.Session = sessionmaker(self.engine)



    def encrypt(self, class_name):
        data_list = self.Session.query(class_name).all()

        for data in data_list:
            data.password = generate_password_hash(data.password, method='pbkdf2:sha256', salt_length=8)
            self.Session.commit()


hashpassword = HashPassword("users.db")
hashpassword.encrypt(self.User)
