# hh_api_parser
## Example of code
```finder = HHVacanciesParser()
areas = [dict_value['id'] for dict_value in finder.search_params['area'] if dict_value['name'] not in ['Россия','Украина','Беларусь']]
data = finder.find(text = 'QA', schedule = 'remote', area = areas, per_page = 100, order_by = 'publication_time')
data
```
<img src="https://github.com/alexeiveselov92/hh_api_parser/blob/main/hh_parser_example_screen.png" alt="drawing" width=600/>