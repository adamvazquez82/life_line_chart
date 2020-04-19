# import pytest
# from life_line_chart import GedcomParsing
from life_line_chart import ReadGedcom
import os, sys


def test_read_sample_file():
    data = ReadGedcom.read_data(os.path.join(os.path.dirname(__file__),'gramps_sample.ged'))
    assert len(data[0]) == 42
    assert len(data[1]) == 15
    assert str(data[0]['@I1@']) == "{'tag_data': 'INDI', 'NAME': {'tag_data': 'Keith Lloyd /Smith/', 'GIVN': {'tag_data': 'Keith Lloyd'}, 'SURN': {'tag_data': 'Smith'}}, 'SEX': {'tag_data': 'M'}, 'BIRT': {'tag_data': '', 'TYPE': {'tag_data': 'Birth of Keith Lloyd Smith'}, 'DATE': {'tag_data': '11 AUG 1966'}, 'PLAC': {'tag_data': 'San Francisco, San Francisco Co., CA'}}, 'FAMC': {'tag_data': '@F8@'}, 'CHAN': {'tag_data': '', 'DATE': {'tag_data': '21 DEC 2007', 'TIME': {'tag_data': '01:35:26'}}}}"
    assert str(data[1]['@F1@']) == "{'tag_data': 'FAM', 'HUSB': {'tag_data': '@I27@'}, 'WIFE': {'tag_data': '@I25@'}, 'MARR': {'tag_data': '', 'TYPE': {'tag_data': 'Marriage of Ingeman Smith and Marta Ericsdotter'}, 'DATE': {'tag_data': 'ABT 1790'}, 'PLAC': {'tag_data': 'Sweden'}}, 'CHIL': {'tag_data': '@I39@'}, 'CHAN': {'tag_data': '', 'DATE': {'tag_data': '21 DEC 2007', 'TIME': {'tag_data': '01:35:26'}}}}"

def test_read_testdata_file():
    data = ReadGedcom.read_data(os.path.join(os.path.dirname(__file__),'autogenerated.ged'))
    assert len(data[0]) == 1361
    assert len(data[1]) == 498
    assert str(data[0]['@I1@']) == "{'tag_data': 'INDI', 'NAME': {'tag_data': 'Stephen /Demetro/'}, 'SEX': {'tag_data': 'M'}, 'BIRT': {'tag_data': '', 'DATE': {'tag_data': '1 JUN 1001'}, 'PLAC': {'tag_data': 'Paris'}}, 'DEAT': {'tag_data': '', 'DATE': {'tag_data': '1 JUN 1060'}, 'PLAC': {'tag_data': 'Bruegge'}}, 'FAMS': {'tag_data': '@F1@'}}"
    assert str(data[1]['@F1@']) == "{'tag_data': 'FAM', 'HUSB': {'tag_data': '@I1@'}, 'WIFE': {'tag_data': '@I2@'}, 'MARR': {'tag_data': '', 'DATE': {'tag_data': '1 MAY 1021'}, 'PLAC': {'tag_data': 'Tokio'}}, 'CHIL': {'tag_data': '@I3@\\n@I4@\\n@I5@'}}"


