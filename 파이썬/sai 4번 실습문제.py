import pandas as pd

pl_df = pd.read_csv('/mnt/data/pl_records.txt', delimiter='\s+')
laliga_df = pd.read_csv('/mnt/data/laliga_records.txt', delimiter='\s+')

combined_df = pd.concat([pl_df, laliga_df], ignore_index=True)

combined_df['Attack_pts'] = combined_df['Goals'] + combined_df['Assists']

def calculate_rating(attack_pts):
    if attack_pts >= 9:
        return "Incredible"
    elif attack_pts >= 6:
        return "Great"
    else:
        return "Good"

combined_df['Rating'] = combined_df['Attack_pts'].apply(calculate_rating)

combined_df.to_csv('combined_player_stats.csv', index=False)

print(combined_df)