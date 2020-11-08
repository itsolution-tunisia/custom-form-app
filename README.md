# To Use:
1. Install

`sudo su - edxapp -s /bin/bash`
`cd ~/`
`. edxapp_env`
`git clone https://github.com/itsolution-tunisia/custom-form-app`
`pip install -e custom-form-app`

Note:
to fix some migration error
`vi /edx/app/edxapp/custom-form-app/custom_reg_form/models.py`
->     user = models.OneToOneField(USER_MODEL, null=True, on_delete=models.PROTECT)
`vi /edx/app/edxapp/custom-form-app/custom_reg_form/migrations/0001_initial.py`
->                ('user', models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT)),

2. Add parameters
In /edx/etc/lms.yml file:
`ADDL_INSTALLED_APPS: ["custom_reg_form"]
REGISTRATION_EXTENSION_FORM: custom_reg_form.forms.ExtraInfoForm`

3. Migrate DB
`cd /edx/app/edxapp/edx-platform
python /edx/app/edxapp/edx-platform/manage.py lms syncdb --migrate --settings=production
python /edx/app/edxapp/edx-platform/manage.py lms makemigrations custom_reg_form --settings=production`

4. Restart LMS
`sudo /edx/bin/supervisorctl restart lms`
