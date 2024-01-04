'''
Generate a Menu
'''

def generate_a_menu(initial_text: str, elements: dict):
        n = 0

        text_array = [
            f"{initial_text}\n", 
            *[f"{item['id']}. {item['name']}\n" for item in elements],
            '> ',
        ]

        while(n == 0):
            user_input = int(input("".join(text_array)))

            value = list(filter(lambda x: x['id'] == user_input, elements))
            n = value[0]['id'] if len(value) else 0

            if n == 0:
                print("Opción no disponible\n")
        
        return n
