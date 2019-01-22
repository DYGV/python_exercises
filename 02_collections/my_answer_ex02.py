# coding : utf-8

def main(names):
    is_Angy = lambda name : name == 'Angy'
    
    for idx, name in enumerate(names):
        if(is_Angy(name)):
            print('{0}.My name is {1}'.format(idx, name))
        else:
            print('{0}.{1} is my classmate'.format(idx, name))

if __name__ == "__main__":
    names = ("Bill", "Anne", "Angy", "Cony", "Daniel", "Occhan")
    main(names)
