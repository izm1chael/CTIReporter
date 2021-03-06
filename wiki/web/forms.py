"""
    Forms
    ~~~~~
"""
from flask_wtf import FlaskForm
from wtforms import BooleanField
try:
    from wtforms import StringField as StringField
except ImportError:
    from wtforms import TextField as StringField
from wtforms import TextAreaField, SelectField
from wtforms import PasswordField
from wtforms.validators import InputRequired
from wtforms.validators import ValidationError
from wtforms.fields import DateField
from datetime import datetime


from wiki.core import clean_url
from wiki.web import current_wiki
from wiki.web import current_users


class URLForm(FlaskForm):
    url = StringField('', [InputRequired()])

    def validate_url(form, field):
        if current_wiki.exists(field.data):
            raise ValidationError('The URL "%s" exists already.' % field.data)

    def clean_url(self, url):
        return clean_url(url)


class SearchForm(FlaskForm):
    term = StringField('', [InputRequired()])
    ignore_case = BooleanField(
        description='Ignore Case',
        # FIXME: default is not correctly populated
        default=True)


class EditorForm(FlaskForm):
    title = StringField('Report Title', [InputRequired()])
    date = StringField('Date of Report (YYYY-MM-DD)', [InputRequired()])
    apt_number = StringField('APT Number (APTXX)')
    apt_name = StringField('APT Name')
    body = TextAreaField('Your Report (In Markdown)', [InputRequired()])
    threat_level = SelectField(
        choices=[
            ('Low', 'Low'),
            ('Moderate', 'Moderate'),
            ('Substantial', 'Substantial'),
            ('Severe', 'Severe'),
            ('Critical', 'Critical'),
        ]
    )
    business_impact = SelectField(
        choices=[
            ('Low', 'Low'),
            ('Moderate', 'Moderate'),
            ('Substantial', 'Substantial'),
            ('Severe', 'Severe'),
            ('Critical', 'Critical'),
        ]
    )
    ips = StringField('List all IP Addresses')
    domains = StringField('List all domains names')
    filehashes = StringField('List all file hashes ')
    cves = StringField('List the assocoaited CVEs')
    tags = StringField('Your Tags (Comma Separated)')



class LoginForm(FlaskForm):
    name = StringField('', [InputRequired()])
    password = PasswordField('', [InputRequired()])

    def validate_name(form, field):
        user = current_users.get_user(field.data)
        if not user:
            raise ValidationError('This username does not exist.')

    def validate_password(form, field):
        user = current_users.get_user(form.name.data)
        if not user:
            return
        if not user.check_password(field.data):
            raise ValidationError('Username and password do not match.')
