from command import Command, CommandData


def list_files_in_current_directory(data: CommandData):
    for entry in data.cwd.iterdir():
        if entry.is_file():
            print(entry.name)


list_command = Command(
    ["List", "LS", "DIR"],
    "Print list of files in current directory",
    list_files_in_current_directory,
)
