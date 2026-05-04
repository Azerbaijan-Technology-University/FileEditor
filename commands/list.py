from command import Command, CommandData


def list_files_in_current_directory(data: CommandData):
    pass


list_command = Command(
    ["List", "LS", "DIR"],
    "Print list of files in current directory",
    list_files_in_current_directory,
)
