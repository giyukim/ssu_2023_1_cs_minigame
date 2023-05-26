def main():
    def get_score(grade):
        if(grade == "F"):
            return 0.0
        return 4.5 - 0.5 * ["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0"].index(grade)
    grade_sum = 0.0
    sum = 0
    for i in range(20):
        raw = list(input().split(' '))[1:]
        if not raw[1] == "P":
            grade_sum += get_score(raw[1]) * float(raw[0])
            sum += float(raw[0])
    print("%.6f"%(grade_sum / sum))

if __name__ == "__main__":
    main()