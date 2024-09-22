import pandas as pd
import re

def clean_user_data(input_file, output_file):
    df = pd.read_csv(input_file)
    df_cleaned = df.drop_duplicates(subset='user_id')

    def is_valid_email(email):
        regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.match(regex, email)

    df_cleaned = df_cleaned[df_cleaned['email'].apply(is_valid_email)]
    df_cleaned.to_csv(output_file, index=False)

if __name__ == "__main__":
    clean_user_data('user_data.csv', 'cleaned_user_data.csv')
