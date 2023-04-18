from datetime import datetime

class Date:
    _date: str = ""
    _lang_selected: str = ""

    MONTH_TO_USE = {
        'FR': [
            'janvier', 'février', 'mars', 'avril', 'mai', 'juin',
            'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre'
        ],
        'EN': [
            'january', 'february', 'march', 'april', 'may', 'june',
            'jully', 'august', 'september', 'october', 'november', 'december'
        ]
    }

    def __init__(self, date, lang_selected):
        self._date = date
        self._lang_selected = lang_selected
    
    def convert_date_to_human_language(self):
        date_obj = datetime.strptime(self._date, "%Y/%m/%d")
        day = date_obj.day
        month = Date.MONTH_TO_USE[self._lang_selected][date_obj.month - 1]
        year = date_obj.year

        return [f"{day}{month}{year}"]
    
    def get_year_parts(self):
        date_obj = datetime.strptime(self._date, "%Y/%m/%d")
        year = date_obj.year
        last_two_digits = year % 100
        return [f"{last_two_digits}", f"{year}"]