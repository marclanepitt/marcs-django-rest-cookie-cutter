
from django.core.management.templates import TemplateCommand
import os

class Command(TemplateCommand):
	help = (
		"Creates a Django rest app directory structure for the given app name in "
		"the app directory"
	)
	missing_args_message = "You must provide an application name."

	def handle(self, **options):
		base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		app_name = options.pop('name')
		target = "./apps"
		template = base+"/restapp_template"
		options['template'] = template
		super().handle('app', app_name, target, **options)