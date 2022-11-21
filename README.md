# hh_api_parser
## Description
This project used official API https://github.com/hhru/api
## Example of code
```
finder = HHVacanciesParser()
# Для примера рассмотрим удаленные вакансии QA во всех регионах кроме РФ, Украины и Беларуси.
areas = [dict_value['id'] for dict_value in finder.search_params['area'] if dict_value['name'] not in ['Россия','Украина','Беларусь']]
data = finder.find(text = 'QA', schedule = 'remote', area = areas, per_page = 100, page = 0, order_by = 'publication_time')
data
```
<img src="https://github.com/alexeiveselov92/hh_api_parser/blob/main/hh_parser_example_screen.png" alt="drawing" width=100%/>