from utils import open_data
from utils import get_executed_operation
from utils import sort_operations_by_date
from utils import format_date
from utils import quantity_sort_operations_by_date
from utils import account_mask



new_list=open_data("operations.json")
right_list=get_executed_operation(new_list)
sort_list=sort_operations_by_date(right_list)
five_operations = quantity_sort_operations_by_date(sort_list,5)



for item in five_operations:
    data_operationAmount = item['operationAmount']
    data_operationAmount_currency = data_operationAmount['currency']
    key_value_from = item.get('from', "")
    key_value_to = item.get('to', "")

    date = format_date(item['date'])
    mask_from = account_mask(key_value_from)
    mask_to = account_mask(key_value_to)
    if len(mask_from) != 0:
        mask_from += " -> "

    print(date, item['description'])
    print(mask_from, mask_to, sep="")
    print(data_operationAmount['amount'], data_operationAmount_currency['name'])
    print("")
