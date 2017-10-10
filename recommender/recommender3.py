import codecs 
# from math import sqrt

users2 = {"Amy": {"Taylor Swift": 4, "PSY": 3, "Whitney Houston": 4},
          "Ben": {"Taylor Swift": 5, "PSY": 2},
          "Clara": {"PSY": 3.5, "Whitney Houston": 4},
          "Daisy": {"Taylor Swift": 5, "Whitney Houston": 3}}

class recommender:

   def __init__(self, data, k=1, metric='pearson', n=5):
      """ initialize recommender
      currently, if data is dictionary the recommender is initialized
      to it.
      For all other data types of data, no initialization occurs
      k is the k value for k nearest neighbor
      metric is which distance formula to use
      n is the maximum number of recommendations to make"""

      self.k = k
      self.n = n
      self.username2id = {}
      self.userid2name = {}
      self.productid2name = {}
      #
      # The following two variables are used for Slope One
      # 
      self.frequencies = {}
      self.deviations = {}
      # for some reason I want to save the name of the metric
      self.metric = metric
      if self.metric == 'pearson':
         self.fn = self.pearson
      #
      # if data is dictionary set recommender data to it
      #
      if type(data).__name__ == 'dict':
         self.data = data

   def convertProductID2name(self, id):
      """Given product id number return product name"""
      if id in self.productid2name:
         return self.productid2name[id]
      else:
         return id


   def userRatings(self, id, n):
      """ not used in this program """
      pass


   def showUserTopItems(self, user, n):
      """ show top n items for user"""
      items = list(self.data[user].items())
      items.sort(key=lambda itemTuple: itemTuple[1], reverse=True)
      for i in range(n):
         print("%s\t%i" % (self.convertProductID2name(items[i][0]),
                           items[i][1]))
            
   def loadMovieLens(self, path=''):
      self.data = {}
      #
      # first load movie ratings
      #
      i = 0
      #
      # First load book ratings into self.data
      #
      #f = codecs.open(path + "u.data", 'r', 'utf8')
      f = codecs.open(path + "u.data", 'r', 'ascii')
      #  f = open(path + "u.data")
      for line in f:
         i += 1
         #separate line into fields
         fields = line.split('\t')
         user = fields[0]
         movie = fields[1]
         rating = int(fields[2].strip().strip('"'))
         if user in self.data:
            currentRatings = self.data[user]
         else:
            currentRatings = {}
         currentRatings[movie] = rating
         self.data[user] = currentRatings
      f.close()
      #
      # Now load movie into self.productid2name
      # the file u.item contains movie id, title, release date among
      # other fields
      #
      #f = codecs.open(path + "u.item", 'r', 'utf8')
      f = codecs.open(path + "u.item", 'r', 'iso8859-1', 'ignore')
      #f = open(path + "u.item")
      for line in f:
         i += 1
         #separate line into fields
         fields = line.split('|')
         mid = fields[0].strip()
         title = fields[1].strip()
         self.productid2name[mid] = title
      f.close()
      #
      #  Now load user info into both self.userid2name
      #  and self.username2id
      #
      #f = codecs.open(path + "u.user", 'r', 'utf8')
      f = open(path + "u.user")
      for line in f:
         i += 1
         fields = line.split('|')
         userid = fields[0].strip('"')
         self.userid2name[userid] = line
         self.username2id[line] = userid
      f.close()
      print(i)                
        
   def computeDeviations(self):
      # for each person in the data:
      #    get their ratings
      for ratings in self.data.values():
         # for each item & rating in that set of ratings:
         for (item, rating) in ratings.items():
            self.frequencies.setdefault(item, {})
            self.deviations.setdefault(item, {})                    
            # for each item2 & rating2 in that set of ratings:
            for (item2, rating2) in ratings.items():
               if item != item2:
                  # add the difference between the ratings to our
                  # computation
                  self.frequencies[item].setdefault(item2, 0)
                  self.deviations[item].setdefault(item2, 0.0)
                  self.frequencies[item][item2] += 1
                  self.deviations[item][item2] += rating - rating2
        
      for (item, ratings) in self.deviations.items():
         for item2 in ratings:
            ratings[item2] /= self.frequencies[item][item2]


   def slopeOneRecommendations(self, userRatings):
      recommendations = {}
      frequencies = {}
      # for every item and rating in the user's recommendations
      for (userItem, userRating) in userRatings.items():
         # for every item in our dataset that the user didn't rate
         for (diffItem, diffRatings) in self.deviations.items():
            if diffItem not in userRatings and \
               userItem in self.deviations[diffItem]:
               freq = self.frequencies[diffItem][userItem]
               recommendations.setdefault(diffItem, 0.0)
               frequencies.setdefault(diffItem, 0)
               # add to the running sum representing the numerator
               # of the formula
               recommendations[diffItem] += (diffRatings[userItem] +
                                             userRating) * freq
               # keep a running sum of the frequency of diffitem
               frequencies[diffItem] += freq
      recommendations =  [(self.convertProductID2name(k),
                           v / frequencies[k])
                          for (k, v) in recommendations.items()]
      # finally sort and return
      recommendations.sort(key=lambda artistTuple: artistTuple[1],
                           reverse = True)
      # I am only going to return the first 50 recommendations
      return recommendations[:50]
        
   def pearson(self, rating1, rating2):
       """ not used in this program """
       pass


   def computeNearestNeighbor(self, username):
       """ not used in this program """
       pass

   def recommend(self, user):
       """ not used in this program """
       pass
  
r = recommender(users2)
r.computeDeviations()
print ("The deviations are: ", r.deviations)


r = recommender(users2)
r.computeDeviations()
g = users2['Ben']
print ("\nRecommend to Ben are (Slope One): ", r.slopeOneRecommendations(g))

# Moive len example 
r = recommender(0)
r.loadMovieLens('./movielen/')
r.showUserTopItems(user = '1', 50)
r.computeDeviations()
print ("The deviations are: ", r.deviations)
r.slopeOneRecommendations(r.data['1'])
r.slopeOneRecommendations(r.data['25'])