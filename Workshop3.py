import csv
import random
file_handle = open('c:/YOUR--PATH/Countries.csv')
reader = csv.DictReader(file_handle)
countries = list(reader)
file_handle.close()

# cleaning up the country list
country_list = [row['country'] for row in countries]  # list of countries only
country_space = []
for item in country_list:
    country_space.append(item.strip())  # strips leading/trailing whitespace from country list
country_only = []
for item in country_space:
     country_only.append(item.casefold())  # renders the country list caseless to match the user's input

#global variables
answer = random.choice(countries)       # full answer including country, lat, long
the_country = answer['country']         # random country
the_latitude = answer['lat']                 # latitude of random country
the_longitude = answer['long']               # longitude of random country
max_attempts = 10                       # maximum attempts

# get the new file
log = open('c:/YOUR--PATH/log.txt', 'w')

def user_name():
    name = input('What is your name?') # records the user's name
    log.write(name)
    log.write("\n")

def guess_display():
    guess = input('What country am I?').casefold()
    log.write(guess)
    log.write("\n")
    if guess not in country_only:
         print('Invalid input, please try again')
    
def game_rules():   # this function defines game rules
    attempts = 0    # start at 0 attempts
    name = user_name()
    guess = guess_display()
    while attempts < max_attempts:
        attempts += 1
        guess = guess_display()
        if the_latitude > guess['lat']: 
            print('Further north!')
        else: 
            print('Further south!')
        if the_longitude > guess['long']: 
            print('Go east') 
        else: 
            print('Go west')
        if guess == the_country.casefold():
            print('Well done! You have identified the country :)')
            break
    if attempts >= max_attempts:
            print(f'You are out of guesses :( The answer is {the_country}')
            log.write('The answer is ')
            log.write(the_country)

game_rules()  # runs the game

log.close()  # closes the log.txt file after the game is complete
