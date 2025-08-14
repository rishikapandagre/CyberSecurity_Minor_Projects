import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

data = pd.read_csv("phishing-links.txt", names=["URL", "Label"])
data['Label'] = data['Label'].apply(lambda x: 1 if x== 'Phishing' else 0)

vectorizer=TfidfVectorizer()
X=vectorizer.fit_transform(data['URL'])
Y=data['Label']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, Y_train)

joblib.dump(model, 'phishing_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

print("Model trained and saved using phishing-links.txt")

# Evaluate
accuracy = model.score(X_test, Y_test)
print(f"Model Accuracy: {accuracy:.2f}")
