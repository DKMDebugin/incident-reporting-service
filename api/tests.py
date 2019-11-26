from django.test import TestCase

from api.models import (
            Frequency,
            Type,
            Definition,
            Report
            )

# Testcases for Models

class FrequencyTestCase(TestCase):
    """Test case for Frequency model"""
    def setUp(self):
        Frequency.objects.create(name="one-time")
        Frequency.objects.create(name="daily")

    def test_frequency_name_time(self):
        one_time = Frequency.objects.get(name="one-time")
        daily = Frequency.objects.get(name="daily")

        self.assertEqual(one_time.name, 'one-time')
        self.assertTrue(one_time.created_at != "")

        self.assertEqual(daily.name, 'daily')
        self.assertTrue(daily.created_at != "")

class TypeTestCase(TestCase):
    """Test case for Type model"""
    def setUp(self):
        Type.objects.create(name="bug-created")
        Type.objects.create(name="bug-closed")

    def test_type(self):
        bug_created = Type.objects.get(name="bug-created")
        bug_closed = Type.objects.get(name="bug-closed")

        self.assertEqual(bug_created.name, "bug-created")
        self.assertTrue(bug_created.created_at != "")

        self.assertEqual(bug_closed.name, "bug-closed")
        self.assertTrue(bug_closed.created_at != "")

class DefinitionTestCase(TestCase):
    """Test case for Definition model"""
    def setUp(self):
        Frequency.objects.create(name="one-time")
        Type.objects.create(name="bug-created")
        self.one_time = Frequency.objects.get(name="one-time")
        self.bug_created = Type.objects.get(name="bug-created")
        Definition.objects.create(
                        frequency=self.one_time,
                        type=self.bug_created,
                        project_uuid="test101",
                        roles=["tester", "manager"],
                        users=["osho", "sushant"]
                        )

    def test_def(self):
        definition = Definition.objects.get(frequency=self.one_time)

        self.assertEqual(definition.roles, ["tester", "manager"])
        self.assertTrue(definition.project_uuid != "")

class ReportTestCase(TestCase):
    """Test case for Report model"""
    def setUp(self):
        Frequency.objects.create(name="one-time")
        Type.objects.create(name="bug-created")
        one_time = Frequency.objects.get(name="one-time")
        bug_created = Type.objects.get(name="bug-created")
        Definition.objects.create(
                        frequency=one_time,
                        type=bug_created,
                        project_uuid="test101",
                        roles=["tester", "manager"],
                        users=["osho", "sushant"]
                        )
        self.definition = Definition.objects.get(frequency=one_time)
        Report.objects.create(definition=self.definition, status="valid", attachment="file/to/path")

    def test_report(self):
        report = Report.objects.get(definition=self.definition)

        self.assertEqual(report.status, "valid")
        self.assertEqual(report.attachment, "file/to/path")


# Testcases for API endpoints
