from django.test import TestCase

class AverageRateTest(TestCase):
    def test_avg_rate(self):
        response = self.client.get('/exchanges/gbp/2023-01-02')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "5.2768")
    
    def test_avg_rate_invalid_currency(self):
        response = self.client.get('/exchanges/abc/2023-01-02')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Invalid currency code or date is out of range")

    def test_avg_rate_invalid_date_range(self):
        response = self.client.get('/exchanges/gbp/2100-02-02')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Invalid currency code or date is out of range")

    def test_avg_rate_invalid_date_format(self):
        response = self.client.get('/exchanges/gbp/02-01-2023')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Date format should be YYYY-MM-DD")
    
    def test_avg_rate_not_working_day(self):
        response = self.client.get('/exchanges/gbp/2023-01-01')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Date is not a working day")
    
    def test_avg_rate_invalid_date_format_range(self):
        response = self.client.get('/exchanges/gbp/2023-27-01')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Invalid date format. Should be YYYY-MM-DD")

    def test_avg_rate_invalid_request(self):
        response = self.client.get('/exchanges/gbp/2023-01-02/abc')
        self.assertEqual(response.status_code, 404)
    
class MinMaxAverageTest(TestCase):
    def test_min_max_avg(self):
        response = self.client.get('/exchanges/average/gbp/5')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "min")
        self.assertContains(response, "max")

    def test_min_max_avg_invalid_currency(self):
        response = self.client.get('/exchanges/average/abc/5')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Invalid currency code")

    def test_min_max_avg_invalid_last_days_range(self):
        response = self.client.get('/exchanges/average/gbp/300')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Maximal value of last days (N) is 255")

    def test_min_max_avg_invalid_request(self):
        response = self.client.get('/exchanges/average/gbp/abc')
        self.assertEqual(response.status_code, 404)
    
class DifferenceTest(TestCase):
    def test_difference(self):
        response = self.client.get('/exchanges/difference/gbp/5')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "max_diff")
    
    def test_difference_invalid_currency(self):
        response = self.client.get('/exchanges/difference/abc/5')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Invalid currency code")

    def test_difference_invalid_last_days_range(self):
        response = self.client.get('/exchanges/difference/gbp/300')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Maximal value of last days (N) is 255")

    def test_difference_invalid_request(self):
        response = self.client.get('/exchanges/difference/gbp/abc')
        self.assertEqual(response.status_code, 404)
