from dataclasses import dataclass

def full_sql_alchemist(data_cls):
    # Push your alchemy here
    pass


@full_sql_alchemist
@dataclass()
class LapisPhilosophorum:
    """
    Class represent the table
    Instanse represent the rows of the table
    """
    human_blood : int # whole number of liters
    alchemist_name: str # only knowing the truth
    red_mercury: float # import from USSR


if __name__ == '__main__':
    print(LapisPhilosophorum.__table__) # Print dataclass related table
    engine = ... # create your engine
    LapisPhilosophorum.create(engine) # Create table if not exist

    stone = LapisPhilosophorum(5, "Edward", 3.14)
    stone.insert(engine) # insert to table

    for item in LapisPhilosophorum.rows(engine): # read rows from table
        print(item)

