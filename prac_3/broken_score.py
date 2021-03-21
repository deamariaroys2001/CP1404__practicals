
# program to determine score status

def main():
  score = float(input("Enter score: "))
  print("score_status (score) ")
   def score_status():
       if 100 >= score >= 90:
           return "Excellent"
       elif 90 > score >= 50:
           return "Passable"
       elif 0<= score < 50:
           return "Bad"
       else:
           return "Invalid score"
   score_status()
main()