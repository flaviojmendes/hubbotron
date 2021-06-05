import re
import mimetypes
from io import BytesIO
import logging as puts
import os
import requests
import uuid
from collections import OrderedDict

from discord import File
from io import BytesIO


RANDOM_EXCEPTION_COMEBACKS = ["Are you dumb?", "No, I don't think I will."]


def mention(ctx, criteria):
    if len(criteria) < 3:
        return "Don't be evil."
    mentioned = ""
    for member in ctx.message.channel.members:
        if (criteria.lower() in member.display_name.lower()) or (criteria.lower() in member.name.lower()):
            mentioned += member.mention + " "
    return mentioned


def format_params(params):
    if params is None:
        return ""
    else:
        params_response = ""
        for param in params:
            params_response += "[{}] ".format(param)
        return params_response


def split_dict(input_dict, size):
    return_dict = OrderedDict()

    for k, v in sorted(input_dict.items()):
        if len(return_dict) == size:
            yield return_dict
            return_dict = OrderedDict()

        return_dict[k] = v

    yield return_dict
