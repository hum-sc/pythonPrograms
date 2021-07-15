DATA = [
        {
            'name': 'Facundo',
            'age': 72,
            'organization': 'Platzi',
            'position': 'Technical Coach',
            'language': 'python',
        },
        {
            'name': 'Luisana',
            'age': 33,
            'organization': 'Globant',
            'position': 'UX Designer',
            'language': 'javascript',
        },
        {
            'name': 'Héctor',
            'age': 19,
            'organization': 'Platzi',
            'position': 'Associate',
            'language': 'ruby',
        },
        {
            'name': 'Gabriel',
            'age': 20,
            'organization': 'Platzi',
            'position': 'Associate',
            'language': 'javascript',
        },
        {
            'name': 'Isabella',
            'age': 30,
            'organization': 'Platzi',
            'position': 'QA Manager',
            'language': 'java',
        },
        {
            'name': 'Karo',
            'age': 23,
            'organization': 'Everis',
            'position': 'Backend Developer',
            'language': 'python',
        },
        {
            'name': 'Ariel',
            'age': 32,
            'organization': 'Rappi',
            'position': 'Support',
            'language': '',
        },
        {
            'name': 'Juan',
            'age': 17,
            'organization': '',
            'position': 'Student',
            'language': 'go',
        },
        {
            'name': 'Pablo',
            'age': 32,
            'organization': 'Master',
            'position': 'Human Resources Manager',
            'language': 'python',
        },
        {
            'name': 'Lorena',
            'age': 56,
            'organization': 'Python Organization',
            'position': 'Language Maker',
            'language': 'python',
        },
    ]


def run():
    """ {
            'name': 'Facundo',
            'age': 72,
            'organization': 'Platzi',
            'position': 'Technical Coach',
            'language': 'python',
        } 
    """
    all_python_devs =list( map( lambda worker : worker['name'], 
        filter( lambda worker : worker['language'] == 'python', DATA )))
    
    all_platzi_workers = list()
    all_platzi_workers=list(map(lambda worker : worker['name'],
        filter(lambda worker : worker['organization'] == 'Platzi',DATA )))

    adults = [worker for worker in DATA if worker['age'] > 17]
    old_people = [worker | {'old': worker['age'] > 69} for worker in adults]

    for i in old_people:
        print(i)



if __name__ == '__main__':
    run()