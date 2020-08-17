from watchman.decorators import check
from psutil import disk_usage, cpu_percent, virtual_memory, swap_memory
from django.conf import settings
from apps.api_ditec.configs_api import (PATH_NOTICIAS, PATH_PROGRAMA_RADIO,
                                        PATH_PROGRAMA_TV, PATH_RADIOAGENCIA)
from requests import get


@check
def check_used_disk():
    hdd = disk_usage('/').percent
    if hdd <= 90.0:
        response = {'Storage Disk': {"ok": True}}
    else:
        response = {'Storage Disk': {"ok": False}}

    return response


@check
def check_used_memory():
    percent = virtual_memory().percent
    if percent <= 90.0:
        response = {'Virtual Memory': {"ok": True}}
    else:
        response = {'Virtual Memory': {"ok": False}}

    return response


@check
def check_used_swap():
    percent = swap_memory().percent
    if percent <= 90.0:
        response = {'Swap Memory': {"ok": True}}
    else:
        response = {'Swap Memory': {"ok": False}}

    return response


@check
def check_used_cpu():
    percent = cpu_percent()
    if percent <= 90.0:
        response = {'CPU': {"ok": True}}
    else:
        response = {'CPU': {"ok": False}}
    return response


@check
def check_api_noticias():
    response_status = get(settings.API_DITEC + PATH_NOTICIAS)
    if response_status.ok:
        response = {'API NOTICIAS': {"ok": True}}
    else:
        response = {'API NOTICIAS': {"ok": False}}

    return response


@check
def check_api_programa_tv():
    response_status = get(settings.API_DITEC + PATH_PROGRAMA_TV)
    if response_status.ok:
        response = {'API PROGRAMA TV': {"ok": True}}
    else:
        response = {'API PROGRAMA TV': {"ok": False}}

    return response


@check
def check_api_programa_radio():
    response_status = get(settings.API_DITEC + PATH_PROGRAMA_RADIO)
    if response_status.ok:
        response = {'API PROGRAMA RADIO': {"ok": True}}
    else:
        response = {'API PROGRAMA RADIO': {"ok": False}}

    return response


@check
def check_api_radioagencia():
    response_status = get(settings.API_DITEC + PATH_RADIOAGENCIA)
    if response_status.ok:
        response = {'API RADIOAGENCIA': {"ok": True}}
    else:
        response = {'API RADIOAGENCIA': {"ok": False}}

    return response
