import os
import json

def is_disposable_mail(target_mail, other_disposible_domain_list = [], override=False):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "disposable_domains.json")    
    with open(file_path, "r") as f:
        disposable_domain_list = json.load(f)
    if override is False:
        disposable_domain_list += other_disposible_domain_list
    else:
        disposable_domain_list = other_disposible_domain_list
    target_domain = target_mail.partition("@")[2]
    for disposable_domain in disposable_domain_list:
        if disposable_domain == target_domain:
            return True
    return False