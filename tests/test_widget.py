from tw2.core.testbase import WidgetTest
from tw2.jqplugins.chosen.widgets import (
    ChosenSingleSelectField,
    ChosenMultipleSelectField,
)


class TestChosenSingleSelectField(WidgetTest):
    engines = ['mako', 'genshi']
    widget = ChosenSingleSelectField
    attrs = {'id': 'chosen-test', 'options': ['Red', 'Blue']}
    params = {}
    expected = """
    <select id="chosen-test" name="chosen-test">
            <option></option><option value="Red">Red</option><option
            value="Blue">Blue</option>
            </select>"""


class TestChosenMultipleSelectField(WidgetTest):
    engines = ['mako', 'genshi']
    widget = ChosenMultipleSelectField
    attrs = {'id': 'chosen-test', 'options': ['Red', 'Blue']}
    params = {}
    expected = """
    <select multiple="multiple" id="chosen-test" name="chosen-test">
            <option value="Red">Red</option><option
            value="Blue">Blue</option>
            </select>"""
