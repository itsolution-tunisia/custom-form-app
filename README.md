# To Use:
Add registration form custom filds {favorite movie(text), favorite_editor(Select)} 
# 1. Install

`sudo su - edxapp -s /bin/bash`

`cd ~/`

`. edxapp_env`

`git clone https://github.com/itsolution-tunisia/custom-form-app`

`pip install -e custom-form-app`

# 2. Migrate DB

`cd /edx/app/edxapp/edx-platform`

`python /edx/app/edxapp/edx-platform/manage.py lms makemigrations custom_reg_form --settings=production`

`python /edx/app/edxapp/edx-platform/manage.py lms migrate custom_reg_form --settings=production`

`exit`

# 3. Add parameters
In /edx/etc/lms.yml file:

```
ADDL_INSTALLED_APPS: ["custom_reg_form"]
REGISTRATION_EXTENSION_FORM: custom_reg_form.forms.ExtraInfoForm
```
# 4. Restart LMS and EDX

`sudo /edx/bin/supervisorctl restart lms`

`sudo /edx/bin/supervisorctl restart edxapp_worker:`

# 5. Form fields translation

In en/LC_MESSAGES/django.po file:

```
msgid "Organization/Institution name"
msgstr ""

msgid "Please tell us your telephone number."
msgstr ""

msgid "Invalid telephone number."
msgstr ""

msgid "Phone number"\n
msgstr ""
```

In ar/LC_MESSAGES/django.po file:

```
msgid "Organization/Institution name"
msgstr "اسم المنظمة/المؤسسة"

msgid "Please tell us your telephone number."
msgstr "من فضلك أدخل رقم هاتفك."

msgid "Invalid telephone number."
msgstr "رقم الهاتف غير صحيح."

msgid "Phone number"
msgstr "رقم الهاتف"
```
