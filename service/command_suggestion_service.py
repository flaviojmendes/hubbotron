from fuzzywuzzy import process
from util.commands import Commands


async def execute_suggested_command(ctx):

    command_tuple = get_command(ctx.invoked_with)
    command = command_tuple[1]
    if is_default_command(command):
        command_module = Commands.get_instance().dictionary[command]['module']

        module = getattr(__import__('commands'), command_module)
        method = getattr(module, command)

        args = ctx.message.content.split(' ', 1)[1] if len(ctx.message.content.split(' ', 1)) > 1 else ''

        await method(ctx, args)


def is_default_command(command):
    if "module" in Commands.get_instance().dictionary[command]:
        return True
    return False


def get_command(cmd):
    cmd_dict = list(Commands.get_instance().dictionary.keys())
    ratios = process.extract(cmd, cmd_dict)
    return cmd_dict, ratios[0][0]
