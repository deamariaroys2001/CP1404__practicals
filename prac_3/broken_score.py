
# program to determine score status

def main():
    score = float(input("Enter score: "))
    print("score_status (score) ")

def score_status():
    if  score >= 90:
        return "Excellent"
    elif  score >= 50:
        return "Passable"
    elif 0<= score < 50:
        return "Bad"
    else:
        return "Invalid score"
main()