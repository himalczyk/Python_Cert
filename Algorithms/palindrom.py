text = "Co mi dał duch? Cud, ład i moc."

# text_cleaned = []

clean_text = [t.upper() for t in text if t.isalpha()]

# clean_text = [text_cleaned.append(t.upper()) for t in text if t.isalpha()]

print(clean_text[: len(clean_text)//2] == clean_text[: len(clean_text)//2:-1])