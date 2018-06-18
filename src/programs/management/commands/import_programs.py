from django.core.management.base import LabelCommand
from csv import DictReader

from programs.models import Contact, Organization, Program
from programs.importer import split_dicts


class Command(LabelCommand):
    args = "<csv program file>"
    help = "Idempotently import programs, organizations and contacts from a CSV"

    DICTS = ['program', 'organization', 'contact']

    def handle_label(self, file, **options):
        print(f"Loading from file {file} ...")
        with open(file) as csvfile:
            reader = DictReader(csvfile)
            for i, row in enumerate(reader):
                try:
                    self.insert_row(row)
                except Exception as e:
                    print(f"Error handling row {i}: {row}\n{e}")

    def insert_row(self, row):
        program, org, contact = split_dicts(row, self.DICTS)

        # make the org first
        db_org, _ = Organization.objects.get_or_create(**org)
        # print(f"org = {org}, db = {db_org}")

        # then the contacts
        db_contact, _ = Contact.objects.get_or_create(**contact)
        # print(f"contact = {contact}, db = {db_contact}")

        # then the program - link up the right foreign key ids
        program['donations_accepted'] = program['donations_accepted'].find('Yes') != -1
        program['organization_id'] = db_org.id
        program['contact_id'] = db_contact.id
        db_program, _ = Program.objects.get_or_create(**program)
        # print(f"program = {program}, db = {db_program}")
