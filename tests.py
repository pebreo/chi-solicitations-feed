import pytest
import requests
import lxml.html

TIMEOUT = 2
SOLICITATIONS_URL = 'https://webapps1.cityofchicago.org/VCSearchWeb/org/cityofchicago/vcsearch/controller/solicitations/begin.do?agencyId=city'
CONTRACTS_AWARDS_URL = 'https://webapps1.cityofchicago.org/VCSearchWeb/org/cityofchicago/vcsearch/controller/contracts/begin.do?agencyId=city'


class TestSolicitationsPage:
    
    @classmethod
    def setup_class(cls):
        cls.the_url = SOLICITATIONS_URL
        cls.resp = requests.get(cls.the_url)
        cls.html_root = lxml.html.fromstring(cls.resp.content)

    def assertExists(self, html_root, xpath_str):
        if html_root.xpath(xpath_str):
            return True
        return False

    def test_that_the_solicitation_page_exists(self):
        assert self.resp.status_code == 200
        assert 'City of Chicago Solicitations' in self.resp.content
        assert len(self.resp.content) > 250 
 
    def test_that_search_button_exists(self):
        self.assertExists(self.html_root, '//input[@alt="search button"]')

    def test_that_fromDate_field_exists(self):
        self.assertExists(self.html_root, '//input[@id="fromDateId"]')
    
    def test_that_toDate_field_exists(self):
        self.assertExists(self.html_root, '//input[@id="toDateId"]')

    def test_that_minimum_award_field_exists(self):
        self.assertExists(self.html_root, '//input[@name="{actionForm.awardAmountMin}"]')

    def test_that_maximum_award_field_exists(self):
        self.assertExists(self.html_root, '//input[@name="{actionForm.awardAmountMax}"]')


class TestContractsAwardsPage:
    
    @classmethod
    def setup_class(cls):
        cls.the_url = CONTRACTS_AWARDS_URL
        cls.resp = requests.get(cls.the_url)
        cls.html_root = lxml.html.fromstring(cls.resp.content)

    def assertExists(self, html_root, xpath_str):
        if html_root.xpath(xpath_str):
            return True
        return False

    def test_that_the_solicitation_page_exists(self):
        assert self.resp.status_code == 200
        assert 'City of Chicago Contracts and Awards' in self.resp.content
        assert len(self.resp.content) > 250 
 
    def test_that_search_button_exists(self):
        self.assertExists(self.html_root, '//input[@alt="search button"]')

    def test_that_fromDate_field_exists(self):
        self.assertExists(self.html_root, '//input[@id="fromDateId"]')
    
    def test_that_toDate_field_exists(self):
        self.assertExists(self.html_root, '//input[@id="toDateId"]')

    def test_that_minimum_award_field_exists(self):
        self.assertExists(self.html_root, '//input[@name="{actionForm.awardAmountMin}"]')

    def test_that_maximum_award_field_exists(self):
        self.assertExists(self.html_root, '//input[@name="{actionForm.awardAmountMax}"]')
