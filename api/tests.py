from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import (
    Frequency,
    Type,
    Definition,
    Report
)
from .serializers import DefinitionSerializer
from .utilities import reverse_querystring


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
        self.bug_created = Type.objects.create(name="bug-created")
        self.bug_closed = Type.objects.create(name="bug-closed")

    def test_type(self):
        self.assertEqual(self.bug_created.name, "bug-created")
        self.assertTrue(self.bug_created.created_at != "")

        self.assertEqual(self.bug_closed.name, "bug-closed")
        self.assertTrue(self.bug_closed.created_at != "")


class DefinitionTestCase(TestCase):
    """Test case for Definition model"""

    def setUp(self):
        Frequency.objects.create(name="one-time")
        Type.objects.create(name="bug-created")
        one_time = Frequency.objects.get(name="one-time")
        bug_created = Type.objects.get(name="bug-created")
        self.definition = Definition.objects.create(
            frequency=one_time,
            type=bug_created,
            project_uuid="test101",
            roles=["tester", "manager"],
            users=["osho", "sushant"]
        )

    def test_def(self):
        self.assertEqual(self.definition.roles, ["tester", "manager"])
        self.assertTrue(self.definition.project_uuid != "")


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
        definition = Definition.objects.get(frequency=one_time)
        self.report = Report.objects.create(definition=definition, status="valid", attachment="file/to/path")

    def test_report(self):
        self.assertEqual(self.report.status, "valid")
        self.assertEqual(self.report.attachment, "file/to/path")


# Testcases for API endpoints
class FrequencyAPITests(APITestCase):
    """Testcase for Frequency endpoint"""

    def setUp(self):
        self.frequency = Frequency.objects.create(name="monthly")

    def test_list_frequency(self):
        """Ensure frequency list endpoint works properly."""
        url = reverse('frequency-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_frequency(self):
        """Ensure frequency detail endpoint works properly."""
        url = reverse('frequency-detail', args=[self.frequency.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Frequency.objects.get().name, self.frequency.name)


class TypeAPITests(APITestCase):
    """Testcase for Type endpoint"""

    def setUp(self):
        self.type = Type.objects.create(name="bug-created")

    def test_list_type(self):
        """
        Ensure type list endpoint works properly.
        """
        url = reverse('type-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_type(self):
        """
        Ensure type detail endpoint works properly.
        """
        url = reverse('type-detail', args=[self.type.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Type.objects.get().name, self.type.name)


class DefinitionAPITests(APITestCase):
    """Testcase for Definition endpoint"""

    def setUp(self):
        self.type = Type.objects.create(name="bug-created")
        self.frequency = Frequency.objects.create(name="monthly")
        self.def1 = Definition.objects.create(
            frequency=self.frequency, type=self.type,
            project_uuid="544", roles=["manager"],
            users=['IBC'])
        self.def2 = Definition.objects.create(
            frequency=self.frequency, type=self.type,
            project_uuid="4545", roles=["manager"],
            users=['IBC'])
        self.def3 = Definition.objects.create(
            frequency=self.frequency, type=self.type,
            project_uuid="e5e563", roles=["manager"],
            users=['IBC'])

    def test_create_definition(self):
        """
        Ensure definition create endpoint works properly.
        """
        url = reverse('definition-list')
        data = {
            'frequency': {
                "name": self.frequency.name,
                "created_at": self.frequency.created_at,
                "updated_at": self.frequency.updated_at
            },
            'type': {
                "name": self.type.name,
                "created_at": self.type.created_at,
                "updated_at": self.type.updated_at
            },
            "project_uuid": "545454",
            "roles": ["manager"],
            "users": ["IBC"]
        }
        data = DefinitionSerializer(data=data)
        # data.is_valid(raise_exception=True)
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Definition.objects.count(), 1)
        self.assertEqual(Definition.objects.get().project_uuid, data["project_uuid"])

    def test_list_definition(self):
        """
        Ensure definition list endpoint works properly.
        """
        url = reverse('definition-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_definition(self):
        """
        Ensure definition detail endpoint works properly.
        """
        url = reverse('definition-detail', args=[self.def1.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Definition.objects.get(id=self.def1.id).project_uuid, self.def1.project_uuid)

    def test_delete_definition(self):
        """
        Ensure definition delete endpoint works properly.
        """
        url = reverse('definition-detail', args=[self.def1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_bulk_delete_definition(self):
        """
        Ensure definiton bulk delete endpoint works properly.
        """
        url = reverse_querystring("definition-bulk-destroy", query_kwargs={"def_ids": f"{self.def2.id},{self.def3.id}"})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
