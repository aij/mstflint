#######################################################
#
# QueryCommand.py
# Python implementation of the Class QueryCommand
# Generated by Enterprise Architect
# Created on:      14-Aug-2019 10:12:00 AM
# Original author: talve
#
#######################################################
from commands.ResDumpCommand import ResDumpCommand
from commands.CommandFactory import CommandFactory
from utils import constants
from validation.CapabilityValidator import CapabilityValidator
from resource_data.QueryData import QueryData
from resource_data.DataPrinter import DataPrinter
from utils import constants as cs


class QueryCommand(ResDumpCommand):
    """This class is responsible for performing the query command flow by validate,
    getting the data and print it.
    """

    def __init__(self, **kwargs):
        """QueryCommand initialization.
        """
        self.device_name = kwargs[cs.UI_ARG_DEVICE]
        self.vHCAid = kwargs[cs.UI_ARG_VHCAID]
        self.data = None

    def get_data(self):
        """call the QueryData for getting the menu data.
        """
        self.data = QueryData.get_query(self.device_name, self.vHCAid)

    def print_data(self):
        """call the data printer with the right configuration for print the menu to screen.
        """
        DataPrinter.print_query_data(self.data)

    def validate(self):
        """call the capability validator and check if the core dump supported by the FW.
        """

        if CapabilityValidator.validate():
            return True
        else:
            raise Exception("Resource Dump register is not supported by the FW")


CommandFactory.register(constants.RESOURCE_DUMP_COMMAND_TYPE_QUERY, QueryCommand)