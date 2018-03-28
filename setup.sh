#!/bin/bash

path="$( cd "$(dirname "$0")" ; pwd -P )"

echo -e "Welcome to Marc's Django Rest Cookie Cutter!"
echo -e "Please enter Project Name"
read project_name

cat <<EOF >> ./marcs-django-rest-cookie-cutter/cookiecutter.json
{"project_name" : "$project_name",
 "_copy_without_render": [
 		"apps/management/*"
    ]
}
EOF

echo -e "Creating django project..."
cookiecutter $path --no-input
echo -e "Done."

rm $path/cookiecutter.json

cd $project_name

echo -e "Creating Virtual environment..."
virtualenv -p python3 venv >/dev/null
echo -e "Done."

source venv/bin/activate

echo -e "Installing project requirements (this may take awhile) ..."
pip install -r requirements.txt >/dev/null
echo -e "Done."

echo -e "Migrating..."
./manage.py makemigrations >/dev/null
./manage.py migrate >/dev/null
echo -e "Done."

deactivate

echo -e "All Done! cd into the directory and activate the venv to start."