from shell_parser.executors.executor import Executor
from commands.commandFactory import CommandFactory
from utils.argument_handler import ArgumentHandler


class Call(Executor):
    """
    This class represents an implementation of the Executor
    for executing commands.

    It provides functionality to handle command execution by taking a command
    and its arguments, processing them using an Config,
    and then executing the command using a CommandFactory.
    """

    def __init__(self, command: str, args: [str]) -> None:
        """
        Initializes a new instance of the Call class.

        Args:
            command (str): The command to be executed.
            args ([str]): A list of arguments for the command.
        """

        super().__init__()

        self.command = command
        self._args = args

    def evaluate(self, input: str = None) -> [str]:
        """
        Executes the command with the provided arguments and optional additional input.

        This method uses the CommandFactory to execute the command and returns the result.

        Args:
            input (str, optional): Additional input that may be required for command execution.
                                    Defaults to None

        Returns:
            [str]: The output from the executed command.
        """

        args = ArgumentHandler.assign_arguments(self.command, self._args)

        return [
            *filter(
                lambda x: x,
                [CommandFactory().execute_command(self.command, args, input)],
            )
        ]
