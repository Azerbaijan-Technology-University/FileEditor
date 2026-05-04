from command import Command, CommandData


def edit_file(data: CommandData):
    pass


edit_command = Command(["Edit", "Open"], "Create/Edit file", edit_file)
