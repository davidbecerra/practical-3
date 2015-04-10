import numpy as np
import csv
from sklearn import preprocessing


## Given user params, returns a numpy vector representing this user
def vectorizeUser(sex, age, countryID):
  '''
  Given the sex, age, and countryID of a user, creates a corresponding numpy
  integer vector to represent this data

  Returns: numpy vector with 4 integer components
    First component is 1 if sex is male, o/w 0
    Second component is 1 if sex is femail, o/w 0
    Third component is age
    Fourth component is countryID
       ['m'?, 'f'?, age, countryID]
    The vectors are not standardized
  '''
  vector = []
  gender = []
  if sex is 'm':
    gender = [1, 0]
  else:
    gender = [0, 1]
  vector += gender
  vector += [age]
  vector += [countryID]
  return vector

## Read through profiles.csv and convert each user into a vector. returns vectors
def read_users():
  '''
  Vectorizes each user in profiles.csv. Iterates through each user and extracts
  sex, age, and country. Each country will have a unique id. Then, vectorizeUser
  is called to use this data to create a numpy vector for the user. Vector
  inserted into user_data dictionary

  Returns: user_data: a dictionary mapping user ids to numpy vector for that user.

  See vectorizeUser for details on numpy vector for each user
  '''
  user_file = 'profiles.csv'

  user_data = {}
  countryIDs = []
  # Read through users csv to vectorize each user and put into user_data dictionary
  with open(user_file, 'r') as user_fh:
    user_csv = csv.reader(user_fh, delimiter=',', quotechar='"')
    next(user_csv, None) # skip header
    for row in user_csv:
      user    = row[0]
      sex     = row[1]
      age     = row[2]
      country = row[3]

      if not age: age = 0 # age is empty field - make 0
      age = int(age)
      # Get country ID
      if country not in countryIDs:
        countryIDs.append(country)
      countryID = countryIDs.index(country)
      # Convert data into numpy vector
      user_vector = vectorizeUser(sex, age, countryID)
      # Insert into dictionary
      user_data[user] = user_vector
  return user_data

def read_artists():
  artist_file = 'artists.csv'

  artist_data = {}
  with open(artist_file, 'r') as artist_fh:
    artist_csv = csv.reader(artist_fh, delimiter=',', quotechar='"')
    next(artist_csv, None)
    for row in artist_csv:
      artistID = row[0]
  return artist_data

def read_artists_bin():
  artist_file = 'artists_bin.csv'

  artist_data = {}
  with open(artist_file, 'r') as artist_fh:
    artist_csv = csv.reader(artist_fh, delimiter=',', quotechar='"')
    next(artist_csv, None)
    for row in artist_csv:
      artist_data[row[0]] = row[1:]
  return artist_data

def get_data():
  train_file = 'train.csv'

  print "Getting user data...",
  user_data = read_users()
  print "Done!"
  artist_data = read_artists_bin()
  print len(user_data)

  print "Getting data from training file...",
  train_data = []
  with open(train_file, 'r') as train_fh:
    train_csv = csv.reader(train_fh, delimiter=',', quotechar='"')
    next(train_csv, None)
    for row in train_csv:
      user    = row[0]
      artist  = row[1].translate(None, '-')
      plays   = row[2]
      if user not in user_data:
        print "ERROR: user not found."
        exit()
      datum = list(user_data[user])
      datum += [int(artist, 16)]
      datum.append(int(plays)) 
      train_data.append(datum)

  print "Done!"
  print "Converting into numpy matrix...",
  X = np.array(train_data)
  print "Done!"
  print X.shape

def main():
  get_data()


if __name__ == '__main__':
  main()