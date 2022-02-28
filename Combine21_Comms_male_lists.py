# opens event lists and writes into new txt file
# this combines only the male comms ranking data into 1 txt file 

path = "/Users/newmac/Desktop/Programs and Code/"

filenames = [path + 'Toplist21_male_100m_CommsRank.txt', path + 'Toplist21_male_200m_CommsRank.txt', path + 'Toplist21_male_400m_CommsRank.txt', path + 'Toplist21_male_800m_CommsRank.txt', path + 'Toplist21_male_1500m_CommsRank.txt', path + 'Toplist21_male_3000msc_CommsRank.txt', path + 'Toplist21_male_5000m_CommsRank.txt', path + 'Toplist21_male_10000m_CommsRank.txt', path + 'Toplist21_male_110mh_CommsRank.txt', path + 'Toplist21_male_400mh_CommsRank.txt', path + 'Toplist21_male_long-jump_CommsRank.txt', path + 'Toplist21_male_triple-jump_CommsRank.txt', path + 'Toplist21_male_high-jump_CommsRank.txt', path + 'Toplist21_male_pole-vault_CommsRank.txt', path + 'Toplist21_male_discus-throw_CommsRank.txt', path + 'Toplist21_male_shot-put_CommsRank.txt', path + 'Toplist21_male_hammer-throw_CommsRank.txt', path + 'Toplist21_male_javelin-throw_CommsRank.txt', path + 'Toplist21_male_20km-race-walking_CommsRank.txt', path + 'Toplist21_male_marathon_CommsRank.txt']  # concatenate all events # add path + 'Toplist21_male_decathlon_CommsRank.txt' once hep included
with open('/Users/newmac/Desktop/Programs and Code/COMMS21_male_COMBINEDFILE.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line.replace(" : ", ":"))
