from utils.exceptions import (
    UnexpectedArgumentError,
    MissingValueError,
    TooManyArgumentsError,
)


class Argument:
    """
    Represents a command line argument with a type, name, and optional value.

    Attributes:
        type (int): Type of the argument (e.g., INTEGER, STRING).
        name (str): Name of the argument.
        value (any, optional): Value of the argument,
                               defaults to None.
    """

    # Argument types
    INTEGER = 1
    STRING = 2
    FLAG = 3
    FLAG_WITH_INTEGER = 4
    FLAG_WITH_STRING = 5
    LIST = 6

    def __init__(self, arg_type: int, arg_name: str, arg_value=None) -> None:
        """
        Initializes an Argument instance.

        Args:
            arg_type (int): The type of the argument.
            arg_name (str): The name of the argument.
            arg_value (any, optional): The initial value of the argument.
                                       Defaults to None.
        """
        self.type = arg_type
        self.name = arg_name
        self.value = arg_value

    @staticmethod
    def populate_args(command_name: str, args_info: dict,
                      arg_list: [str]) -> dict:
        """
        Populates arguments based on the provided list of command line
        arguments.

        Args:
            args_info (dict): Information about expected arguments.
            arg_list (list[str]): List of command line arguments.

        Returns:
            dict: Updated args_info with populated arguments.

        Raises:
            MissingValueError: If a required value is missing.
            UnexpectedArgumentError: If an unexpected argument is encountered.
        """
        i = 0
        positional_count = 0
        seen_positional_args = False
        stop_positional_after_named_args = args_info.get(
            'stop_positional_after_named', True
        )

        while i < len(arg_list):
            arg = arg_list[i]
            if arg.startswith('-'):
                arg_name = arg[1:]
                if arg_name in args_info['named_args']:
                    # Handle named argument and update index if needed
                    # i.e -n 10 would consume two args
                    i = Argument.handle_named_arg(
                        command_name, args_info, arg_name, arg_list, i
                    )
                elif (
                    not seen_positional_args
                    or not stop_positional_after_named_args
                ):
                    positional_count += 1
                    Argument.handle_positional_arg(
                        command_name, args_info, arg, positional_count
                    )
                else:
                    raise UnexpectedArgumentError(command_name, arg)
            else:
                seen_positional_args = True
                Argument.handle_positional_arg(
                    command_name, args_info, arg, positional_count
                )
                positional_count += 1
            i += 1

        return args_info

    @staticmethod
    def handle_named_arg(command_name: str, args_info: dict, arg_name: str,
                         arg_list: [str], i: int) -> int:
        """
        Handles a named argument and updates its value in args_info.

        Args:
            args_info (dict): Information about expected arguments.
            arg_name (str): The name of the argument to handle.
            arg_list (list[str]): List of command line arguments.
            i (int): Current index in arg_list.

        Returns:
            int: Updated index after processing the named argument.

        Raises:
            MissingValueError: If a required value is missing for the
            named argument.
        """
        arg_obj = args_info['named_args'][arg_name]
        arg_obj.value = True
        if arg_obj.type != Argument.FLAG:
            if i + 1 < len(arg_list):
                arg_obj.value = Argument.convert_arg_value(
                    arg_list[i + 1], arg_obj.type
                )
                i += 1
            else:
                raise MissingValueError(command_name, arg_name)
        return i

    @staticmethod
    def handle_positional_arg(command_name: str, args_info: dict, arg: str,
                              positional_count: int) -> None:
        """
        Handles a positional argument and updates its value in args_info.

        Args:
            args_info (dict): Information about expected arguments.
            arg (str): The current argument to handle.
            positional_count (int): Count of positional arguments processed
            so far.

        Raises:
            UnexpectedArgumentError: If an unexpected positional argument is
            encountered.
            TooManyArgumentsError: If too many arguments are provided.
        """
        if positional_count < len(args_info['positional_args']):
            arg_obj = args_info['positional_args'][positional_count]
            arg_obj.value = Argument.convert_arg_value(arg, arg_obj.type)
        else:
            if len(args_info['positional_args']) == 0:
                raise UnexpectedArgumentError(command_name, arg)
            else:
                arg_obj = args_info['positional_args'][-1]
                if arg_obj.type == Argument.LIST:
                    arg_obj.value.append(
                        Argument.convert_arg_value(arg, Argument.STRING)
                    )
                else:
                    raise TooManyArgumentsError(command_name, arg)

    @staticmethod
    def convert_arg_value(arg_value: str, arg_type: int):
        """
        Converts the argument value to its appropriate type.

        Args:
            arg_value (str): The argument value as a string.
            arg_type (int): The type of the argument.

        Returns:
            any: The converted argument value.
        """
        converters = {
            Argument.INTEGER: int,
            Argument.STRING: str,
            Argument.LIST: lambda x: [x],
            Argument.FLAG_WITH_INTEGER: int,
            Argument.FLAG_WITH_STRING: str,
        }
        return (
            converters[arg_type](arg_value)
            if arg_type in converters
            else arg_value
        )

    @staticmethod
    def set_keys_to_readable(args_info: dict) -> dict:
        """
        Converts argument objects in args_info to a dictionary with
        readable keys.

        Args:
            args_info (dict): Information about expected arguments.

        Returns:
            dict: Dictionary with arguments as keys and their details as
            values.
        """
        return {
            arg.name: arg
            for arg in args_info['positional_args']
            + list(args_info['named_args'].values())
        }
