def saving_paths():
    return {
        'investment_button': '//*[@id="Placements"]/a',
        'date_text': '//*[@id="content"]/div[3]',
        'contract_number_account_type': '//*[@id="content"]/div[1]/div[1]/div/span',
        'investment_type': '//*[@id="content"]/div[4]/div[1]/div/div[1]',
        'rate': '//*[@id="content"]/div[4]/div[2]/table/tbody/tr[2]/td[1]',
        'balance': '//*[@id="content"]/div[4]/div[2]/table/tbody/tr[2]/td[2]'
    }



def fund_paths():
    return {
        'table_body':{
            'main_body': '//*[@id="content"]/div[4]/div[2]/table/tbody/*',
            'table_rows':  ".//*"
        }
    }

def client_paths():
    return {
        'contract_specifications': '//*[@id="Specifications"]/a',
        'personal_information': '//*[@id="content"]/div[3]/table[2]/tbody/tr[4]/td[2]/a',
        'table_client':{
            'main_client': '//*[@id="search_content"]/div/div[3]/table/tbody/tr',
            'row_client': './td[2]'
        }
    }

def participant_paths():
    return{
        'contract_number': '//*[@id="content"]/div[3]/table[1]/tbody/tr[1]/td[2]',
        'table_participant':{
            'main_participant': '//*[@id="content"]/div[1]/div[1]/table/tbody/tr',
            'role_participant': './td[1]',
            'name_participant':'./td[2]',
            'birthday_participant':'./td[3]'
        }
    }
def beneficiary_paths():
    return{
        'contract_number':'//*[@id="content"]/div[3]/table[1]/tbody/tr[1]/td[2]',
        'table_beneficiary':{
            'main_beneficiary': '//*[@id="content"]/div[3]/div[2]/table/tbody/tr',
            'name_beneficiary': './td[1]',
            'allocation_beneficiary': './td[2]',
            'relationship_beneficiary': './td[3]',
            'class_beneficiary': './td[4]'

        }

    }