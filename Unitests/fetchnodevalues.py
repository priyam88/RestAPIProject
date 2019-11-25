import json
import jsonpath
import unittest


class TestFetchNodeValues(unittest.TestCase):

    response_json = ""

    def setUp(self):
        data_file_path = "/Users/Mohan/PycharmProjects/RestAPIAssgn/Resources/response.json"
        with open(data_file_path, 'r') as data_file_object:
            response_data = data_file_object.read()
        self.response_json = json.loads(response_data)

    def test_username(self):
        username = jsonpath.jsonpath(self.response_json, "username")
        print("username: " + username[0])
        self.assertEqual(username[0], "aa@m.com")

    def test_sessionid(self):
        sessionid = jsonpath.jsonpath(self.response_json, "sessionid")
        print("sessionid: " + str(sessionid[0]))
        self.assertEqual(sessionid[0], [12, 23, 34, 56])

        print("sessionid last value: " + str(sessionid[0][-1]))
        last_value = sessionid[0][-1]
        self.assertIs(last_value, 56)

    def test_students(self):
        contacts = jsonpath.jsonpath(self.response_json, "students[0:2].contact")
        print("Contacts of all students: " + str(contacts))
        self.assertEqual(contacts, [["1234", "3456"], ["4534", "3456"]])

    def test_second_student(self):
        # Marks
        student2_marks = jsonpath.jsonpath(self.response_json, "students[1].marks")
        print("Second student marks: " + str(student2_marks[0]))
        self.assertEqual(student2_marks[0], [20, 25, 22])
        # Contact
        student2_contact = jsonpath.jsonpath(self.response_json, "students[1].contact[1]")
        print("Second contact value of second student: " + student2_contact[0])
        self.assertEqual(student2_contact[0], "3456")
        # Cities
        student2_cities = jsonpath.jsonpath(self.response_json, "students[1].adresss[0:2].city")
        print("Second student cities: " + str(student2_cities))
        self.assertIn("abc", student2_cities)
        self.assertIn("xyz", student2_cities)

    def test_first_student(self):
        # State
        student1_state = jsonpath.jsonpath(self.response_json, "students[0].adresss[1].state")
        print("First student's second state value: " + student1_state[0])
        self.assertEqual(student1_state[0], "ca")
        # Address
        student1_adress = jsonpath.jsonpath(self.response_json, "students[0].adresss")
        print("First student address: " + str(student1_adress[0]))
        self.assertEqual(student1_adress[0], [ {"state": "nc", "city": "abc"}, {"state": "ca", "city": "xyz"}])


unittest.main()
