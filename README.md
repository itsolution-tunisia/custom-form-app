# To Use:
Install
sudo su - edxapp -s /bin/bash
cd ~/
. edxapp_env
git clone https://github.com/open-craft/custom-form-app
pip install -e custom-form-app

vi /edx/app/edxapp/custom-form-app/custom_reg_form/models.py
->     user = models.OneToOneField(USER_MODEL, null=True, on_delete=models.PROTECT)
vi /edx/app/edxapp/custom-form-app/custom_reg_form/migrations/0001_initial.py
->                ('user', models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT)),

Add parameters
In lms.env.json file:
"ADDL_INSTALLED_APPS": ["custom_reg_form"] to the root node.
"REGISTRATION_EXTENSION_FORM": "custom_reg_form.forms.ExtraInfoForm"
Migrate DB
cd /edx/app/edxapp/edx-platform
python /edx/app/edxapp/edx-platform/manage.py lms syncdb --migrate --settings=production
python /edx/app/edxapp/edx-platform/manage.py lms makemigrations custom_reg_form --settings=production
Restart edxapp
sudo /edx/bin/supervisorctl restart edxapp:
# To Use:

1. Install with `pip install -e .` within this folder within the edx platform virtual environment.
2. Add "custom_reg_form" to the "ADDL_INSTALLED_APPS" array in `lms.env.json` (you may have to create it if it doesn't exist.)
3. Set "REGISTRATION_EXTENSION_FORM" to "custom_reg_form.forms.ExtraInfoForm" in `lms.env.json`.
4. Run migrations.
5. Start/restart the LMS.
