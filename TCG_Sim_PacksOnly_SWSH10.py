import pandas as pd

# Read the file
data = pd.read_csv("SWSH10_Compiled_Simple_RH.csv",
                   header=0,
                   names=['Card_Name', 'Rarity', 'RH?', 'Number', 'Market_Price', 'Listed_Median', 'Adjusted_Price',
                          'Slot_1', 'Slot_2', 'Slot_3', 'Slot_4', 'Slot_5', 'Slot_6', 'Slot_7', 'Slot_8', 'Slot_9',
                          'Slot_10', 'Slot_11'])

# Save data as DataFrame
df = pd.DataFrame(data)

# Create Sim_Results DataFrame
Sim_Results = pd.DataFrame(columns=['Card_Name', 'Number', 'Adjusted_Price', 'Pk_Num'])

# Simulate a Booster Box worth of Packs. Increase i by 1 for each pack opened.
for i in range(1, 36001):
    # Select Series of Common Cards (Slots 1-5). Add Pack #. Merge to Sim_Results.
    Common_Cards = df.loc[:, ['Card_Name', 'Number', 'Rarity', 'Market_Price', 'Adjusted_Price']].sample(
        5, weights=df.Slot_1)
    Common_Cards['Pk_Num'] = i
    Sim_Results = Sim_Results.merge(Common_Cards, how='outer')
    # Select Series of Uncommon Cards (Slots 6-8). Add Pack #. Merge to Sim_Results.
    Uncommon_Cards = df.loc[:, ['Card_Name', 'Number', 'Rarity', 'Market_Price', 'Adjusted_Price']].sample(
        3, weights=df.Slot_6)
    Uncommon_Cards['Pk_Num'] = i
    Sim_Results = Sim_Results.merge(Uncommon_Cards, how='outer')
    # Select Illustration Rare/Reverse Holo/Radiant Rare (Slot 9). Add Pack #. Merge to Sim_Results.
    Ill_RH = df.loc[:, ['Card_Name', 'Number', 'Rarity', 'Market_Price', 'Adjusted_Price']].sample(
        1, weights=df.Slot_9)
    Ill_RH['Pk_Num'] = i
    Sim_Results = Sim_Results.merge(Ill_RH, how='outer')
    # Select Rare+ (Slot 10). Add Pack #. Merge to Sim_Results.
    Rare = df.loc[:, ['Card_Name', 'Number', 'Rarity', 'Market_Price', 'Adjusted_Price']].sample(
        1, weights=df.Slot_10)
    Rare['Pk_Num'] = i
    Sim_Results = Sim_Results.merge(Rare, how='outer')
    # Select Code Card (Slot 11). Add Pack #. Merge to Sim_Results.
    Code_Card = df.loc[:, ['Card_Name', 'Number', 'Rarity', 'Market_Price', 'Adjusted_Price']].sample(
        1, weights=df.Slot_11)
    Code_Card['Pk_Num'] = i
    Sim_Results = Sim_Results.merge(Code_Card, how='outer')
    print("Pack ", i, " Completed.")

Sim_Results.to_csv('Pack_Sim_Results_SWSH10.csv', encoding='utf-8', index=False)
