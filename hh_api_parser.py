import requests
import pandas as pd

#### base classes
class BaseRequest:
    url: str = None
    params: dict = dict()
    all_params = None
    def __init__(self):
        if not self.url: raise ValueError('Class property "url" must be a working link!')
    def get(self, params = None):
        params = self.params if not params else params
        return requests.get(self.url, params).json()

#### dictionaries classes
class DictionariesRequest(BaseRequest):
    url = 'https://api.hh.ru/dictionaries'
class AreasRequest(BaseRequest):
    url = 'https://api.hh.ru/areas'
class SpecializationsRequest(BaseRequest):
    url = 'https://api.hh.ru/specialization'
class IndustriesRequest(BaseRequest):
    url = 'https://api.hh.ru/industries'
dictionaries = DictionariesRequest().get()
areas = AreasRequest().get()
specializations = SpecializationsRequest().get()
industries = IndustriesRequest().get()
hosts = ['hh.ru','rabota.by','hh1.az','hh.uz','hh.kz','headhunter.ge','headhunter.kg']

#### search classes
class VacanciesRequest(BaseRequest):
    url = 'https://api.hh.ru/vacancies'
    params = {
        'text':'',
        'search_field':None,
        'experience':None,
        'employment':None,
        'schedule':None,
        'area':None,
        'metro':None,
        'specialization':None,
        'industry':None,
        'employer_id':None,
        'currency':None,
        'salary':None,
        'only_with_salary':None,
        'label':None,
        'period':None,
        'date_from':None,
        'date_to':None,
        'responses_count_enabled':'true',
        'per_page':None,
        'page':None,
        'order_by':None,
        'search_field':None
    }
    all_params = {
        'search_field':dictionaries.get('vacancy_search_field'),
        'experience':dictionaries.get('experience'),
        'employment':dictionaries.get('employment'),
        'schedule':dictionaries.get('schedule'),
        'currency':dictionaries.get('currency'),
        'label':dictionaries.get('vacancy_label'),
        'order_by':dictionaries.get('vacancy_search_order'),
        'area':areas,
        'specialization':specializations,
        'industry':industries   
    }
class EmployersRequest(BaseRequest):
    url = 'https://api.hh.ru/employers'
    params = {
        'text':None,
        'area':None,
        'type':None,
        'only_with_vacancies':None,
        'page':None,
        'per_page':None,
        'host':None
    }
    all_params = {
        'area':areas,
        'type':dictionaries.get('employer_type'),
        'host':hosts
    }
class HHVacanciesParser:
    search_params = VacanciesRequest().all_params
    last_search_fount_items = None
    last_search_kwargs = None
    def __init__(self):
        pass
    def get_json_items(self, **kwargs):
        kwargs = locals()['kwargs']
        self.last_search_kwargs = kwargs
        r = VacanciesRequest().get(params = kwargs)
        self.last_search_fount_items = r.get('found')
        return r.get('items')
    def find(self, text = '', search_field = 'name', area = None, responses_count_enabled = 'true', order_by = None, 
            experience = None, employment = None, schedule = None,  specialization = None, industry = None, employer_id = None, currency = None, label = None, date_from = None, date_to = None, per_page = None, page = None):
        kwargs = locals()
        del kwargs['self']
        json_items = self.get_json_items(**kwargs)
        
        data = pd.DataFrame()
        ind = -1
        for item in json_items:
            ind += 1
            for item_property in item.keys():
                if type(item[item_property]) != dict:
                    data.loc[ind, item_property] = ''
                    data.at[ind, item_property] = item[item_property]
                else:
                    for item_subproperty in item[item_property].keys():
                        data.loc[ind, str(item_property) + '_' + str(item_subproperty)] = ''
                        data.at[ind, str(item_property) + '_' + str(item_subproperty)] = item[item_property][item_subproperty]
        return data