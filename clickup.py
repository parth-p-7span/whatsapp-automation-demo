import constants
import requests
import pytz
import json

tz_IN = pytz.timezone('Asia/Kolkata')


def create_new_task(name):
    response = requests.post(
        url=constants.list_url,
        headers=constants.clickup_header,
        data=json.dumps(
            {"name": name}
        )
    )
    return response.json()


def update_task_name(task_id, name):
    response = requests.put(
        url=f'{constants.get_task}/{task_id}',
        headers=constants.clickup_header,
        data=json.dumps({"name": name})
    )
    return response.json()


def set_custom_field_value(task_id, field_id, value):
    response = requests.post(
        url=f'{constants.get_task}/{task_id}/field/{field_id}',
        headers=constants.clickup_header,
        data=json.dumps({"value": value})
    )
    return response.json()


def get_user_data(whatsapp_id):
    response = requests.get(
        url='%s?custom_fields=[{"field_id": "%s", "operator":"=", "value": "%s"}]' % (
            constants.list_url, constants.whatsapp_field_id, whatsapp_id),
        headers=constants.clickup_header
    )
    # if response.json()
    task_data = response.json()['tasks'][0]['custom_fields']
    data = []
    for field in task_data:
        if 'value' in field:
            data.append(1)
        else:
            data.append(0)
    final_data = arrange(data)
    task_id = response.json()['tasks'][0]['id']
    # return task_id, final_data
    return response.json()


def arrange(data):
    """[ctc, email, exp, name, last_comp, loc, med, mob, ski, sum, wa] -> [wa, name, email, mob, ski, exp, last_comp, ctc, loc, sum, med]"""
    return [data[10], data[3], data[1], data[7], data[8], data[2], data[4], data[0], data[5], data[9], data[6]]

