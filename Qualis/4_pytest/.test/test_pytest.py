import sys
import os
import re

sys.path.append(os.getcwd())

from mytest import test_inventory
import autopep8
from xml.etree import ElementTree
import pytest
import inspect


@pytest.fixture
def get_xml_root_element(source):
    xml = ElementTree.parse(source)
    root = xml.getroot()
    return root


@pytest.mark.parametrize(
    "source, expected", [("pytestresult.xml", 18)], ids=["test_testcase_result"]
)
def test_pytest_testcase_result(get_xml_root_element, expected):
    test_case_success = (
        int(get_xml_root_element[0].attrib["tests"])
        - int(get_xml_root_element[0].attrib["failures"])
        - int(get_xml_root_element[0].attrib["errors"])
        - int(get_xml_root_element[0].attrib["skipped"])
    )
    print(test_case_success)
    assert (
        int(get_xml_root_element[0].attrib["tests"]) == expected
        and test_case_success == expected
    )


@pytest.mark.parametrize(
    "source, expected", [("coverage.xml", 18)], ids=["test_coverage_result"]
)
def test_pytest_coverage_result(get_xml_root_element, expected):
    line_coverage_status = (
        int(get_xml_root_element.attrib["lines-valid"])
        == int(get_xml_root_element.attrib["lines-covered"])
    ) and (int(float(get_xml_root_element.attrib["line-rate"])) == 1)
    branch_coverage_status = (
        int(get_xml_root_element.attrib["branches-valid"])
        == int(get_xml_root_element.attrib["branches-covered"])
    ) and (int(float(get_xml_root_element.attrib["branch-rate"])) == 1)
    assert line_coverage_status and branch_coverage_status
