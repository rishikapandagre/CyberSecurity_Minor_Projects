import joblib
from colorama import init, Fore, Style

init(autoreset=True)

model=joblib.load('phishing_model.pkl')
vectorizer = joblib.load("vectorizer.pkl")

def predict_url(url):
    features=vectorizer.transform([url])
    prediction=model.predict(features)[0]
    return "Phishing" if prediction==1 else "Legitimate"

def main():
    print(Fore.CYAN + Style.BRIGHT + "\n Phishing Link Detector")
    print(Fore.YELLOW + "Type 'exit' to quit \n")

    while True:
        url=input("Enter a URL to check ->").strip()
        if url.lower()=='exit':
            print(Fore.CYAN + "\n Goodbye! Stay safe Online...")
            break

        result=predict_url(url)
        if result == "Phishing":
            print(Fore.RED + Style.BRIGHT + "Result-> Phishing Link!")
        else:
            print(Fore.GREEN + Style.BRIGHT + "Result-> Legitimate Link!")

if __name__=="__main__":
    main()
        